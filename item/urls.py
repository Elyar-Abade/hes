from django.urls import path
from . import views
urlpatterns = [
    path('', views.WelcomePageView.as_view()),
    path('<requested_item>', views.ItemView.as_view())
]