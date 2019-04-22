from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from . import models
from . import filters
from . import forms
import datetime
import json

# Create your views here.

def populate(request):

    for N in range(6000):
        scheme_id_list = [u['pk'] for u in models.Scheme.objects.all().filter(name__exact = 'Student Scholarship').values('pk')]
        scheme = random.choice(scheme_id_list)

        f = open('D:/Codes/name.txt','r')
        names = f.readlines()
        name = random.choice(names)


        gender = random.choice(['M','F'])


        age = random.randint(12,35)


        phone_num = random.randint(7000000000,9999999999)

        account_num = random.randint(100000000000,999999999999)


        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ifsc = ''
        for i in range(4):
            ifsc = ifsc + random.choice(letters)
        
        ifsc = ifsc + str(random.randint(1000000,9999999))


        models.Beneficiary.objects.create(
            scheme = models.Scheme.objects.get(pk__exact=scheme),
            name = name,
            gender=gender,
            age=age,
            phone_num=phone_num,
            account_number = account_num,
            ifsc_code = ifsc, 

        )
    
    return HttpResponse('Done')





def search(request):
    beneficiary_list = models.Beneficiary.objects.all()
    beneficiary_filter = filters.BeneficiaryFilter(request.GET, queryset=beneficiary_list)
    return render(request, 'beneficiary/beneficiary_list.html', {'filter':beneficiary_filter})


def status_approve(request, pk):
    member = models.Status.objects.all().filter(beneficiary__pk__exact=pk, month__exact=datetime.datetime.now().month, year__exact=datetime.datetime.now().year)
    member.delete()
    return redirect('beneficiary:check_url')

def status_disapprove(request, pk):
    beneficiary = models.Beneficiary.objects.get(pk__exact=pk)
    pending_member = models.Status.objects.all().filter(beneficiary__pk__exact=pk, month__exact=datetime.datetime.now().month, year__exact=datetime.datetime.now().year, status__exact='pending')
    if not len(pending_member) == 0:
        for member in pending_member:
            member.status = 'disapproved'
            member.save()
    else:

        models.Status.objects.create(
            beneficiary=beneficiary,
            month = datetime.datetime.now().month,
            year = datetime.datetime.now().year,
            status = 'disapproved'
        )
    return redirect('beneficiary:check_url')


def status_pending(request, pk):
    beneficiary = models.Beneficiary.objects.get(pk__exact=pk)
    disapproved_member = models.Status.objects.all().filter(beneficiary__pk__exact=pk, month__exact=datetime.datetime.now().month, year__exact=datetime.datetime.now().year, status__exact='disapproved')
    if not len(disapproved_member) == 0:
        for member in disapproved_member:
            member.status = 'pending'
            member.save()
    else:
        models.Status.objects.create(
            beneficiary=beneficiary,
            month = datetime.datetime.now().month,
            year = datetime.datetime.now().year,
            status = 'pending'
        )
    return redirect('beneficiary:check_url')

def check_url(request):
    return render(request, 'beneficiary/check_url.html')


def search_admin(request):
    beneficiary_list = models.Beneficiary.objects.all()
    beneficiary_filter = filters.BeneficiaryFilter(request.GET, queryset=beneficiary_list)
    return render(request, 'beneficiary/beneficiary_list_admin.html', {'filter':beneficiary_filter})


def make_payment(request):

    everyone = [u['pk'] for u in models.Beneficiary.objects.all().values('pk')]
    pending_list = [u['beneficiary'] for u in models.Status.objects.all().filter(status__exact='pending').values('beneficiary')]
    disapproved_list = [u['beneficiary'] for u in models.Status.objects.all().filter(status__exact='disapproved').values('beneficiary')]
    everyone = [x for x in everyone if x not in pending_list]
    everyone = [x for x in everyone if x not in disapproved_list]

    for member in everyone:
        transact = models.Transaction.objects.create(
            transaction_id=random.randint(100000000000,999999999999),
            beneficiary=models.Beneficiary.objects.get(pk__exact=member),
            month=datetime.datetime.now().month,
            year=datetime.datetime.now().year,
        )
        fund = models.Fund.objects.get(pk__exact=1)
        fund.balance = fund.balance - transact.beneficiary.scheme.amount
        fund.save()

    return redirect('home')


def edit_transactions_admin(request):
    status_list = models.Status.objects.all()
    status_filter = filters.StatusFilter(request.GET, queryset=status_list)
    return render(request, 'beneficiary/status_list.html', {'filter':status_filter})


def status_temp_approve(request, pk):

    member = models.Status.objects.all().filter(beneficiary__pk__exact=pk, month__exact=datetime.datetime.now().month, year__exact=datetime.datetime.now().year)
    member.delete()
    models.TempApproved.objects.create(
        beneficiary = models.Beneficiary.objects.get(pk__exact=pk)
    )
    return redirect('beneficiary:check_url')

def make_temp_payment(request):
    members = models.TempApproved.objects.all()
    for member in members:
        transact = models.Transaction.objects.create(
            transaction_id=random.randint(100000000000,999999999999),
            beneficiary=models.Beneficiary.objects.get(pk__exact=member.beneficiary.pk),
            month=datetime.datetime.now().month,
            year=datetime.datetime.now().year,
        )
        fund = models.Fund.objects.get(pk__exact=1)
        fund.balance = fund.balance - transact.beneficiary.scheme.amount
        fund.save()
        member.delete()

    return redirect('home')


def add_applicant(request):
    if request.method == 'POST':
        form = forms.AddApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Error!')
    else:
        form = forms.AddApplicantForm()
        return render(request, 'beneficiary/add_applicant.html', {'form':form})


def list_applicant_rent(request):
    applicant_list = models.Applicant.objects.all().filter(is_disapproved__exact=0, is_approved_rent__exact=0)
    return render(request, 'beneficiary/applicant_list.html', {'applicant_list':applicant_list})


def list_applicant_clerk(request):
    applicant_list = models.Applicant.objects.all().filter(is_disapproved__exact=0,is_approved_clerk__exact=0, is_approved_rent__exact=1)
    return render(request, 'beneficiary/applicant_list.html', {'applicant_list':applicant_list})


def list_applicant_adc(request):
    applicant_list = models.Applicant.objects.all().filter(is_disapproved__exact=0,is_approved_adc__exact=0, is_approved_clerk__exact=1)
    return render(request, 'beneficiary/applicant_list.html', {'applicant_list':applicant_list})


def disapprove_applicant(request, pk):
    applicant = models.Applicant.objects.get(pk__exact=pk)
    applicant.is_disapproved = True
    applicant.save()
    return redirect('beneficiary:check_url')

def add_beneficiary(request,pk):
    applicant = models.Applicant.objects.get(pk__exact=pk)
    applicant.is_approved_adc=1
    applicant.save()
    models.Beneficiary.objects.create(
        scheme=applicant.scheme,
        name = applicant.name,
        gender = applicant.gender,
        age = applicant.age,
        phone_num = applicant.phone_num,
        account_number = applicant.account_number,
        ifsc_code = applicant.ifsc_code
    )

    return redirect('beneficiary:check_url')


def applicant_approve_rent(request, pk):

    applicant = models.Applicant.objects.get(pk__exact=pk)
    applicant.is_approved_rent = 1
    applicant.save()
    return redirect('beneficiary:check_url')

def applicant_approve_clerk(request, pk):

    applicant = models.Applicant.objects.get(pk__exact=pk)
    applicant.is_approved_clerk = 1
    applicant.save()
    return redirect('beneficiary:check_url')


def display_beneficiary_number(request):

    widow = models.Beneficiary.objects.all().filter(scheme__name__exact='Widow Pension').count()
    old_age = models.Beneficiary.objects.all().filter(scheme__name__exact='Old Age Pension').count()
    scholarship = models.Beneficiary.objects.all().filter(scheme__name__exact='Student Scholarship').count()



    label = ['Widow Pension', 'Old Age Pension', 'Student Scholarship']

    data = {
                "label": label,
                "value": [widow,old_age,scholarship]

            }
    jsondata = json.dumps(data)

    return render(request, 'beneficiary/display_beneficiary_number.html', {'jsondata':jsondata})


def schemewise_data(request):

    value1=[]
    value2=[]
    value3=[]
    for month in range(1,13):
        value1.append(models.Transaction.objects.all().filter(beneficiary__scheme__name__exact='Widow Pension', month__exact=month).count() * models.Scheme.objects.get(name__exact='Widow Pension').amount)
        value2.append(models.Transaction.objects.all().filter(beneficiary__scheme__name__exact='Old Age Pension', month__exact=month).count() * models.Scheme.objects.get(name__exact='Old Age Pension').amount)
        value3.append(models.Transaction.objects.all().filter(beneficiary__scheme__name__exact='Student Scholarship', month__exact=month).count() * models.Scheme.objects.get(name__exact='Student Scholarship').amount)

    data = [{
        "label": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
        "value": value1
    },
    {
        "label": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
        "value": value2
    },
    {
        "label": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
        "value": value3
    }]

    jsondata = json.dumps(data)

    return render(request, 'beneficiary/schemewise_data.html', {'jsondata': jsondata})


def personwise_data(request, pk):

    data = []
    for month in range(1,13):
       transacts =  models.Transaction.objects.all().filter(pk__exact=pk, month__exact=month, year__exact=datetime.datetime.now().year)
       if len(transacts) == 0:
           data.append(0)
       else:
            data.append(1)

    

    return render(request, 'beneficiary/personwise_data.html', {'data': data})


def change_amount(request):
    if request.method == 'POST':
        form = forms.ChangeAmountForm(request.POST)
        if form.is_valid():
            scheme = models.Scheme.objects.get(name__iexact=form.cleaned_data['scheme'])
            scheme.amount = form.cleaned_data['amount']
            scheme.save()
            return redirect('beneficiary:change_amount')
        else:
            return HttpResponse("<h1>Some Error Occured</h1>")
        
    else:
        form = forms.ChangeAmountForm()
        return render(request, 'beneficiary/change_amount.html', {'form':form})
            








