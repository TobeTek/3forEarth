from django.urls import path
from .views import TreeListView, TreeDetailView,TreeTypeListView
urlpatterns = [
    path('', TreeListView.as_view()),
    path('<int:pk>', TreeDetailView.as_view()),
    path('treetype/', TreeTypeListView.as_view()),

]

