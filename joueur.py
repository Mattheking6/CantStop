import random


class Bot:
    def __init__(self, aggressivite: int):
        print("Ajout d'un bot")
        self.aggressivite = aggressivite
        encore = [True for _ in range(self.aggressivite)]
        stop = [False for _ in range(100 - self.aggressivite)]
        self.stop_encore = stop + encore

    def jouer(self, plateau: dict, options: list):
        print("Je réfléchis...")
        mon_choix = random.choice(options)
        if type(mon_choix) is int:
            mon_choix = [mon_choix]
        continuer = random.choice(self.stop_encore)
        return mon_choix, continuer
