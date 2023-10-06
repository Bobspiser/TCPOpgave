from socket import *
from threading import *
import random
import json

serverPort = 9

def handleClient(clientSocket, addr):
    ask = f'Choose an option:\n 1. add [num] [num]\n 2. substract [num] [num] \n 3. random [num] [num]\n\n'

    clientSocket.send(ask.encode())

    while True:
        sentence = clientSocket.recv(2048).decode()
        #if not sentence:
            #break  # Afslut løkken, hvis der ikke er modtaget nogen besked fra klienten

        splitterText = sentence.split()
        Text = ""
        if splitterText[0].lower() == "add":
            talx = int(splitterText[1])
            taly = int(splitterText[2])
            #Text = f"{talx} + {taly} = {(talx + taly)}\n\n"

            dict = {   # Converter python objekt til en json string
                "tal1": talx, "tal2": taly, "Result": [talx + taly]  # Udfylder json string
            }

            y = json.dumps(dict)

        elif splitterText[0].lower() == "substract":
            talx = int(splitterText[1])
            taly = int(splitterText[2])
            #Text = f"{talx} - {taly} = {(talx - taly)}\n\n"

            dict = {
                "tal1": talx, "tal2": taly, "Result": [talx - taly]
            }

            y = json.dumps(dict)

        elif splitterText[0].lower() == "random":
            talx = int(splitterText[1])
            taly = int(splitterText[2])
            #Text = f" {random.randint(talx, taly)}\n\n"

            dict = {
                "tal1": talx, "tal2": taly, "Result": [random.randint(talx, taly)]
            }

            y = json.dumps(dict)

        else:
            y = f"understøtter ikke denne metoden {splitterText[0]}"
            
            y = json.dumps(dict)

            #Text = f"understøtter ikke metoden {splitterText[0]}\n\n"
    
        clientSocket.send(y.encode())

    clientSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is up and running on port", serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    print("forbundet til en Client fra adressen", addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()
