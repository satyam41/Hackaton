# import csv

# key = open("Keys.csv", 'w', newline=' ')
# keyWriter = csv.writer(key)
# keyWriter.writerow(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

# key_dict = {
#     'A':'@','B':'!','C':'#','D':'$','E':'%','F':'^','G':'--.','H':'!!','I':'$#','J':'!@','K':'&','L':'**','M':'@#','N':'//','O':'??','P':'||','Q':'%^','R':'+&','S':'...','T':'-','U':'..-','V':'...-','W':'^^','X':'%*&','Y':'*&^','Z':'**-/'
# }

# key = str(key_dict)
# value = str(key_dict.values())

keyList = []

text = input("Enter any text: ")

for i in text:
    if (text in 'A'):
        keyList.append(text.replace('A','-'))
        # newText = text.replace('A','@')
    elif (text in 'B'):
        keyList.append(text.replace('B','-...'))
    elif (text in 'C'):
        keyList.append(text.replace('C','-.-.'))
    elif (text in 'D'):
        keyList.append(text.replace('D','-..'))
    elif (text in 'E'):
        keyList.append(text.replace('E','.'))
    elif (text in 'F'):
        keyList.append(text.replace('F','..-.'))
    elif (text in 'G'):
        keyList.append(text.replace('G','--.'))
    elif (text in 'H'):
        keyList.append(text.replace('H','.....'))
    elif (text in 'I'):
        keyList.append(text.replace('I','..'))
    elif (text in 'J'):
        keyList.append(text.replace('J','.---'))
    elif (text in 'K'):
        keyList.append(text.replace('K','-.-'))
    elif (text in 'L'):
        keyList.append(text.replace('L','.-..'))
    elif (text in 'M'):
        keyList.append(text.replace('M','--'))
    elif (text in 'N'):
        keyList.append(text.replace('N','-.'))
    elif (text in 'O'):
        keyList.append(text.replace('O','---'))
    elif (text in 'P'):
        keyList.append(text.replace('P','.--.'))
    elif (text in 'Q'):
        keyList.append(text.replace('Q','--.-'))
    elif (text in 'R'):
        keyList.append(text.replace('R','.-.'))
    elif (text in 'S'):
        keyList.append(text.replace('S','...'))
    elif (text in 'T'):
        keyList.append(text.replace('T','-'))
    elif (text in 'U'):
        keyList.append(text.replace('U','..-'))
    elif (text in 'V'):
        keyList.append(text.replace('V','...-'))
    elif (text in 'W'):
        keyList.append(text.replace('W','.--'))
    elif (text in 'X'):
        keyList.append(text.replace('X','-..-'))
    elif (text in 'Y'):
        keyList.append(text.replace('Y','-.--'))
    elif (text in 'Z'):
        keyList.append(text.replace('Z','--..'))

newText = str(keyList)
# print(str(keyList))
print(newText)
