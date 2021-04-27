# script hecho caundo estaba medio enfermo XD
# me gusta el pan
# se que existen mil herramientas similares
# pero es para practicar :)

import os
from requests import get


def banner():
    os.system("clear")
    print("""
    
██████   ██████  ██   ██     ██ ██████  
██   ██ ██    ██  ██ ██      ██ ██   ██ 
██   ██ ██    ██   ███       ██ ██████  
██   ██ ██    ██  ██ ██      ██ ██      
██████   ██████  ██   ██     ██ ██      
                                   

 *-----------------------*
 * Script para obtener   *
 * informacion de una ip *
 *                       *
 * Hecho por vulk4n0     *
 * Fecha: 26/04/2021     *
 *                       *
 * "tengo sueño xddd"    *
 *-----------------------*

  MENÚ:
 [1] Obtener Informacion de una IP
 [2] Informacion de mi IP
 [0] Salir
    
    """) 

def ob():
    ip = input("\n Introduce la IP: ")
    de = int(input("\n ¿Que dox quiere ver? \n 1) Dox basico\n 2) Dox completo\n Respuesta: "))
    if de == 1:
        print("")
        os.system(f"curl ipinfo.io/{ip}")
        print("")
        k = int(input(" ¿Desea realizar otra operación?\n 1)si\n 2)no\n Responde: "))
        if k == 1:
            os.system("python3 Dox_ip.py")
        else:
            os.system("clear")
            print("\n Gracias por utilizarme :D\n Hecho por vulk4n0")
            exit
    elif de == 2:
        print("")
        os.system(f"curl ipinfo.io/{ip}")
        print("")
        print("")
        os.system(f"whois {ip}")
        print("")
        k = int(input(" ¿Desea realizar otra operación?\n 1)si\n 2)no\n Responde: "))
        if k == 1:
            os.system("python3 Dox_ip.py")
        else:
            os.system("clear")
            print("\n Gracias por utilizarme :D\n Hecho por vulk4n0")
            exit

def yo():
    ip = get("https://api.ipify.org").text
    print(f"\n Tu IP actual es: ",ip)
    print("")
    de = int(input(" ¿Que dox quiere ver? \n 1) Dox basico\n 2) Dox completo\n Respuesta: "))
    if de == 1:
        print("")
        os.system(f"curl ipinfo.io/{ip}")
        print("")
        k = int(input(" ¿Desea realizar otra operación?\n 1)si\n 2)no\n Responde: "))
        if k == 1:
            os.system("python3 Dox_ip.py")
        else:
            os.system("clear")
            print("\n Gracias por utilizarme :D\n Hecho por vulk4n0")
            exit
    elif de == 2:
        print("")
        os.system(f"curl ipinfo.io/{ip}")
        print("")
        print("")
        os.system(f"whois {ip}")
        print("")
        k = int(input(" ¿Desea realizar otra operación?\n 1)si\n 2)no\n Responde: "))
        if k == 1:
            os.system("python3 Dox_ip.py")
        else:
            os.system("clear")
            print("\n Gracias por utilizarme :D\n Hecho por vulk4n0")
            exit

banner()
eleccion = int(input(" -¿Que opción elegiras?\n -Responde: "))
print("")
os.system("clear")

if eleccion == 1:
    ob()
elif eleccion == 2:
    yo()
else:
    exit


