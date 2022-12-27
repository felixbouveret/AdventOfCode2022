import glob


class RockPaperScissors:
    score: int = 0
    strategy_guide: list[list[str]] = []

    loser_guide = {
        'X': 'B',  # Pierre / Feuille
        'Y': 'C',  # Feuille / Ciseaux
        'Z': 'A',  # Ciseaux / Pierre
    }
    winner_guide = {
        'X': 'C',  # Pierre / Ciseaux
        'Y': 'A',  # Feuille / Pierre
        'Z': 'B',  # Ciseaux / Feuille
    }
    shape_score_guide = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    round_score_guide = {
        'LOST': 0,
        'DRAW': 3,
        'WIN': 6
    }

    def __init__(self, inputPath: str):
        self.strategy_guide = self.formatInput(inputPath)

    def formatInput(self, inputPath: str) -> list[list[str]]:
        strategy = []
        for infile in glob.glob(inputPath):
            file = open(infile, 'r').read()
            for step in file.split('\n'):
                if step:
                    strategy.append(step.split(' '))
        return strategy

    def getGuide(self) -> list[list[str]]:
        return self.strategy_guide

    def getScore(self) -> int:
        return self.score

    def playRound(self, step: list[str]):
        elf_move = step[0]
        player_move = step[1]
        round_score = 0

        if self.winner_guide[player_move] == elf_move:
            round_score = self.round_score_guide['WIN']

        elif self.loser_guide[player_move] == elf_move:
            round_score = self.round_score_guide['LOST']

        else:
            round_score = self.round_score_guide['DRAW']
        round_score += self.shape_score_guide[player_move]
        self.score += round_score

    def playMultipleRounds(self):
        for step in self.strategy_guide:
            self.playRound(step)


rpcIntance = RockPaperScissors('./02/input')
rpcIntance.playMultipleRounds()
print(rpcIntance.getScore())
