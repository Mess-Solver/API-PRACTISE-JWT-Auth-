from django.urls import path
from . import views


urlpatterns=[path('',                  views.Bio_CL.as_view(),    name='list'),
              path('<int:id>',        views.Bio_RUD.as_view(),     name='ret'),

]