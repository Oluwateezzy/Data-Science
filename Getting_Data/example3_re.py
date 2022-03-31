import os

directory = 'c:/users/Teezzy/desktop/'
files = os.listdir(directory)

for f in files:
    if os.path.isfile(directory+f):
        print(f)