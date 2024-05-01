"""
TO DO
---------
###When player 2 starts it isn't random
###double inputs into progression
###begining simulations
"""
import random
class NimGame:
    def __init__(self, piles):
        self.piles = piles

    def make_move(self, pile_index, num_remove):#make sthe move, removing a stone from the pile
        if pile_index < 0 or pile_index >= len(self.piles) or num_remove <= 0 or num_remove > self.piles[pile_index]:
            return False  #invalid move
        self.piles[pile_index] -= num_remove
        return True  #successful move

    def get_valid_moves(self):#gets all valid moves for the minimax player
        valid_moves = []
        for i, count in enumerate(self.piles):
            for num_removed in range(1, count + 1):
                valid_moves.append((i, num_removed))
        return valid_moves

    def is_game_over(self):#checks to see if the game is over
        return all(p == 0 for p in self.piles)

    def winner(self):#returns winner
        return 'Player 1' if sum(self.piles) % 2 == 0 else 'Player 2'
    

def game(starting_piles, starting_player):
    game = NimGame(starting_piles)#creates a new game
    game_progression = [list(starting_piles)]#first part of progression will always be the first set of piles
    current_player = starting_player#set first player

    while not game.is_game_over():
        if current_player == 1:#player 1 follows minimax
            valid_moves = game.get_valid_moves()
            pile_index, num_remove = min(valid_moves, key=lambda move: move[1])
            game.make_move(pile_index, num_remove)
            #game_progression.append(list(game.piles))
        else:#player 2 is random
            possible_moves = []
            for i, count in enumerate(starting_piles):#gets the possible moves
                for num_removed in range(1, count + 1):
                    new_pile = starting_piles[:i] + [starting_piles[i] - num_removed] + starting_piles[i + 1:]
                    if any(objects != 0 for objects in new_pile):
                        possible_moves.append(new_pile)
            if possible_moves:
                starting_piles = random.choice(possible_moves)#choses randomly from possible moves
                game.piles = starting_piles
                #game_progression.append(list(starting_piles))
                
            
            else:
                break#no moves means game is over
        game_progression.append(list(game.piles))#progression for the output
        current_player = 3 - current_player  #alternate the players

    winner = game.winner()#winner of game
    return winner, game_progression

def simgames(num):
    results = {'Player 1': 0, 'Player 2': 0}
    for i in range(num//2):#since the loop does both player 1 and 2 we only need 50 loops
        starting_piles = [2, 2, 1]  # Using the starting position from part B
        winner, progression = game(starting_piles,1)#game start with 1
        for i in progression:#prints the progression and the winner of that round
            print(f'{i}>', end = '')
        print(f' winner: {winner}\n')
        results[winner] += 1#adds one to the respective winner's count
        
    for i in range(num//2):
        starting_piles = [2, 2, 1]
        winner, _ = game(starting_piles,2)#game start with 2
        results[winner] += 1#adds one to the respective winner's count
        for i in progression:#prints the progression and the winner of that round
            print(f'{i}>', end = '')
        print(f' winner: {winner}\n')

    print(f"Results after {num} games: Player 1 wins {results['Player 1']} games, Player 2 wins {results['Player 2']} games.")



def main():
    #code for the examples

    #code for the simulation
    simgames(100)

main()
