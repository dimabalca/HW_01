class Cinema:
    def __init__(self):
        self.name = input('ведите имя')
        self.rating = input('ведите rating')
    def printInfo(self):
        print(f'{self.name} {self.rating}')

cinemas = []
cinemas.append(Cinema())
cinemas.append(Cinema())
cinemas.append(Cinema())

for i in range(len(cinemas)):
    cinemas[i].printInfo()
