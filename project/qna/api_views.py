from .models import *
from .serializers import *
from .api_authentication import AdminOnlyAuth

from rest_framework import viewsets
from rest_framework.response import Response

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer
    authentication_classes = (AdminOnlyAuth, )
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CustomQuestionView(viewsets.ViewSet):
    def list(self, request, format=None):
        questions = [question.question_text for question in Question.objects.all()]
        return Response(questions)