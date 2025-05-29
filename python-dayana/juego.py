import random
import os 

lista = ["pi","pa","ti"]

while True:
     os.system("cls")
     compu = random.choice(lista)
     yo = input("Elija piedra,papel o tijera: ")

print(f"compu: {compu}, yo: {yo}")
if compu == "pi" and yo == "ti": 
 print("Gano compu")
if compu == "pi" and yo == "pa": 
 print("Gano yo")
if compu == "pa" and yo == "pi": 
 print("Gano compu")
if compu == "pa" and yo == "ti": 
 print("Gano yo") 
if compu == "ti" and yo == "pa": 
 print("Gano compu")
if compu == "ti" and yo == "pi": 
 print("Gano yo")
if compu == "pa" and yo == "pa": 
 print("Empate")
if compu == "pi" and yo == "pi": 
 print("Empate")
if compu == "ti" and yo == "ti": 
 print("Empate")

input()