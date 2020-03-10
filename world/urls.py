from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'worldborders', views.WorldBorderViewSet, basename='worldborders')
# urlpatterns = router.urls

# import views
urlpatterns = [
   path('', views.MapView.as_view(), name='world_index'),
   # path('api/', include(router.urls)),
   path('api/', views.api_get_worldborder),
   # path('/api', views.WorldBorderViewSet.as_view()),
]