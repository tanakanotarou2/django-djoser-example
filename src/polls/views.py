from rest_framework.permissions import AllowAny
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from polls.models import Question
from polls.serializers import (
    QuestionDetailSerializer,
)


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [AllowAny]
