import random

class Nim:
    def __init__(self, piles):
        self.piles = piles
        self.current_player = 0  # Player 0 is the one using minimax

    def get_legal_moves(self):
        moves = []
        for i, count in enumerate(self.piles):
            for remove in range(1, count + 1):
                moves.append((i, remove))
        return moves

    def make_move(self, move):
        pile_index, count = move
        self.piles[pile_index] -= count
        self.current_player = 1 - self.current_player

    def is_game_over(self):
        return all(count == 0 for count in self.piles)

    def get_winner(self):
        return 1 - self.current_player

def minimax(nim, depth, maximizing_player):
    if nim.is_game_over() or depth == 0:
        return 1 if maximizing_player else -1

    if maximizing_player:
        max_eval = float('-inf')
        for move in nim.get_legal_moves():
            nim.make_move(move)
            eval = minimax(nim, depth - 1, False)
            nim.make_move((move[0], -move[1]))  # Undo move
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in nim.get_legal_moves():
            nim.make_move(move)
            eval = minimax(nim, depth - 1, True)
            nim.make_move((move[0], -move[1]))  # Undo move
            min_eval = min(min_eval, eval)
        return min_eval

def minimax_player(nim, depth):
    best_eval = float('-inf')
    best_move = None
    for move in nim.get_legal_moves():
        nim.make_move(move)
        eval = minimax(nim, depth - 1, False)
        nim.make_move((move[0], -move[1]))  # Undo move
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def random_player(nim):
    return random.choice(nim.get_legal_moves())

def display_piles(piles):
    print("Current Piles:")
    for i, count in enumerate(piles):
        print(f"Pile {i + 1}: {'O ' * count}")

def play_nim():
    nim = Nim([2, 2, 1])  # Initial piles
    while not nim.is_game_over():
        display_piles(nim.piles)
        if nim.current_player == 0:
            move = minimax_player(nim, 3)  # Minimax player with depth 3
        else:
            move = random_player(nim)
        nim.make_move(move)
        print(f"Player {nim.current_player + 1} removes {move[1]} from pile {move[0]+1}")
    display_piles(nim.piles)
    
    winner = nim.get_winner()
    print(f"Player {winner + 1} wins!")

if __name__ == "__main__":
    play_nim()
