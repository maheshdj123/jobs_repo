from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')

from testapp.models import HydJobs
def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)
