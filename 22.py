from aocd.models import Puzzle
from tqdm import tqdm
day22puzzle = Puzzle(year=2019, day=22)
inputs = day22puzzle.input_data


class Card():
    def __init__(self, cards, inputs):
        self.cards = cards
        self.inputs = inputs
        self.current_position = 0

    def deal_into_new_stack(self):
        self.cards = self.cards[-1::-1]

    def cut_n(self, n):
        new = self.cards.copy()[n::]
        new.extend(self.cards[0:n])
        self.cards = new

    def increment_n(self, n):
        new_cards = [None] * len(self.cards)
        start = 0
        for element in self.cards:
            new_cards[start] = element
            start = (start + n) % len(self.cards)
        self.cards = new_cards

    def parse_input(self, line):
        if line == "deal into new stack":
            return self.deal_into_new_stack()

        elif line.startswith("cut"):
            increment = int(line.split(" ")[-1])
            return self.cut_n(increment)


        elif line.startswith("deal"):
            increment = int(line.split(" ")[-1])
            return self.increment_n(increment)


    def run(self):
        instructions = inputs.split("\n")
        for line in tqdm(instructions):
            self.parse_input(line)

all_cards = []

for i in tqdm(range(119315717514047)):
    all_cards.append(i)

cards = Card(all_cards, inputs)
cards.run()

print(cards.cards.index(2019))
