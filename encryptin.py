import random  #importing library for using in the program 

"""
    @author: Shilpi, Simran, Ritika, Satyam
    @version: 1.0
    @since: 2022
    @see 
"""

num = random.random()  #initilizing the num variable and store random number less than 1.

def encrypt(sttr, enkey=str(num)):  #define the encrypt fuction for convert any plain text to cipher text
    return enkey.join(sttr)
try:
    text = input("Enter any text: ")

    #cipher text create a new file Encrypt.txt and all cipher text store at that file.
    with open("Encrypt.txt", 'a') as f:
        f.write(encrypt(text))
        f.write("\n")

except ValueError:
    pass