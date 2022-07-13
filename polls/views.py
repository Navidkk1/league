from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import League,Team






def index(request):
    latest_league_list = League.objects.order_by('-pub_date')[:5]
    context = {'latest_league_list': latest_league_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    league = get_object_or_404(League, pk=question_id)
    return render(request, 'polls/detail.html', {'league': league})

def results(request, question_id):
    league = get_object_or_404(League, pk=question_id)
    return render(request, 'polls/results.html', {'league': league})

def vote(request, question_id):
    league = get_object_or_404(League, pk=question_id)
    try:
        selected_team = league.team_set.get(pk=request.POST['team'])
    except (KeyError, Team.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'league': league,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_team.votes += 1
        selected_team.save()

        return HttpResponseRedirect(reverse('polls:results', args=(league.id,)))












