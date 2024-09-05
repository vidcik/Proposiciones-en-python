# Proposiciones-en-python
Codigo en python que te dice si las proposiciones que ingresaste son equivalentes o no con ejemplos 

# Proposiciones Equivalentes:

proposicion1 = "p -> q"
proposicion2 = "¬p | q"
##############################

proposicion1 = "p <-> q"
proposicion2 = "(p -> q) & (q -> p)"
##################################

proposicion1 = "¬(p | q)"
proposicion2 = "¬p & ¬q"
################################

proposicion1 = "¬(p & q)"
proposicion2 = "¬p | ¬q"
################################

proposicion1 = "p | (q & r)"
proposicion2 = "(p | q) & (p | r)"


#Proposiciones no Equivalentes:

proposicion1 = "p & (q | r)"
proposicion2 = "(p & q) | (p & r)"
############################

proposicion1 = "p & q"
proposicion2 = "p | q"
##########################

proposicion1 = "p -> q"
proposicion2 = "q -> p"
############################

proposicion1 = "p | ¬p"
proposicion2 = "q & ¬q"
###########################

proposicion1 = "p -> (q & r)"
proposicion2 = "(p -> q) & (p -> r)"
