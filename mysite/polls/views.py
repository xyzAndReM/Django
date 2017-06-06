from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render



from .models import List,Question,Choice


def index(request):
    list_list = List.objects.order_by('-pub_date')
    context = {
        'list_list': list_list,
    }
    return render(request,'polls/index.html',context)


def list_contents(request, list_id):
    lc = get_object_or_404(List,pk=list_id)
    return render(request, 'polls/list_contents.html', {'lc': lc})
# Leave the rest of the views (detail, results, vote) unchanged
# ...

def question_contents(request,question_id):
    print("lol")
    question = get_object_or_404(Question,pk=question_id)
    #return HttpResponse("You're voting on question %s." % question_id)
    return render(request,'polls/question_contents.html', {'question': question })



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/question_contents.html', {
            'question': question,
            'error_message': "Você não assinalou uma opção",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))