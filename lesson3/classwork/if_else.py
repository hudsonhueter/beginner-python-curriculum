age = int(input("How old are you? "))

if age >= 18:
    print ("You can vote!")
    print ("Congratulations!")

print("vote check complete!")
# if/else: choose one of two paths
temp = int(input("What's the temperature outside?"))

if temp < 10:
    print(It's cold, wear a jacket.)
else:
    print(no jacket needed!)
print (weather check complete!)

# if/elif/else: handle multiple cases
score = int(input(What's your score out of 100?"))
if score >= 90:
    print ("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
elif score >= 60
    print ("D")
else: 
    print ("F")

print ("Grading complete.")