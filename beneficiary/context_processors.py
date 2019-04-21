from . import models
import datetime
def BeneficiaryList(request):
    pending_list = [u['beneficiary'] for u in models.Status.objects.all().filter(status__exact='pending', month=datetime.datetime.now().month, year=datetime.datetime.now().year).values('beneficiary')]
    disapproved_list = [u['beneficiary'] for u in models.Status.objects.all().filter(status__exact='disapproved', month=datetime.datetime.now().month, year=datetime.datetime.now().year).values('beneficiary')]
    return {'pending_list':pending_list, 'disapproved_list':disapproved_list}