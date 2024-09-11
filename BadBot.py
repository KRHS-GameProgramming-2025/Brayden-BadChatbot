name=input("Enter name.")
greeting="Hello,"
print(greeting + " " + name + ".")
soccer=["Soccer",
      "soccer"]
tennis=["Tennis", 
      "tennis"]
sports=["football", 
      "soccer",
      "tennis",
      "basketball",
      "baseball",
      "badminton",
      "cricket"
      "golf"
      "table tennis"
      "hockey"
      "ice hockey"
      "bowling"]
colors=["red", 
      "orange",
      "yellow",
      "green",
      "blue",
      "purple",
      "magenta",
      "turquoise"]
weirdwords=["ultraviolet",
      "megagenta",
      "insaniteal",
      "mysterycolor",
      "buygold",
      "bill",
      "Bill",
      "cipher",
      "Cipher",
      "BillCipher",
      "billcipher",
      "Bill Cipher",
      "bill cipher",
      "brown 2"]
ufav=input("What's your favorite sport?")
if (ufav in colors):  
    print ("Colors aren't sports.")
elif (ufav in soccer):  
    print ("Soccer is my favorite too!")
elif (ufav in tennis):  
    print ("Tennis is pretty cool!")
else: 
    print (ufav + " " + "is alright, but I like soccer better!")
ufav2=input("What's your favorite color?")
if (ufav2 in sports):  
    print ("Sports aren't colors.")
elif (ufav2 in colors):  
    print ("That's cool, I like all colors!")
elif (ufav2 in weirdwords):  
    print ("HA   HA    HA " *1000000)
    print (" " *10000)
    print ("Remember! Reality is an illusion, the universe is a hologram, buy gold, bye!")
    print ("End.")
