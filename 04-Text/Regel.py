import re

while True:
    phone = input("Voer je mobiele nummer in: ")
    patroon = '^06-?\d{8}$'
    matches = re.findall(patroon, phone)
    if(len(matches)>0):
        break
print(f"Bedankt nummer in juiste formaat. {matches[0]}")
