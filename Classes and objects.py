# Питон это обьектно ориентированный язык программирования - парадигма основанная на представлении прогр в виде совокупн обьектов являющихся
class House():
    '''House revue'''
    def __init__(self, street, number):
        '''House optioms'''
        self.street = street
        self.number = number

    def build(self):
        '''Build a house'''
        print('House on street ' + self.street + 'on number ' + str(self.number) + ' alredy build.')
House1 = House('Kharkiv str ', 20)
House2 = House('Kharkiv str ', 21)

print(House1.street)

print(House1.build)
