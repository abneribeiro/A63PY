class party:
    x = 0

    def __init__(self):
        print('I am construred')

    def part(self):
        self.x = self.x + 1
        print('so far', self.x)

    def __del__(self):
        print('I am destrured', self.x)


an = party()
an.part()
an.part()

an = 42
print('im contains', an)