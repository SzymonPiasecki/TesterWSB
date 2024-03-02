import os


with open ('./my_file.txt', 'r') as plik1:
    zmienalines = plik1.read()

zmienalines = zmienalines.split()

for i in zmienalines:
    print(i)
    
