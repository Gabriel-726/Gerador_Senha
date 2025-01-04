import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas python!")
nr_letters= int(input("Quantas letras você deseja na sua senha?\n")) 
nr_symbols = int(input(f"Quantos símbolos você deseja na sua senha?\n"))
nr_numbers = int(input(f"Quantos números você deseja na sua senha?\n"))


#Segue sequência letras, símbolos e números.

password = ""

#Loop de letras, com escolha random de letra.
for letras in range(1, nr_letters + 1):
    letras_ran = random.choice(letters)
    password = password + letras_ran

#Loop de simbolos, com escolha random de simbolos. 
for simbolo in range(1, nr_symbols + 1):
    simbolo_ran = random.choice(symbols)
    password = password + simbolo_ran
    
#Loop de números, com escolha random de números. 
for numero in range(1, nr_numbers + 1):
    numero_ran = random.choice(numbers)
    password = password + numero_ran
 
#Embaralha a sequência da senha
    
#transformamos a var password em uma lista(password_list)   
password_list = list(password)

#com o comando "random.shuffle" a lista embaralha todos os caracteres
random.shuffle(password_list)

#var password random
password_ran = ""

#para cada item na password_list nós os passamos para uma var (password_ran) tipo str
for item in password_list:
   password_ran += item

print(password)
print(password_ran)

    

    
    

    

    

