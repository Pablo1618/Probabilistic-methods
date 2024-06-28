#include <iostream>
#include <time.h>

using namespace std;

int main() {
	srand(time(NULL));
	float xy_table[4][4] = {{ 0.1,		0,		0,		0.4		},
							{ 0.2,		0,		0,		0		},
							{ 0,		0.1,	0,		0.1	},
							{ 0,		0,		0.1,	0	} };

	// Sumowanie wierszy - prawdopodobienstwo danego wiersza
	cout << "Tabelka P_i" << endl;
	float P_xi[4] = { 0 };
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			P_xi[i] += xy_table[i][j];
		}
		cout << P_xi[i] << " ";
	}
	cout << endl << endl;


	// Prawdopodobienstwo y jesli x=i
	float prob_y_if_x[4][4] = { { 0 }, { 0 }, { 0 }, { 0 } };
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			prob_y_if_x[j][i] = xy_table[j][i] / P_xi[j];
		}
	}
	cout << "Pr. y jesli x: " << endl;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cout << prob_y_if_x[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;


	//////////
	
	// Prawdopodobienstwo wylosowania danego wiersza (X), w ostatnim pr.==1.0
	float row_prob[4] = { 0 };
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j <= i; j++) {
			row_prob[i] += P_xi[j];
		}
	}

	// Prawdopodobienstwo wylosowania danej kolumny (Y) jesli wylosowano dany wiersz, w ostatnim pr.==1.0
	float prob_column_if_row[4][4] = { { 0 }, { 0 }, { 0 }, { 0 } };
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k <= i; k++) {
				prob_column_if_row[j][i] += prob_y_if_x[j][k];
			}
		}
	}

	// Losowanie wynikow
	int results[4][4] = { { 0 }, { 0 }, { 0 }, { 0 } };

	for (int i = 0; i < 100000; i++) {
		float x = (float)rand() / (float)RAND_MAX;
		float y = (float)rand() / (float)RAND_MAX;

		int row_index = 0;
		int column_index = 0;

		// Losowanie wiersza
		for (int i = 0; i < 4; i++) {
			if (x < row_prob[i]) {
				row_index = i;
				break;
			}
		}

		// Losowanie kolumny
		for (int j = 0; j < 4; j++) {
			if (y < prob_column_if_row[row_index][j]) {
				column_index = j;
				break;
			}
		}

		results[row_index][column_index]++;
	}

	cout << "Wyniki: " << endl;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cout << results[i][j] << "		";
		}
		cout << endl;
	}
	return 0;
}