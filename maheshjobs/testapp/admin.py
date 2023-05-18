from django.contrib import admin
from testapp.models import HydJobs,PuneJobs,BngJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)

class BngJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(BngJobs,BngJobsAdmin)
