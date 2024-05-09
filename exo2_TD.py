import random

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def adjacentes(self, jeu):
        adjacent_cases = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                adjacent_x = self.x + dx
                adjacent_y = self.y + dy
                if 0 <= adjacent_x < len(jeu.listeDesCases) and 0 <= adjacent_y < len(jeu.listeDesCases[0]):
                    adjacent_cases.append(jeu.listeDesCases[adjacent_x][adjacent_y])
        return adjacent_cases

class Creature:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
    
    def __str__(self):
        return f"Creature {self.nom} at {self.position}"

    def choisirCible(self, jeu):
        adjacent_cases = self.position.adjacentes(jeu)
        cases_occupees = [case for case in adjacent_cases if jeu.estOccupee(case)]
        if cases_occupees:
            return random.choice(cases_occupees)
        else:
            return random.choice(adjacent_cases)

class Jeu:
    def __init__(self, taille_x, taille_y, creatures):
        self.listeDesCases = [[Case(x, y) for y in range(taille_y)] for x in range(taille_x)]
        self.listeDesCreatures = creatures
        self.tour = 1
        self.actif = self.listeDesCreatures[0]

    def __str__(self):
        return f"Tour {self.tour}, Active: {self.actif}\n"

    def estOccupee(self, case):
        for creature in self.listeDesCreatures:
            if creature.position == case:
                return True
        return False

    def deplacer(self, creature, nouvelle_position):
        if nouvelle_position in creature.position.adjacentes(self) and not self.estOccupee(nouvelle_position):
            creature.position = nouvelle_position
            for autre_creature in self.listeDesCreatures:
                if autre_creature.position == nouvelle_position:
                    print(f"{autre_creature.nom} a été capturée par {creature.nom}!")
                    return True
            self.tour += 1
            self.actif = self.listeDesCreatures[self.tour % len(self.listeDesCreatures)]
        return False

#6
creature1 = Creature("Creature1", Case(0, 0))
creature2 = Creature("Creature2", Case(3, 3))
creatures = [creature1, creature2] 
jeu = Jeu(4, 4, creatures)
#7

while True:
    print(jeu)
    creature_active = jeu.actif
    nouvelle_position = creature_active.choisirCible(jeu)
    if jeu.deplacer(creature_active, nouvelle_position):
        print(f"{creature_active.nom} a gagné!")
        break
