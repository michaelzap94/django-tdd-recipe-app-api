from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# the DefaultRouter is a built-in feature of rest_framework that will automatically generate the URLs
# for our viewset that we created in the views.py (TagViewSet) eg: set(/api/recipe | /api/recipe/34 | /api/recipe/34/put)
# so it automatically registers the appropiate URLs for all the actions in our viewset
router = DefaultRouter()
router.register('tags', views.TagViewSet)

#we need this for the reverse() function to look up the correct name
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]