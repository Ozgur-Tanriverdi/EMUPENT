.data
msg     db 'Enter a word:: $'
msg1     db 'It is a Palindrom $'
msg2     db 'It is not a Palindrom $'
buffer  db 10,?, 10 dup('$')  
.code
mov edx,offset msg
mov ah,09h
int 21h

mov edx,offset buffer
mov ah,0Ah
int 21h

mov edi,esi
mov eax,4
add edi,eax



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

ank: