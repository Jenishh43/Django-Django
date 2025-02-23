from django.urls import path
from . import views

urlpatterns =[
    path('', views.chart_list, name='chart_list'),
    path('chart/<int:pk>/', views.chart_detail, name='chart_detail'),
    path('chart/new/', views.chart_new, name='chart_new'),
    path('chart/<int:pk>/edit/', views.chart_edit, name='chart_edit'),
]