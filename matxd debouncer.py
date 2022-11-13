import json
import threading
import shutil
from random import choice
from requests import get
import os
from pystyle import System , Colors

System.Size(140 , 40)
System.Title("Matxd Debouncer ~ V1.5 ~ @matxd291")

if os.path.exists("results") == True:
        shutil.rmtree("results")
else:
        pass

url = "https://messente.com/messente-api/number-lookup/?phone_number=%2B{}"

ascii = """

███╗   ███╗ █████╗ ████████╗██╗  ██╗██████╗     ██████╗ ███████╗██████╗  ██████╗ ██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ 
████╗ ████║██╔══██╗╚══██╔══╝╚██╗██╔╝██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗
██╔████╔██║███████║   ██║    ╚███╔╝ ██║  ██║    ██║  ██║█████╗  ██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║   ██║    ██╔██╗ ██║  ██║    ██║  ██║██╔══╝  ██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║   ██║   ██╔╝ ██╗██████╔╝    ██████╔╝███████╗██████╔╝╚██████╔╝╚██████╔╝██║ ╚████║╚██████╗███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝
"""

with open("config.json" , 'r') as f:
    content = f.read()

x = json.loads(content)

thread = x["Threads"]

print(ascii.replace('█', Colors.red+"█"+Colors.reset))

def Debouncer():

        while True : 

            t = "+336"+"".join(choice("0123456789") for y in range(8))
            r = get(url.format(t))
            
            z = r.json()

            Fournisseur = z["originalCarrierName"].replace("*", "").replace("[", "").replace("]", "").replace(",", "").replace(";", "").replace("(", "").replace(")", "")
            Pays = z["countryName"]
            timezone = z["timeZone"]

            os.makedirs("Results/" + Pays , exist_ok=True)

            if Fournisseur == "":
                print(f"[{Colors.red}-{Colors.reset}] {t} | Invalid")
            else : 

                print(f"[{Colors.light_green}+{Colors.reset}] {t} | Pays : {Pays} | Opérateur : {Fournisseur} | Timezone : {timezone}")
                with open("Results/" + Pays + f"/{Fournisseur}.txt" , 'a+') as file : 
                    file.write(t + '\n')
                    file.close()


for b in range(thread) :
    th = threading.Thread(target=Debouncer)
    th.start()
