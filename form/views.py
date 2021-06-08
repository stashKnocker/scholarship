from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)

from .models import Personal_detail

# Create your views here.
class FormListView(LoginRequiredMixin, ListView):

    model = Personal_detail
    template_name = 'form_list.html'
    login_url = 'login'


class FormDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Personal_detail
    template_name = 'form_detail.html'
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return obj.owner == self.request.user


class FormUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Personal_detail
    
    fields = ('Fullname', 'Email_Address', 'Gender', 'Date_of_birth', 'Age', 'Aadhar_number', 'Marital_status',
        'Father_name', 'Father_occupation', 'Father_number', 'Mother_name', 'Mother_occupation', 'Guardian_name',
         'Guardian_occupation', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'District', 'Zipcode',
         'Annual_income', 'Caste', 'Community','course_pursuing', 'specialization', 'roll_number', 'mark_in_higher_school', 
         'mark_in_secondary_school', 'Education_mode', 'scholarship', 'mention_scholarship','disability', 'mention', 'applying_for')
    
    template_name = 'form_edit.html'
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return obj.owner == self.request.user


class FormDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Personal_detail
    template_name = 'form_delete.html'
    success_url = reverse_lazy('form_list')
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return obj.owner == self.request.user


class FormCreateView(LoginRequiredMixin, CreateView):

    model = Personal_detail
    template_name = 'form_create.html'
    fields = ('Fullname', 'Email_Address', 'Gender', 'Date_of_birth', 'Age', 'Aadhar_number', 'Marital_status',
        'Father_name', 'Father_occupation', 'Father_number', 'Mother_name', 'Mother_occupation', 'Guardian_name',
         'Guardian_occupation', 'Mobile_number', 'Address_1', 'Address_2', 'City', 'District', 'Zipcode',
         'Annual_income', 'Caste', 'Community','course_pursuing', 'specialization', 'roll_number', 'mark_in_higher_school', 
         'mark_in_secondary_school', 'Education_mode', 'scholarship', 'mention_scholarship','disability', 'mention', 'applying_for')

    login_url = 'login'

    def form_valid(self, form): # new
        form.instance.owner = self.request.user
        return super().form_valid(form)
    






# Create your views here.
