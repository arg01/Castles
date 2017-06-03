from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from .forms import playersForm
from django.http import HttpResponseRedirect
import django_tables2 as tables

def index(request):
    num_plays=players.objects.all().count()

    return render(
        request,
        'index.html',
    )

class ResultsView(tables.Table):
    class Meta:
        model = players

def players_list(request):
    queryset = players.objects.filter(display=False, played=True)
    table = ResultsView(queryset)
    return render(request, 'game/players_list.html', {'table': table})

def play(request):
    if request.method == "POST":
        form = playersForm(request.POST)
        print(form)
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
        tempPlayKeys = players.objects.values_list('pk', flat=True).filter(played=True)
        print(tempPlayKeys)
        playKeys.append(tempPlayKeys)
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
    return HttpResponseRedirect('/game/results')
