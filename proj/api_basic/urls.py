from django.urls import path, include
from .views import GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/', GenericAPIView.as_view()),
    path('article/<int:id>/', GenericAPIView.as_view()),
]
