.data
msg     db 'Technically, anything with a microprocessor can be considered a robot.$' ; Define the message to be printed

.code
mov edx, offset msg    ; Load the address of the message into EDX
mov ah, 09h            ; Set AH to 09h (invoke string printing service)
int 21h                ; Call interrupt to print the message

mov ebx, 0             ; Initialize EBX to 0 (used as a comparison value)
mov ecx, 1             ; Initialize ECX to 1 (used as a counter)

loop:
mov eax, [esi]         ; Load the value at ESI into EAX
inc esi                ; Increment ESI to point to the next character
cmp eax, 20h           ; Compare EAX with the ASCII value of a space (' ')
je pluss               ; If equal, jump to pluss (increment the counter)
cmp eax, 24h           ; Compare EAX with the ASCII value of '$' (end of message)
cmp eax, ebx           ; Compare EAX with the value in EBX (0)
je decision            ; If equal, jump to decision
jmp loop               ; Otherwise, repeat the loop

pluss:
inc ecx                ; Increment the counter
jmp loop               ; Continue the loop

decision:
mov ebx, 9             ; Set EBX to 9 for comparison
cmp ebx, ecx           ; Compare EBX with ECX (counter)
jne over_9             ; If not equal, jump to over_9

mov eax, 30h           ; Load the ASCII value of '0' into EAX
add ecx, eax           ; Convert the counter to its ASCII value
mov edx, ecx           ; Move the ASCII value to EDX for printing
mov ah, 02h            ; Set AH to 02h (invoke character printing service)
int 21h                ; Call interrupt to print the character

over_9:
mov eax, ecx           ; Move the counter value to EAX
mov ebx, 10            ; Set EBX to 10 for division
div ebx                ; Divide EAX by 10 (result in EAX, remainder in EDX)
mov edi, edx           ; Move the remainder to EDI
mov edx, eax           ; Move the quotient to EDX

mov eax, 30h           ; Load the ASCII value of '0' into EAX
add edx, eax           ; Convert the quotient to its ASCII value
mov ah, 02h            ; Set AH to 02h (invoke character printing service)
int 21h                ; Call interrupt to print the character

mov edx, edi           ; Move the remainder (stored in EDI) to EDX
mov eax, 30h           ; Load the ASCII value of '0' into EAX
add edx, eax           ; Convert the remainder to its ASCII value
mov ah, 02h            ; Set AH to 02h (invoke character printing service)
int 21h                ; Call interrupt to print the character
