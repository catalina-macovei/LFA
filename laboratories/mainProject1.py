# Here I'll call the functions:
from lab1 import *
d = reading_data_set("lab1.in")

validation_Sigma(d)
validation_states(d)
validation_transitions(d)
dfa = reading_data_set("lab1date2.in")

def emulate_dfa(dfa, input_str):
    if validation_Sigma(dfa) and validation_states(dfa) and validation_transitions(dfa) and d['States'][2] == dfa['States'][2]:
        reveresed_str = input_str[::-1]
        if reveresed_str[0] == "0" and reveresed_str[1] == "0" and reveresed_str[2] == "1":
            print("Pass!")
        else:
            print("Reject!")
    else:
        print("Validation rejected!")


emulate_dfa(dfa, '0000100100')

print(d)
def emulate_nfa(nfa, input_str):
    n = len(input_str)
    i = 0
    if validation_Sigma(dfa) and validation_states(dfa) and validation_transitions(dfa) and d['States'][2] == dfa['States'][2]:
        print("nfa:passed the validation")
        reversed_str = input_str[::-1]
        lista = [0]
        for simbol in input_str:
            print(f"simbol={simbol}")
            for trans in d['Transitions']:
                if simbol == trans[1]:
                    print(f"trans[1]={trans[1]}")
                    if trans[2] != lista[i]:
                        lista.append(trans[2])
                        i += 1
                        print(i)
    if lista[len(lista) - 2] == d['States'][2]:
        print('nfa: passed!')
    else:
        print(lista)
        print('nfa: rejected!')


nfa = reading_data_set("dateinNFA.in")
print(nfa)
emulate_nfa(nfa, '001000')
