from rest_framework.serializers import ModelSerializer

from polls.models import Choice, Question


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"
        read_only_fields = ["question", "votes"]


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionDetailSerializer(ModelSerializer):
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"
