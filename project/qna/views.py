from django.views import generic
from django.shortcuts import redirect
from django.views.generic.base import TemplateResponseMixin

from .models import Question, Choice
from .mixins import RequireLoginMixin


class IndexView(generic.ListView):
    template_name = 'qna/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "qna/question_detail.html"

class DeleteView(generic.DeleteView):
    model = Question
    success_url = "/polls/"

class VoteView(generic.View):

    def get_queryset(self, choice_id):
        return Choice.objects.get(pk=choice_id)

    def post(self, request, pk):
        question_id = pk
        choice_id = request.POST.get('choice', None)
        try:
            queryset = self.get_queryset(choice_id)
        except (KeyError, Choice.DoesNotExist):
            return redirect('polls:detail', pk=question_id)
        else:
            queryset.votes += 1
            queryset.save()
            return redirect('polls:vote_result', pk=question_id)


class ResultsView(TemplateResponseMixin, generic.View):
    template_name = 'qna/results.html'

    def get_queryset(self, question_id):
        return Question.objects.get(pk=question_id)

    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        context = {'question': queryset}
        return self.render_to_response(context)


class SwitchboardView(generic.View):
    def get(self, request, pk):
        view = ResultsView.as_view()
        return view(request, pk)

    def post(self, request, pk):
        view = VoteView.as_view()
        return view(request, pk)
