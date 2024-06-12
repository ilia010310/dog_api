from django.urls import path, include
from .controllers import DogList, DogDetail, BreedList, BreedDetail
from rest_framework.routers import DefaultRouter


app_name = 'api'

router = DefaultRouter()
router.register(r'breed-detail', BreedDetail, basename='breed-detail')
router.register(r'breed-list', BreedList, basename='breed-list')

urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list-create'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('', include(router.urls)),

]
