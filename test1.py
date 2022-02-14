import random
import os
import time
def clear():
        os.system('cls')

def facile():
    trousseau = 0
    while True:
        choix = int(input("\nChoisissez votre jarre : (1-5) "))
        
        serpent = random.randint(1,5)

        if choix == serpent :
            print("\nPiège")
            trousseau -= 1
            time.sleep(1)
            clear()
        elif choix > 5 :
            print("\nIl y en a que 5 jarres !\n")
            time.sleep(1)
            clear()
            continue
        else:
            print("\nGagné")
            trousseau += 1
            time.sleep(1)
            clear()
            
        if trousseau == 3:
            print("Tu deviens roi du temple")
            break
        elif trousseau == -1:
            print("Game Over")
            break
            
def normal():
    trousseau = 0
    while True:
        choix = int(input("\nChoisissez votre jarre : (1-5) "))
        
        serpent = random.randint(1,5)
        serpent2 = random.randint(1,5)

        if choix == serpent or choix == serpent2:
            print("\nPiège")
            trousseau -= 1
            time.sleep(1)
            clear()
        elif choix > 5 :
            print("\nIl y en a que 5 jarres !\n")
            time.sleep(1)
            clear()
            continue
        else:
            print("\nGagné")
            trousseau += 1
            time.sleep(1)
            clear()
            
        if trousseau == 3:
            print("Tu deviens roi du temple")
            break
        elif trousseau == -1:
            print("Game Over")
            break
    
def difficile() :
    trousseau = 0
    while True:
        choix = int(input("\nChoisissez votre jarre : (1-5) "))

        serpent = random.randint(1,5)
        serpent2 = random.randint(1,5)
        serpent3 = random.randint(1,5)
        serpent4 = random.randint(1,5)

        if choix == serpent or choix == serpent2 or choix == serpent3 or choix == serpent4:
            print("\nPiège")
            trousseau -= 1
            time.sleep(1)
            clear()
        elif choix > 5 :
            print("\nIl y en a que 5 jarres !\n")
            time.sleep(1)
            clear()
            continue
        else:
            print("\nGagné")
            trousseau += 1
            time.sleep(1)
            clear()
            
        if trousseau == 3:
            print("Tu deviens roi du temple")
            break
        elif trousseau == -1:
            print("Game Over")
            break

print("Bienvenue dans le jeux de jarres !")

print("\nVous avez 5 jarres devant vous et vous devez faire attention car dans l'un d'entre eux contient un serpent\n")


if __name__ == '__main__':
    # The GAME LOOP
    while True:
 
        # The Game Menu
        print()
        print("Let's Play!!!")
        print("Choisissez le niveau")
        print("1 Facile")
        print("2 Normal")
        print("3 Difficile")
        print("4 Exit")
        print()
 
        # Try block to handle the player choice 
        try:
            choice = int(input("Choisissez le niveau : "))
        except ValueError:
            clear()
            print("Mauvais choix Choice")   
            continue
 
        if choice == 1:
            facile()
 
        elif choice == 2:
            normal()
    
        elif choice == 3:
            difficile()
        elif choice == 4:
            break    
        
        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")