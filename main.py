sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    ask = input("Enter a word or Exit: ")
    if ask in sample_dict:
        print(sample_dict[ask])
    elif ask== "exit":
        break
    else:
        print ("try again")

print ("Bye")