#myDict = {}
myDict = {"Indepensable":"Absolutely necessary", "Present":["Existing or occuring now","A gift"]}

addWords = True

while addWords == True:
    print("Would you like to add a word to your dictionary? (y/n)")
    answer = input().lower()
    if(answer == 'y'):
        print("Okay, what's the word?")
        word = input().lower()
        print("What's the definition?")
        definition = input().lower()

        myDict[word] = definition
    elif(answer == 'n'):
        print("Your dictionary entry has been saved!")
        addWords = False
    else:
        print("Please enter 'y' or 'n'")

#print(myDict)
print("MY DICTIONARY:")
print()
for item in myDict:
    print("Word:" + item)
    definition = myDict[item]
    defineType = type(definition)
    if (defineType == str):
        print("Definition:" + myDict[item])
    elif (defineType == list):
        for x in definition:
            print ("-" + x)
        print()
