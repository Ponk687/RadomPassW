import random 

i_security = 12

speciaux = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126] #liste des chratceres speciaux en code ascii generalement accéptés en mdp


def randomMot():
    with open("francais.txt", "r", encoding="utf-8") as file :
        mots = [line.strip() for line in file]
        return random.choice(mots)

def generate(i_security = 10, Type = 'r'):
    mdp = ""
    if (Type == 'r'):
        while (len(mdp) < i_security):
            n = random.randint(0,3)
            if (n == 0):
                mdp = mdp + chr(random.randint(97,122))
            elif (n == 1):
                mdp = mdp + chr(random.randint(65,90))
            elif (n == 2):
                mdp = mdp + chr(random.randint(48,57))
            else:
                mdp = mdp + chr(random.choice(speciaux))

    elif (Type == 'p'):
        i = 0
        while(i < i_security): 
            mdp += randomMot()
            mdp += " "  
            i += 1

    return mdp

print(generate(i_security, 'p'))