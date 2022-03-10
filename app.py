import random

print("Adivinhe o número que o Computador está pensando")
random_number = random.randint(0, 10)
user_number = int(input("Digite um número de 0 a 10: "))
print(random_number)
while user_number != random_number:
    if user_number > random_number:
        print(f"O número {user_number} está acima do número que pensei!")
        user_number = int(
            input(f"Digite outro número maior do que {user_number}: "))
    if user_number < random_number:
        print(f"O número {user_number} está abaixo do número que pensei!")
        user_number = int(
            input(f"Digite outro número menor do que {user_number}: "))
else:
    print("Você acertou!")
