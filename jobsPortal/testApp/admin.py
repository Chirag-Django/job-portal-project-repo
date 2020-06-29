from django.contrib import admin
from testApp.models import HyderabadJobs,PuneJobs,BangaloreJobs,ChennaiJobs

# Register your models here.
class HyderabadJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class BangaloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(HyderabadJobs,HyderabadJobsAdmin)
admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)
admin.site.register(BangaloreJobs,BangaloreJobsAdmin)