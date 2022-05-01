
class GameField:
    avgGameDur = 0
    firstPlayerW = 0
    secondPlayerW = 0


class Node:
    number = 0
    ways = []

    def __init__(self):
        pass

    def __init__(self, number, ways):
        self.number = number
        self.ways = ways
field = []


class Player:
    currentNode = Node()
    def __init__(self):
        pass


def start_game():
    field = GameField()


start_game()
