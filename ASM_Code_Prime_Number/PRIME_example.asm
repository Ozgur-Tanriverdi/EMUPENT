MOV BH,0        ; Initialize BH register to 0
MOV CL,7        ; CL is the number that is checked to be prime
MOV AL,CL       ; Move the value of CL to AL (to use as dividend in division operation)
mov dl,2        ; Move the value 2 to DL (to use as divisor in division operation)
div dl          ; Divide AX by DL (AL: quotient, AH: remainder)
cmp edx,ebx     ; Compare the remainder (in EDX) with EBX (which is not initialized yet)
je false        ; Jump to 'false' label if remainder equals EBX (which it won't initially)

MOV BL,02H      ; Set BL to 02H (start divisor for checking prime)
MOV DX,0        ; Set DX to 0 (to avoid Divide overflow error)
MOV AH,0        ; Set AH to 0 (to avoid Divide overflow error)

; Loop to check for Prime No
start:
DIV BL          ; Divide AX by BL (AL: quotient, AH: remainder)
MOV ah,dl       ; Move the remainder (in DL) to AH
mov dl,0        ; Clear DL for next operation
CMP AH,DL       ; Compare AH (remainder) with DL (0)
jne next        ; If not equal, jump to 'next' label
INC BH          ; Increment BH (to count the number of factors)
next:
MOV DL,2        ; Reset DL to 2 (for next division operation)
CMP BH,DL       ; Compare BH with 2 (check if it's prime or not)
je false        ; If BH equals 2, jump to 'false' label (it's not a prime number)
INC BL          ; Increment BL (to check next potential divisor)
MOV AX,0000H    ; Clear AX (to avoid Divide overflow error)
MOV DX,0000H    ; Clear DX (to avoid Divide overflow error)
MOV AL,CL       ; Restore the original value of the number to AL
MOV AH,00H      ; Set AH to 0
CMP BL,AL       ; Compare BL with AL (to run loop until BL matches the number)
jne start       ; If not equal, jump back to 'start' label to continue checking

true:           ; PRIME
MOV DX,AX       ; Move the value of AX (which is the original number) to DX
JMP exit        ; Jump to 'exit' section

false: 		; NOT PRIME
MOV DX,65535    ; Move 65535 to DX (a value to indicate it's not prime)
JMP exit        ; Jump to 'exit' section

exit:
MOV AL,CL       ; Move the original value of the number back to AL
MOV CL,0        ; Clear CL