import random

chiffre_mystere = random.randint(1, 101)

nombre_essais = 5

print("\033[92mBienvenue dans le jeu du nombre mystère !\033[0m")
print("\033[94mTu vas devoir deviner ce fameux nombre qui se trouve entre 1 et 100.\033[0m")

while nombre_essais > 0:
    pc = input("Quel est le nombre mystère d'après toi ? ")

    if pc == str(chiffre_mystere):
        print("BRAVO ! Tu as trouvé le nombre mystère.")
        break  # Sortir de la boucle si le bon nombre est trouvé

    nombre_essais -= 1

    if pc > str(chiffre_mystere):
        print(f"Le nombre mystère est plus petit que {pc}.")
    elif pc < str(chiffre_mystere):
        print(f"Le nombre mystère est plus grand que {pc}.")

    print(f"\033[91mIl te reste {nombre_essais} chance(s).\033[0m")

if nombre_essais == 0:
    print(f"Désolé, tu as épuisé toutes tes chances. Le nombre mystère était {chiffre_mystere}.")




