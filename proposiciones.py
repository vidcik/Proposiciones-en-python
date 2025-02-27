
import itertools
import re

def convertir_proposicion(proposicion):
    proposicion = proposicion.replace('¬', ' not ')
    proposicion = proposicion.replace('&', ' and ')
    proposicion = proposicion.replace('|', ' or ')
    proposicion = re.sub(r'(\w+)\s*->\s*(\w+)', r'implica(\1, \2)', proposicion)
    proposicion = proposicion.replace('<->', ' == ')
    return proposicion

def extraer_variables(proposicion):
    return sorted(set(re.findall(r'\b[a-z]\b', proposicion)))

def implica(p, q):
    return not p or q

def evaluar_proposiciones(prop1, prop2, variables):
    prop1_python = convertir_proposicion(prop1)
    prop2_python = convertir_proposicion(prop2)
    combinaciones = list(itertools.product([True, False], repeat=len(variables)))

    for combinacion in combinaciones:
        contexto = dict(zip(variables, combinacion))
        contexto['implica'] = implica

        resultado1 = eval(prop1_python, {}, contexto)
        resultado2 = eval(prop2_python, {}, contexto)

        if resultado1 != resultado2:
            return False

    return True

def son_equivalentes(proposicion1, proposicion2):
    variables = list(set(extraer_variables(proposicion1) + extraer_variables(proposicion2)))
    equivalentes = evaluar_proposiciones(proposicion1, proposicion2, variables)

    if equivalentes:
        print("Las proposiciones son equivalentes.")
    else:
        print("Las proposiciones no son equivalentes.")


proposicion1 = "p | (q & r)" #aqui se pone la primera proposicion
proposicion2 = "(p | q) & (p | r)" #aqui se pone la segunda proposicion
son_equivalentes(proposicion1, proposicion2)

