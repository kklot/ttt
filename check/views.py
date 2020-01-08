from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

# from django.template import loader
    # template = loader.get_template('check/index.html')
    # return HttpResponse(template.render(context, request))
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return(HttpResponse(output))

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # mapping template variable names to Python objects
#     context = {'latest_question_list': latest_question_list} 
#     return render(request, 'check/index.html', context)

from django.views import generic
class Qlist(generic.ListView):
    """display list"""
    template_name = 'check/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# from django.http import Http404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')    
from django.shortcuts import get_object_or_404
    # get_list_or_404

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'check/detail.html', {'question': question})

class Qdetail(generic.DetailView):
    """docstring for Qdetail"""
    model = Question
    template_name = 'check/detail.html'

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'check/detail.html', {
            'question': question,
            'error_message': "U did not select a choice",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('check:results', args=(question.id,)))
    # return HttpResponse("Voting on %s" % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)    
#     response = "result of question %s."
#     return render(request, 'check/results.html', {'question': question})
    # return HttpResponse(response % question_id)

class Vresult(generic.DetailView):
    """docstring for VoteResult"""
    model = Question
    template_name = 'check/results.html'

from .models import DuocThu, Tuongtac

from .forms import CheckTT
from .kutils import gen_hash_tt

def get_tt(request):
    formtt = CheckTT()
    return render(request, 'check/tuongtac.html', {'formtt': formtt})

def ketqua_tt(request):
    formtt = CheckTT(request.POST)
    # text1 = formtt['thuoc_1'].value()+formtt['thuoc_2'].value()
    need_hash = gen_hash_tt(formtt['thuoc_1'].value(),
                            formtt['thuoc_2'].value())
    match_tt = get_object_or_404(Tuongtac, tt_hash=need_hash)
    return render(request, 'check/ketqua_tt.html', {'match_tt': match_tt})