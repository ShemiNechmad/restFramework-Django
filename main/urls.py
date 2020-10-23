from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path("<int:id>", views.index, name="index"),
    path('mainApi/', views.mainApi)
]
