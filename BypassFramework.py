#!/usr/bin/python

from termcolor import colored
import os
import logging
import sys
from core.functions import *
import readline
from module.memory.CreateFiber import *
from module.memory.QueueUserAPC import *
from module.Separation.imageShell import *

python_version = sys.version_info[0]

if python_version != 3:
    print(colored("[-] Unable to run ", "red"))
    print(colored("[-] Please run FourEye with python 3", "red"))
    sys.exit()


banner()

while True:
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
    try:
        command = input("\033[4mFourEye\033[0m"+colored(" >>", "green"))
        if command == "exit":
            break

        if command == "list":
            list()

        if command == "help":
            help()

        if command.split(" ")[0] == "shellcode":
            readline.set_completer(shellcode_completer)
            readline.parse_and_bind("tab: complete")
            while True:
                try:
                    exe_command = input("\033[4mFourEye(shellcode)\033[0m"+colored(" >>", "green"))
                    if exe_command == "back":
                        break

                    if exe_command == "list":
                        bypass_list()

                    if exe_command == "exit":
                        sys.exit()

                    if exe_command.split(" ")[0] == "1":
                        while True:
                            try:
                                bypass1_command = input("\033[4mFourEye(shellcode_bypass1)\033[0m" + colored(" >>", "green"))
                                if bypass1_command == "rot13":
                                    Fiber_rot_13()
                                if bypass1_command == "xor":
                                    Fiber_xor_13()
                                if bypass1_command == "execute":
                                    shellcode_execute()
                                if bypass1_command == "exit":
                                    sys.exit()
                                if bypass1_command == "back":
                                    break
                            except EOFError:
                                print(" ")

                    if exe_command.split(" ")[0] == "2":
                        while True:
                            try:
                                bypass2_command = input("\033[4mFourEye(shellcode_bypass2)\033[0m" + colored(" >>", "green"))
                                if bypass2_command == "rot13":
                                    Queue_rot_13()
                                if bypass2_command == "xor":
                                    Queue_xor_13()
                                if bypass2_command == "execute":
                                    shellcode2_execute()
                                if bypass2_command == "exit":
                                    sys.exit()
                                if bypass2_command == "back":
                                    break
                            except EOFError:
                                print(" ")
                    if exe_command.split(" ")[0] == "3":
                        while True:
                            try:
                                bypass3_command = input("\033[4mFourEye(shellcode_bypass3)\033[0m" + colored(" >>", "green"))
                                if bypass3_command == "png":
                                    imageSehllcode()
                                if bypass3_command == "execute":
                                    shellcode_execute()
                                if bypass3_command == "exit":
                                    sys.exit()
                                if bypass3_command == "back":
                                    break
                            except EOFError:
                                print(" ")

                except EOFError:
                    print(" ")
    except EOFError:
        print(" ")