import random as r

class Chromosome:
    """pass"""
    def __init__(self):
        self.start_layer = [[r.randint(1, 5) for i in range(13)] for j in range(13)]
        self.start_layer_corrections()
        self.second_layer = [[r.randint(1, 2) for i in range(21)] for j in range(13)]


    def show_second_layer(self):
        """pass"""
        for row in self.second_layer:
            for i in row:
                print(i, end=' ')
            print()


    def show_start_gene(self):
        """pass"""
        for row in self.start_layer:
            for i in row:
                print(i, end=' ')
            print()

    def start_layer_corrections(self):
        """pass"""
        for i in range(len(self.start_layer)):
            for j in range(len(self.start_layer[0])):
                if i != j and self.start_layer[i][j] == 5:
                    self.start_layer[i][j] = r.randint(1, 4)


