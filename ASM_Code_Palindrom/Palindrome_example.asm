.data
msg     db 'Enter a word: $'
msg4 db 'WELCOME TO THE PALINDROME EXPERIMENT $'
msg5 db 'To check whether the letters from the first digit to the median digit of a word are identical to the letters from the last digit to the median digit (If the string is more than 30 letters, you will get an error message.): $'
msg1     db 'It is a Palindrome $'
msg2     db 'It is not a Palindrome $'
msg3     db 'Length is too long $'
buffer  db 10,?, 10 dup('$')  
.code
mov edx,offset msg4    ;Load the address of the "WELCOME TO THE PALINDROME EXPERIMENT" message into edx
mov ah,09h		       ;Set AH to 09h (invoke string printing service)
int 21h                ;Call interrupt to print the message

mov edx,offset msg5    ;Load the address of the explanation message for palindrome check into edx
mov ah,09h             ;Set AH to 09h (invoke string printing service)
int 21h		           ;Call interrupt to print the message

ank:
mov edx,offset msg     ;Load the address of the message prompting for user input into edx
mov ah,09h             ;Set AH to 09h (invoke string printing service)
int 21h                ;Call interrupt to print the message

mov edx,offset buffer  ;Load the address of buffer to edx to get user input
mov ah,0Ah		       ;Set AH to 0Ah (invoke buffered input service)
int 21h                ;Call interrupt to get input from the user

mov edi,esi            ;Copy the address of input from ESI to EDI
mov eax,[buffer]       ;Get the length of input stored in buffer
dec eax                ;Because an extra byte is stored in the buffer structure after the 0Ah call
add edi,eax            ;Set EDI to point to the end of input
mov ebx,30             ;Load 30 which is the MAXIMUM Length into EBX 
cmp ebx,eax            ;Check if the length of input is less than 30
jl print_msg3          ;If it's less than 30, jump to print_msg3
check_palindrome:
mov eax,[esi]          ;Get a character from the start address
mov ebx,[edi]          ;Get a character from the end address
cmp eax,ebx            ;Compare the characters
jne print_message2     ;If they are different, jump to print_message2
inc esi                ;Move the start address to the next character
dec edi                ;Move the end address to the previous character
cmp edi,esi            ;Check if there is an intersection between EDI and ESI
jl check_palindrome    ;If there's no intersection, continue palindrome check

print_message:         ;Print msg1 which is 'It is a Palindrome'
mov edx,offset msg1    
mov ah,09h
int 21h
jmp ank

print_message2:        ;Print msg2 which is 'It is not a Palindrome'
mov edx,offset msg2
mov ah,09h
int 21h
jmp ank

print_msg3:            ;Print msg3 which is 'Length is too long'
mov edx,offset msg3
mov ah,09h
int 21h
jmp ank                ;Jump to ank

