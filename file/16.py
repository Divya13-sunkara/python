import os

if not os.path.exists("newfile.txt"):
    f = open("newfile.txt", "w")
    f.write("New file created")
    f.close()
else:
    print("File already exists")