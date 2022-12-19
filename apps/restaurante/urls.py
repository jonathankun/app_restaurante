from django.urls import path
from . import views

urlpatterns = [
    path('mesero_list/', views.mesero_list, name='mesero_list'),
    path('plato_list/', views.plato_list, name='plato_list'),
    path('platillo_query/', views.platillo_query, name='platillo_query'),
    path('mesero_query/', views.mesero_query, name='mesero_query'),
    path('mesero_query2/', views.mesero_query2, name='mesero_query2')
]