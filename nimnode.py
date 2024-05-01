class NimNode:
    def __init__(self, piles, depth):
        self.piles = piles
        self.depth = depth
        self.children = []
        self.evaluate()

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def __str__(self):
        return ">\t" * self.depth + f"{self.piles}: Value = {self.value}"

    def __lt__(self, other):
        return self.value < other.value if isinstance(other, NimNode) else self.value < other

    def display(self):
        print(self)
        for child in self.children:
            child.display()

    def evaluate(self):
        possibilities = []
        for i, count in enumerate(self.piles):
            for num_removed in range(1, count + 1):
                new_piles = self.piles[:]
                new_piles[i] -= num_removed

                if sorted(new_piles) not in possibilities and new_piles != [0] * len(self.piles):
                    possibilities.append(sorted(new_piles))
                    child_node = NimNode(new_piles, self.depth + 1)
                    self.add_child(child_node)

        if not possibilities:
            self.value = -1 if self.depth % 2 == 0 else 1
        else:
            self.value = max(self.children).value if self.depth % 2 == 0 else min(self.children).value
