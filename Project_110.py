import random;

response = input("Roll a dice ('y' for yes and 'N' for no) ")
number = random.randint(1,6)  
  
if response == "N": 
        print("no")

elif response == "Y":
        if number == 1:
                print("- -")
                print(" 0 ")
                print("- -")
                print("1")
        if number == 2:
                print("- -")
                print("0 0")
                print("- -")
                print("2")
        
        if number == 3:
                print("- 0")
                print("- 0")
                print("- 0")
                print("3")
        
        if number == 4:
                print("0 0")
                print("0 0")
                print("- -")
                print("4")
        if number == 5:
                print("0 0")
                print(" 0 ")
                print("0 0")
                print("5")
        if number == 6:
                print("0 0")
                print("0 0")
                print("0 0")
                print("6")
        # print(number)Y





   
