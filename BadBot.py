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
weirdcolors=["ultraviolet",
      "megagenta",
      "insaniteal",
      "mysterycolor",
      "gold",
      "confetti",
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
elif (ufav2 in weirdcolors):  
    print ("Remember! Reality is an illusion, the universe is a hologram, buy gold, bye!")
print ("End.")
