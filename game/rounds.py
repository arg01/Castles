# imports the player class
from .models import players
# class to handle each round
class rounds(object):
    #initations class with round details
    def __init__(self, playerNo, names, allocations):
        self.players=[]
        self.rounds=0
        self.winnerName=''
        self.playerNo = playerNo
        self.names = names
        self.allocations = allocations
    # setups array of all players int the round
    def setupPlayers(self):
        i=0
        while i<self.playerNo:
            self.players.append(player.player(self.names[i], self.allocations[i]))
            i+=1
    # puts p the player against o the opponent to work out score
    def fight(self, player, opponent):
        pScore = 0
        oScore = 0
        i=0
        value=0
        while i<10:
            army=player[i]
            opponentArmy=opponent[i]
            value+=1
            if army > opponentArmy:
                pScore+=value
            elif army < opponentArmy:
                oScore+=value
            else:
                pScore+=(value/2)
                oScore+=(value/2)
            i+=1
        if pScore > oScore:
            return 'Win'
        elif pScore < oScore:
            return 'Lose'
        else:
            return 'Tie'

    def playRound(self):
        i=0
        n=0
        while i<self.playerNo:
            while n<self.playerNo:
                if n!=i:
                    result = self.fight(self.players[i].allocations, self.players[n].allocations)
                    if result == 'Win':
                        self.players[i].increaseWins()
                    elif result == 'Lose':
                        self.players[i].increasesLosses()
                    else:
                        self.players[i].increaseTies()
                n+=1
            i+=1

    def winner(self):
        score=[]
        i=0
        while i<self.playerNo:
            score.append(self.players[i].getScore())
            i+=1
        person = score.index(max(score))
        self.winnerName = self.players[person].name
