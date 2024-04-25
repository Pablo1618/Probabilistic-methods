#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <chrono>

using namespace std;

extern "C" double assembly_inverse_distribution(float randomNumber);

int inverse_distribution(float randomNumber) {
    return 50.0 + (100.0 * randomNumber);
}

double change_distribution(float randomNumber) {

    // 0.05 0.15 0.25 0.55
    if (randomNumber < 0.05) {
        return 1;
    }
    if (randomNumber < 0.20) {
        return 2;
    }
    if (randomNumber < 0.45) {
        return 3;
    }
    
    return 4;

}

int main() {

    srand(time(NULL));


    // liczby 1 2 3 4 z prawopodobienstwami kolejno 20% 30% 40% 10%
    int counterOne = 0;
    int counterTwo = 0;
    int counterThree = 0;
    int counterFour = 0;

    for (int i = 0; i < 100000; i++) {

        float randomNumber = ((float)rand() / (RAND_MAX));
        int number = change_distribution(randomNumber);
        switch (number) {
        case 1:
            counterOne++;
            break;
        case 2:
            counterTwo++;
            break;
        case 3:
            counterThree++;
            break;
        case 4:
            counterFour++;
            break;
        default:
            break;
        }
    }

    cout << "Liczby 1,2,3,4" << endl;
    cout << " 1: " << counterOne << endl;
    cout << " 2: " << counterTwo << endl;
    cout << " 3: " << counterThree << endl;
    cout << " 4: " << counterFour << endl << endl;



    vector<int> counts(10, 0);

    int rangeSize = 100;
    int step = rangeSize / 10;

    auto start = chrono::high_resolution_clock::now();

    cout << "Liczba 50-150" << endl;
    for (int i = 0; i < 100000; i++) {
        float randomNumber = ((float)rand() / (RAND_MAX));
        //double number = inverse_distribution(randomNumber);
        double number = assembly_inverse_distribution(randomNumber);
        //cout << " " << number << endl;
        int intervalIndex = (number - 50) / step;
        if (intervalIndex >= 0 && intervalIndex < 10) {
            counts[intervalIndex]++;
        }
    }

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);

    for (int i = 0; i < 10; i++) {
        cout << i * step + 50 << "-" << (i + 1) * step + 50 - 1 << ": " << counts[i] << endl;
    }

    cout << endl << "Czas: " << duration.count() << " mikrosekund" << endl;

    return 0;
}