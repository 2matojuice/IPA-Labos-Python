#Ex 3.1

directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "O": (-1, 0)}
position =()

def deplacer(position, ordre):
    if ordre not in directions: 
        return position
    new_position = []
    for i,j in range(min(len(position), len(ordre))):
        if type(position[i][j])==type(directions[ordre][i][j]):
                new_position.append(position[i][j]+directions[ordre][i][j])
                position = new_position  
    return tuple(position)

print(deplacer((2,3), "N"))

#Ex 3.2

def trajet(ordres, depart):
    return None