from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serilaizers import QuestionSerializer
from questions.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
