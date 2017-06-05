from .models import *


def fight(player, opponent):
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
    print(pScore)
    if pScore > oScore:
        return 'Win'
    elif pScore < oScore:
        return 'Lose'
    else:
        return 'Tie'

def playRound():
    playerNo = players.objects.filter(played=False).count()
    allocation = []
    temp =0
    tempAllocation =[]
    i=0
    tempKey=None
    keys=[]
    tempPlayKeys=None
    playKeys=[]
    while i<playerNo:
        n=1
        tempAllocation=[]
        while n<=10:
            varAll = 'Allocations' + str(n)
            temp = players.objects.values_list(varAll, flat=True).filter(played=False)
            tempAllocation.append(temp[i])
            n+=1
        tempName = players.objects.values_list('pk', flat=True).filter(played=False)
        keys.append(tempName[i])
        allocation.append(tempAllocation)
        i+=1

    playerPlayed = players.objects.filter(played=True).count()
    i=0
    while i < playerPlayed:
        tempPlayKeys = players.objects.values_list('pk', flat=True).filter(played=True)
        playKeys.append(tempPlayKeys[i])
        i+=1

    loop=0

    while loop<playerNo:
        n=0
        while n<playerNo:
            if n!=loop:
                result = fight(allocation[loop], allocation[n])
                print(result)
                if result == 'Win':
                    player = players.objects.get(pk=keys[loop])
                    player.wins+=1
                    player.save()
                elif result == 'Lose':
                    player = players.objects.get(pk=keys[loop])
                    player.losses+=1
                    player.save()
                else:
                    player = players.objects.get(pk=keys[loop])
                    player.ties+=1
                    player.save()
            n+=1
        loop+=1
    playLoop=0
    while playLoop<playerNo:
        player = players.objects.get(pk=keys[playLoop])
        player.played=True
        player.save()
        playLoop+=1
    plays=len(playKeys)
    print(playKeys)
    playsLoop=0
    while playsLoop<plays:
        player = players.objects.get(pk=playKeys[playsLoop])

        player.display=True
        player.save()
        playsLoop+=1
