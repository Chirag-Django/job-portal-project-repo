from django.shortcuts import render
from testApp.models import HyderabadJobs,BangaloreJobs,PuneJobs,ChennaiJobs

# Create your views here.
def index(request):
    return render(request,'testApp/home.html')

def hydjobs(request):
    jobs_list = HyderabadJobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/hyderabad.html',context=my_dict)

def bangjobs(request):
    jobs_list = BangaloreJobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/bangalore.html',context=my_dict)

def chennaijobs(request):
    jobs_list = ChennaiJobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/chennai.html',context=my_dict)

def punejobs(request):
    jobs_list = PuneJobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/pune.html',context=my_dict)

