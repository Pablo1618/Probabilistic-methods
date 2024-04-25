.686
.XMM
.model flat

.data

piecdziesiat dq 50.0
sto dq 100.0

.code

_assembly_inverse_distribution PROC
push ebp
mov ebp, esp

; Pobieranie pierwszego argumentu z stosu
fld dword ptr [ebp+8] ; Pierwszy argument
fld qword ptr [sto]



fmul

fld qword ptr [piecdziesiat]

fadd


; wynik na wierzcholku stosu
pop ebp

ret
_assembly_inverse_distribution ENDP

END