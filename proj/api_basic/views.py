from .models import Article
from .serializers import ArticleSerializer

from rest_framework import mixins
from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

"""generic viewsets"""

class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
