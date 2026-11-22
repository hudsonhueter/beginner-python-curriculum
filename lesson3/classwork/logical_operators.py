age = int(input("How old are you?"))
has_ticket = input("Do you have a movie ticket? (yes/no)")

if age >= 13 and has_ticket == "yes":
    print("You can enter the PG-13 movie.")
else:
    print("Sorry, you can't enter.")

print ("Movie check complete.")

has_pass = input ("Do you have a bus pass? (yes/no) ")
has_coins = input ("Do you have coins? (yes/no) ")

if has_pass == "yes" or has_coins == "yes":
    print("You can ride the bus!")
else:
    print("You can't ride the bus.")

print ("Bus check complete.")

homework_done = input("Did you do your homework? (yes/no) ")

if not homework_done == "yes":
    print ("Go finish your homework!")
else:
    print("Nice job! You're all done.")

print("Homework check complete.")