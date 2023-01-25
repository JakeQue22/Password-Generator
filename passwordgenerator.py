import random

class Password:
    partLength = 0 #The length of each part, Defaults to 5
    partAmount = 0 #The amount of parts, Defaults to 5
    divider = '' #The string that divides parts, Defaults to "-"

    def __init__(
        self,pLength=5,pAmount=5,div='-'): #Set values
        self.partLength = pLength
        self.partAmount = pAmount
        self.divider = div

    def generateKey(self):
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" #Example character set, can be changed
        key = "" #Key to return
        
        for part in range(self.partAmount): #Loops partAmount times
            for onePart in range(self.partLength): #Loops partLength times
                key += random.choice(characters) #Adds random character from the characters string to key

            if (part != self.partAmount-1): #If it isnt the last part
                key += self.divider #Add a divider to the key
        return key

"""
Example Usage:
key = Password()
keyValue = key.generateKey()
print(keyValue)
>>EmgvkZpbbtvLH4W
Customised Usage:
key = Password(3,8,"-")
keyValue = key.generateKey()
print(keyValue)
>>Emg-Zpb-vLH-PbN-GYN-bBt-6Sd-2bV
"""