import re
from Email import mail_list

emails = []

with open("tekstmails.txt", "r") as bestand:
    regel = bestand.readline()
    while regel:
        patroon = r"@" 
        gevonden = re.findall(patroon)
        regel = bestand.readline()
        
print(emails)
