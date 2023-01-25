# Password-Generator
A password generator which generates a new password each time and adds it to a new line in a text file. Also checks for the same password in the file so will never create duplicate. 

# How to run:

- Download or clone git. 
- Open Command Prompt or Terminal and navigate to project folder
- Type 'python passwordgen-run.py' and press enter

### Example Usage:
```
pass = Password()
passValue = pass.generateKey()
print(passValue)
```
>>Emgvk-Zpbbt-vLH4W-PbN9j-GYNjb

### Customised Usage:
```
pass = Password(3,8,"--")
passValue = pass.generateKey()
print(passValue)
```
>>Emg--Zpb--vLH--PbN--GYN--bBt--6Sd--2bV
