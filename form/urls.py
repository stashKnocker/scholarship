from django.urls import path
from .views import (FormListView, FormDetailView, FormCreateView, FormUpdateView, FormDeleteView,)



urlpatterns = [
    path('', FormListView.as_view(), name= 'form_list'),
    path('form/create', FormCreateView.as_view(), name='form_create'),
    path('<int:pk>/', FormDetailView.as_view(), name= 'form_detail'),
    path('<int:pk>/delete/', FormDeleteView.as_view(), name='form_delete'),
    path('<int:pk>/edit/',FormUpdateView.as_view(), name='form_edit')
]

