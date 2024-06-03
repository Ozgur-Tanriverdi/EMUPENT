.DATA
MSG1 DB 'Left button clicked$'
MSG2 DB 'Right button clicked$'
MSG3 DB 'Middle button clicked and program ended.$'
.CODE
main_loop:

; Check mouse button status
mov eax, 3
int 33h

; Compare for left button click
mov ecx,1
cmp ebx,ecx
jne check_right
je go_left
jmp main_loop

check_right:   ; Compare for right button click
mov ecx,2
cmp ebx,ecx
jne check_middle 
je go_right


check_middle: ; Compare for middle button
mov edx,offset MSG3
mov ah, 09h
int 21h
jmp end

go_right:     ; Display right button message
mov edx,offset MSG2
mov ah, 09h
int 21h
jmp main_loop

go_left:     ; Display left button message

mov edx,offset MSG1
mov ah, 09h
int 21h
jmp main_loop

end:         ; End program
