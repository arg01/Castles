from django.shortcuts import render, redirect
from .models import players
from django.views import generic
from .forms import playersForm
from django.http import HttpResponseRedirect

def index(request):
    num_plays=players.objects.all().count()

    return render(
        request,
        'index.html',
    )

class ResultsView(generic.ListView):
    model = players

def play(request):
    if request.method == "POST":
        form = playersForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('results')
    else:
        form = playersForm()
    return render(request, 'game/play.html', {'form':form})

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

    if pScore > oScore:
        return 'Win'
    elif pScore < oScore:
        return 'Lose'
    else:
        return 'Tie'




def run_script(request):
    playerNo = players.objects.filter(played=False).count()
    allocation = []
    temp =0
    tempAllocation =[]
    i=0
    tempKey=None
    keys=[]

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
    

    loop=0

    while loop<playerNo:
        n=0
        while n<playerNo:
            if n!=loop:
                result = fight(allocation[loop], allocation[n])
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
        print(loop)
        loop+=1
    return HttpResponseRedirect('/game/results')
