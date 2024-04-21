.data
msg     db 'Enter a word: $'
msg4 db 'WELCOME TO THE PALINDROME EXPERIMENT $'
msg5 db 'To check whether the letters from the first digit to the median digit of a word are identical to the letters from the last digit to the median digit (If the string is more than 30 letters, you will get an error message.): $'
msg1     db 'It is a Palindrom $'
msg2     db 'It is not a Palindrom $'
msg3     db 'Length is too long $'
buffer  db 10,?, 10 dup('$')  
.code
mov edx,offset msg4
mov ah,09h
int 21h

mov edx,offset msg5
mov ah,09h
int 21h

ank:
mov edx,offset msg
mov ah,09h
int 21h

mov edx,offset buffer
mov ah,0Ah
int 21h

mov edi,esi
mov eax,[buffer]
dec eax
add edi,eax
mov ebx,30
cmp ebx,eax
jl print_msg3
check_palindrome:
mov eax,[esi]
mov ebx,[edi]
cmp eax,ebx
jne print_message2
inc esi
dec edi
cmp edi,esi
jl check_palindrome

print_message:
mov edx,offset msg1
mov ah,09h
int 21h
jmp ank

print_message2:
mov edx,offset msg2
mov ah,09h
int 21h
jmp ank

print_msg3:
mov edx,offset msg3
mov ah,09h
int 21h
jmp ank




















