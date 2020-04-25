from random import randrange


def lancer_de():
    lancer_des = [randrange(1, 7) for x in range(4)]
    possibilite = {1: (lancer_des[0]+lancer_des[1], lancer_des[2]+lancer_des[3]),
             2: (lancer_des[0]+lancer_des[2], lancer_des[1]+lancer_des[3]),
             3: (lancer_des[0]+lancer_des[3], lancer_des[2]+lancer_des[1])
             }
    return lancer_des, possibilite