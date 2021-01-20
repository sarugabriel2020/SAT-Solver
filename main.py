def rezolva(fnc):
    # Cream lista de literali numita literals
    literals = []
    for i in range(len(fnc)):
        clauza = fnc[i].replace('~', '').split('V')
        # Avem o lista de literali
        for j in range(len(clauza)):
            literals.append(clauza[j])

    literals = list(set(literals))  # Stergem duplicarile
    # Crearea matricea
    matrice = []
    for i in range(len(fnc)):
        matrice.append([])
        for j in range(len(literals)):
            matrice[i].append(0)

    for i in range(len(fnc)):
        clauza = fnc[i].split('V')  # Despartim dupa V formula

        for j in range(len(clauza)):
            if '~' in clauza[j]:  # Daca gasim ~ in clauza , eliminam
                clauza[j] = clauza[j].replace('~', '')
                matrice[i][literals.index(clauza[j])] = -1

            # Ne uitam prin pozitia variabilei actuale in lista de literali
            # pentru a o pune pe coloana respectiva

            else:  # Daca nu avem negat
                matrice[i][literals.index(clauza[j])] = 1

    # Mergem prin indicii listei de iterari

    iterari = iterare(len(literals), ['0', '1'])
    for it in range(len(iterari)):
        interpretare = True

        for i in range(len(matrice)):
            clauza = False  # Asumam faptul ca acea clauza este falsa

            for j in range(len(matrice[i])):

                if (matrice[i][j] == 1 and iterari[it][j] == '1') \
                        or (matrice[i][j] == -1 and iterari[it][j] == '0'):
                    # In acest moment, am gasit un element True intr-o
                    # clauza deci toata clauza e True
                    clauza = True
                    break

            if clauza == False:
                # Daca o clauza dintr o expresie e Falsa
                # atunci toata interpretarea e Falsa
                interpretare = False
                break

        if interpretare == True:
            print(1)
            return

        if interpretare == False and it == len(iterari) - 1:
            print(0)
            return

"""

def iterare - realizeaza cautarea exhaustiva 
              pe toate interpretarile posibile
"""

def iterare(nr_element, literals):
    if nr_element == 1:
        return literals
    else:
        return [y + x
                for y in iterare(1, literals)
                for x in iterare(nr_element - 1, literals)
                ]

def sat_solver_algorithm():
    input_fnc = input()
    # Punem in cnf liniile citite din input
    fnc = input_fnc.replace('(', '').replace(')', '').split('^')
    rezolva(fnc)

if __name__ == '__main__':
    sat_solver_algorithm()

