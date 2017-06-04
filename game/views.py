from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from .forms import playersForm
from django.http import HttpResponseRedirect
import django_tables2 as tables
import logging
from .gameScript import *
logger = logging.getLogger()

def index(request):
    num_plays=players.objects.all().count()
    logger.error('There was some crazy error lol', exc_info=True, extra={'request': request, })
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



def run_script(request):
    playRound()
    return HttpResponseRedirect('/game/results')
