print('\nLoti svarigi! Programma pienem tikai tekstus bez diakritiskam zimem!\n')

CODE = {'A': ')', 'a': '0', 'B': '(', 'b': '9', 'C': '*', 'c': '8','D': '&', 'd': '7', 'E': '^', 'e': '6', 'F': '%', 'f': '5','G': '$', 'g': '4', 'H': '#', 'h': '3', 'I': '@', 'i': '2','J': '!', 'j': '1', 'K': 'Z', 'k': 'z', 'L': 'Y', 'l': 'y','M': 'X', 'm': 'x', 'N': 'W', 'n': 'w', 'O': 'V', 'o': 'v','P': 'U', 'p': 'u', 'Q': 'T', 'q': 't', 'R': 'S', 'r': 's','S': 'R', 's': 'r', 'T': 'Q', 't': 'q', 'U': 'P', 'u': 'p','V': 'O', 'v': 'o', 'W': 'N', 'w': 'n', 'X': 'M', 'x': 'm','Y': 'L', 'y': 'l', 'Z': 'K', 'z': 'k', '!': 'J', '1': 'j','@': 'I', '2': 'i', '#': 'H', '3': 'h', '$': 'G', '4': 'g','%': 'F', '5': 'f', '^': 'E', '6': 'e', '&': 'D', '7': 'd','*': 'C', '8': 'c', '(': 'B', '9': 'b', ')': 'A', '0': 'a',':': ',', ',': ':', '?': '.', '.': '?', '<': '>', '>': '<',"'": '"', '"': "'", '+': '-', '-': '+', '=': ';', ';': '=','{': '[', '[': '{', '}': ']', ']': '}'}

def main():
    infile_1 = str(input('\nIevadiet Jusu faila nosaukumu:\n '))
    dtext = open(infile_1, 'r')
    dtext = dtext.readlines()

    encryptText(dtext)

    infile_2 = str(input('\nIevadiet Jusu sifreta faila nosaukumu: \n'))
    etext = open(infile_2, 'r')
    etext = etext.readlines()

    decryptText(etext)

def encryptText(dtext):
    outfile = str(input('\nIevadiet ka nosaukt sifreto failu:\n '))
    etext = open(outfile, 'w')
    for line in dtext:
        for c in line:
            encrypted = (CODE.get(c, c))
            etext.write(encrypted)
    etext.close()

def decryptText(etext):
  outfile_2 = str(input('\nIevadiet ka nosaukt atsifreto failu: \n'))
  detext = open(outfile_2,'w')
  for line in etext:
        for c in line:
            decrypted = (CODE.get(c, c))
            detext.write(decrypted)
  detext.close()

main()