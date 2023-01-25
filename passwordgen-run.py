from passwordgenerator import Password

file_path = "generated-passwords.txt"
passwd = Password(15,1)
PassValue = passwd.generateKey()

name = input ("What would you like to generate a password for?")
if PassValue in file_path:
	PassValue = passwd.generateKey()
	print(PassValue)
else:
	print(PassValue)

if name == "":
	with open(file_path, 'a') as file:
		file.write(PassValue + " - " + "BYPASSED" + "\n")
else:
    with open(file_path, 'a') as file:
    	file.write(PassValue + " - " + name.capitalize() + "\n")