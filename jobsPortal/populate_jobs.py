import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'jobsPortal.settings')
import django
django.setup()


from faker import Faker
from testApp.models import HyderabadJobs,BangaloreJobs,PuneJobs,ChennaiJobs
from random import *




fake = Faker()

def phonenumbergen():
    d1 = randint(7,9)
    num = str(d1)
    for i in range(7):
        num += str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead', 'Software Engineer'))
        feligibility = fake.random_element(elements=('Btech','M.Tech','MCA','PhD'))
        faddress = fake.address()
        femail = fake.email()
        fnumber = phonenumbergen()
        hydjobs_record = ChennaiJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility
                                                            ,address=faddress,email=femail,phonenumber=fnumber)


populate(25)
