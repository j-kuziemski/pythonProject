
import os
import msvcrt as m



def wait():
    m.getch()

os.system('cls')

ans=True
while ans:
    print("""
    Menu:
    ---------------
    
    1. Exponential-E
    2. NBI
    3. Exit
    """)
    ans=input("Choose Project: ")
    if ans=="1":
      print("\nExponential-E was chosen")
      ans=input("1. How many devices: ")
      print("\nPress Enter...")
      wait()
      os.system('cls')
      if ans == "1":
        ans = input("Name of device: ")
        wait()
        os.system('cls')
      elif ans == "2":
        ans = input("Name of 1st device: ")
        ans = input("Name of 2nd device: ")
        print("\nPress Enter...")
        wait()
        os.system('cls')
    elif ans=="2":
      print("\ntest2")
      print("\nPress Enter...")
      wait()
      os.system('cls')
    elif ans=="3":
      print("\nGoodbye")
      ans = None
    else:
      print("\nNot Valid Choice Try again")
      print("\nPress Enter...")
      wait()
      os.system('cls')
      ans = True
