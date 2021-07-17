from colorama import Fore, Style
import os
import platform
import time
import requests

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

def logo():
    global logo
    dmr = Fore.CYAN + """
    ██╗     ███████╗    ██████╗  █████╗ ██╗  ████████╗ ██████╗ ███╗   ██╗
    ██║     ██╔════╝    ██╔══██╗██╔══██╗██║  ╚══██╔══╝██╔═══██╗████╗  ██║
    ██║     █████╗      ██║  ██║███████║██║     ██║   ██║   ██║██╔██╗ ██║
    ██║     ██╔══╝      ██║  ██║██╔══██║██║     ██║   ██║   ██║██║╚██╗██║
    ███████╗███████╗    ██████╔╝██║  ██║███████╗██║   ╚██████╔╝██║ ╚████║
    ╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝    ╚═════╝ ╚═╝  ╚═══╝                                                                
    """+Style.RESET_ALL
    sheesh = dmr + 23*"-" + " THE DIRECTORY SEARCHER "+ 23*"-"
    logo = sheesh + "\n     " + 25*"-" + " BY GUYEDIT#0990 "+ 23*"-"

def inputcolor(msg, param):
    global targeturl
    if param == 1:
        targeturl = input("\n"+Fore.MAGENTA+ f"[~] {msg}"+ Style.RESET_ALL)
    else:
        targeturl = input("\n"+Fore.MAGENTA+ f"[~] {msg}"+ Style.RESET_ALL)

def printcolor(msg, param):
    if param == 1:
        print("\n"+Fore.RED+ f"[-] {msg}"+ Style.RESET_ALL)
    else:
        print("\n"+Fore.GREEN+ f"[+] {msg}"+ Style.RESET_ALL)
        

def main():
    clear()
    print(logo)
    inputcolor("Target url: ", 2)
    nameofdico = input("\n"+Fore.MAGENTA+ f"[~] Name of bruteforce directory: "+ Style.RESET_ALL)
    timeout = float(input("\n"+Fore.MAGENTA+ f"[~] Timeout: "+ Style.RESET_ALL))
    
    if targeturl in "http" or "https":
        printcolor("BruteForce Directory is activate!", 2)
        time.sleep(2)
        clear()
        print(logo)
        bruteforce(targeturl, timeout, nameofdico)
        input()
    else:
        printcolor("Please specify a valid url !", 1)
        time.sleep(5)
        main()

def bruteforce(url, timeout, dico):
    f = open(dico, "r")
    for path in f:
        t1 = time.strftime("%A %d %B %Y %H:%M:%S")
        t2 = time.strftime("%A %d %B %Y")
        time.sleep(float(timeout))
        paths = "/"+path 
        mdrrrr = url + paths
        r = requests.get(mdrrrr)
        goodornote = int(r.status_code)
        if goodornote == 200:
            
            nicetruc = Fore.GREEN + f"[{t1}] | Code: {goodornote} on {mdrrrr}" + Style.RESET_ALL
            print(nicetruc)
            savelogs(f"[{t1}] | Code: {goodornote} on {mdrrrr}", t2)
        else:
            badtruc = Fore.RED + f"[{t1}] | Code: {goodornote} on {mdrrrr}" + Style.RESET_ALL
            print(badtruc)
            savelogs(f"[{t1}] | Code: {goodornote} on {mdrrrr}", t2)
    f.close()
    input()

def savelogs(log, path):
    name = path.replace(" ", "_") + ".txt"
    f = open(name, "a+")
    f.write(log)
    f.close()







if __name__ == "__main__":
    logo()
    main()
