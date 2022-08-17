#BY STUARTLIL- JONHYSTREET

def solve(s):
    #Obtienes una cadena en tu funcion separas tu cadena en vectores y capitalizas la primera letra lo almacenas todo en una nueva cadena
    cadena = ""
    s = s.split(sep=" ")
    for i in range(0,len(s)):
        cadena = cadena + s[i].capitalize() + " "
    print(cadena)

if __name__ == '__main__':
    s = input()
    print(solve(s))
