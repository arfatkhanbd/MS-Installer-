# Author : Arfat_Khan 
# github : https://www.github.com/arfatkhanbd
#facebook : https://www.facebook.com/akbullethz0.2
import os 
import sys 
from time import sleep 
def jalan2(*z):
    for e in z[0]+'\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.10)
    for m in z[1]+'\n':
        sys.stdout.write(m)
        sys.stdout.flush()
        sleep(0.12)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.06)
def sh():
    try :
        print("\x1b[1;93m")
        k="▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇"
        for i in k:
            print(i)
            sleep(0.8)
    except :
        pass 
        
def sh2():
    try :
        print("\x1b[1;95m")
        k="▇▇▇▇▇▇"
        for i in k:
            print(i)
            sleep(0.2)
    except :
        pass 

def wlcm():
    os.system("clear")
    print("\x1b[1;95m\n\n\n\n")
    name=input("Tomar Name Ki Bro :").upper()
    if name =="":
        jalan("\n\ninput your name....")
        wlcm()
    name=name+" bro, Ami ARFAT_KHAN ai tool tar bulider, tomak onk onk Dhonnobad ai tool ta use korar jono, dowa korio bro jate next time aro valo tool nea hajir hote pari :-)"
    print("\x1b[1;94m")
    jalan2("\t\t Hello ",name)
def install():
    os.system("clear")
    jalan("Checking status........")
    sh()
    os.system("clear")
    jalan("it will take 20-30 m........... \n\n")
    jalan("installing metasploit........... ")
    sh2()
    try:
        os.system("pkg update && pkg upgrade && pkg install git curl wget nmap -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh")
        os.system("clear")
        os.system("./msfconsole")
        exit()
    except :
        os.system("clear")
        jalan(" There is an error ")
        Help()
def Help():  
    os.system("clear")
    print("\x1b[1;93m")
    os.system("figlet MS-I")
    jalan("********** MS-Installer By Arfat_Khan **********\n\n")
    jalan("\n▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")    
    jalan("\x1b[1;96mAuthor : Arfat_Khan")
    jalan("Website : https://www.technicalak-bd.blogspot.com\n")
    jalan('Facebook : https://www.facebook.com/akbullethz0.2\n')
    jalan("Github : https://github.com/arfatkhanbd\n")
    jalan("\n▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
    jalan('\n\n\x1b[1;92m1.Help')
    jalan('2.How To Use This Tool')
    jalan('3.Unistall Metasploit' )
    jalan('4.My FB Account')
    jalan('5.My YouTube Channel')
    jalan('6.My Github Account ')
    jalan("7.My Website")
    jalan('8.Install Metasploit')
    jalan('9.Other Tool')
    jalan('10.Exit')
    jalan("\n▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
    sh2()
    a=int(input("localhost@ms-in_# "))
    if a==1:
        os.system("xdg-open https://technicalak-bd.blogspot.com/2020/04/blog-post_28.html")
        Help()
    elif a==2:
        os.system("xdg-open https://technicalak-bd.blogspot.com/2020/04/blog-post_28.html")
        Help()
    elif a==3:
        os.system("pkg uninstall metasploit")
        Help()
    elif a==4:
        os.system("xdg-open https://www.facebook.com/akbullethz0.2")
        Help()
    elif a==5:
        os.system("xdg-open https://www.youtube.com/channel/UC33rTm0ry9X2REsU9WsjgvA")
        Help()
    elif a==6:
        os.system("xdg-open https://www.github.com/arfatkhanbd")
        Help()
    elif a==7:
        os.system("xdg-open https://technicalak-bd.blogspot.com")
        Help()
    elif a==8:
        install()
    elif a==9:
        os.system("xdg-open https://technicalak-bd.blogspot.com/2020/04/FB-Sploit.html?m=1")
        Help()
    elif a==10:
        exit()
    elif a=="":
        Help()
    else :
        Help()
wlcm()
Help()
        