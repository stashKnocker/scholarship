from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Personal_detail


# Register your models here.
class Personal_detail_Admin(admin.ModelAdmin):
    list_display = ['owner','Fullname', 'Aadhar_number', 'Date_of_birth', 'Father_name', 'District', 'roll_number', 'applying_for']
    model = Personal_detail
    last_filter = ['Fullname', 'Aadhar_number']
    search_fields = ['Fullname', 'Aadhar_number']



# Register your models here.
admin.site.register(Personal_detail, Personal_detail_Admin)
