# toFile = open("CodeWars.com Practice\Files\File2.txt", "w")
# toFile.write("Hello Felix")
# toFile.close()
# toFile = open("CodeWars.com Practice\Files\File2.txt", "r")
# print(toFile.read())
# toFile.close()

with open("CodeWars.com Practice\Files\File3.txt", "w") as f:
    f.write('World!')

with open("CodeWars.com Practice\Files\File3.txt", "r") as f:
    a = f.read()
    print(a)
