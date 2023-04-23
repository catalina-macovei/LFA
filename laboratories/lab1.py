# cititi de la stdin/fisier linie cu linie si de afisat

def reading_data_set(f):            # citesc datele din fisierul f
    d = {}                          # voi stoca datele intr-un dictionar unde key = nume_sectiune, value = valorile_sec
    lista = []
    aux = True                      # o var bool prin care se identifica cheia dictionarului
    f = open(f)
    for l in f:                     # acest for trece prin fiecare linie a dict
        linie = l.rstrip("\n : ,")
        if '#' not in linie and linie != '':        # astfel voi ignora comentariile si liniile goale
            if linie != 'End':
                if aux:
                    keydict = linie
                    aux = False     # false daca deja am o cheie setata
                if linie != keydict:
                    lista.append(linie)
            elif linie == 'End':
                aux = True          # din nou true pentru a stoca valorile unei noi sectiuni
                d[keydict] = lista
                lista = []
    f.close()

    for i in range(len(d['Transitions'])):
        d['Transitions'][i] = tuple(d['Transitions'][i].split(", "))  # sectiunea de tranzitii va fi o lista de tupluri

    states = [d['States']]
    for i in range(len(d['States'])):
       if d['States'][i] == 'S' or d['States'][i] == 'F':
           states.append(d['States'][i - 1])

    d['States'] = states
    return d


def validation_Sigma(d):
    for i in d['Sigma']:
        if i not in ('0', '1'):
            print(f"Sigma NULL at {i}")
            return 0
    return 1


# validation states:
# states  can  be  succeeded  by  ”F”,  ”S”,  both  or  nothing
#  ”S”  symbol  can succeed only one state.
def validation_states(d):
    states = d['States'][0]
    count = states.count('S')
    if count > 1:
        print("States NULL: Too many S points in states")
        return 0
    elif count == 1:
        i = states.index('S')
        if 'F' not in states[i:]:
            print("States NULL: States  can  be  succeeded  by  ”F”,  ”S”,  both  or  nothing")
            return 0
    elif count < 1:
        if "F" in states:
            print("States NULL: States  can  be  succeeded  by  ”F”,  ”S”,  both  or  nothing")
            return 0
    return 1


# validation transitions:
def validation_transitions(d):
    transitions = d['Transitions']

    for transition in transitions:
        if transition[0] not in d['States'][0] or transition[2] not in d['States'][0]:
            print('Transitions NULL: can\'t find the transition in States')
            return 0
        if transition[1] not in d['Sigma']:
            print(f'Transitions NULL: invalid transition {transition[1]}')
            return 0

    return 1

# validation for nfa --- SIGMA {0, 1, e(epsilon)}
# States - The same like DFA
# Transitions - a list of simbols between 2 states
