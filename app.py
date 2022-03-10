import random

print("Adivinhe o número que o Computador está pensando")
random_number = random.randint(0, 10)
user_number = int(input("Digite um número de 0 a 10: "))

if user_number < 0 or user_number > 10:
    user_number = int(
        input("Esse número é inválido por favor informe um número de 0 a 10: "))

guesses = 1

while user_number != random_number:
    if user_number > random_number:
        print(f"O número {user_number} é maior do que o número que pensei!")
        user_number = int(
            input(f"Digite outro número menor do que {user_number}: "))
        guesses += 1
    if user_number < random_number:
        print(f"O número {user_number} é menor do que o número que pensei!")
        user_number = int(
            input(f"Digite outro número maior do que {user_number}: "))
        guesses += 1
else:
    print(f"Parabéns, eu tinha pensado no número {random_number}.")
    if guesses == 1:
        print(
            f"Você leu minha mente! Acertou de primeira com {user_number} tentativas")
    if guesses < 3:
        print(
            f"Você está com muita sorte hoje! Acertou com {user_number} tentativas")
    if guesses < 5:
        print(f"Que rápido, acertou com {user_number} tentativas!")
