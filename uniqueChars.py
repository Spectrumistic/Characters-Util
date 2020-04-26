
promt_input = input("Type file name in working directory: ")
f = None

try:
    f = open(promt_input, "r")
    print("File opened successfuly \n")
    
except:
    print("Could not open file, exiting...")
    exit(-1)

macaroni = f.read()

print("-----------------------RESULTS-----------------------")
print("Total length in characters: ", len(macaroni), "\n")
seenChars = []
macaroniCopy = macaroni

def is_unseen(character, characterList):
    for char in characterList:
        if char == character:
            return False
    return True

seen = 0
for char in macaroni:
    if is_unseen(char, seenChars):
        seenChars.append(char)
        seen = seen + 1

print("Unique characters: ", seen)