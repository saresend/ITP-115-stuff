#Samuel Resendez
#ITP 115
#Assignment 2
#September 11th, 2016
#Description:
#This program simulates a wizardly vending machine


# ---------------- begin implementation ---------------------- #
prices = { "a" : 58, "b" : 10,"c" : 7,"d" : 400 }
items = {"a":"Butterber","b":"Quill","c":"The Daily Prophet","d":"Book of Spells" } 
print("Please select an item from the vending machine: ")
print("a) Butterbeer: 58 knuts")
print("b) Quill: 10 knuts")
print("c) The Daily Prophet: 7 knuts")
print("d) Book of Spells: 400 knuts")
selection = input(">>")
while(selection.lower() != "a" and selection.lower() != "b" and selection.lower() !="c" and selection.lower() != "d"):
    print("Please select an item: ")
    selection = input(">>")
print("Excellent. Will you be sharing your purchase on instagram for a 5 knut discount?(y/n): ")
instagram = input(">>")
while(instagram.lower() != "y" and instagram.lower() != "n"):
    instagram = input("Please enter y or n: ")
galleonCount = input("Please enter number of galleons: ")
sickleCount = input("Please enter number of sickles: ")
knutCount = input("Please enter number of sickles: ")
discount = 0
totalKnuts = int(galleonCount)*493 + int(sickleCount)*29 + int(knutCount)

if instagram == "y" :
    discount = 5
change = totalKnuts - prices[selection] + discount
numberOfGalleons = change // 493
numberOfSickles = (change % 493) // 29
numberOfKnuts = change - (493 * numberOfGalleons) - (29 * numberOfSickles)
print("You bought a",items[selection],"for",prices[selection],"knuts (with a coupon of",discount,"knuts) and paid with",numberOfGalleons,"galleons,",numberOfSickles,"sickles, and",numberOfKnuts,"knuts.") 
print("Here is your change: ")
print("Galleons:",numberOfGalleons)
print("Sickles:",numberOfSickles)
print("numberOfKnuts:",numberOfKnuts)
