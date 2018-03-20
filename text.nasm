    SECTION .data       ; data section
msg:    db "Hello World",10 ; the string to print, 10=cr
len:    equ $-msg       ; "$" means "here"
%macro test #a #b
    mov eax,#a
    mov ebx,#b
    %mend

%Sdef awesome 10 

%macro text #a
    test 5,6
    %mend
        
                ; len is a value, not an address

    SECTION .text       ; code section
        global main     ; make label available to linker 
main:               ; standard  gcc  entry point


	
    text 6,awesome	
    
    mov edx,len     ; arg3, length of string to print
    mov ecx,msg     ; arg2, pointer to string
    mov ebx,1       ; arg1, where to write, screen
    mov eax,4       ; write sysout command to int 80 hex
    int 0x80        ; interrupt 80 hex, call kernel
    
    mov ebx,0       ; exit code, 0=normal
    mov eax,1       ; exit command to kernel
    int 0x80        ; interrupt 80 hex, call kernel
