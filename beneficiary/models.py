from django.db import models

# Create your models here.


class Scheme(models.Model):

    name = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Beneficiary(models.Model):

    GENDER_CHOICES = [

            ('M', 'Male'),
            ('F', 'Female'),
    ]

    scheme = models.ForeignKey('beneficiary.Scheme', related_name='beneficiaries', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    phone_num = models.PositiveIntegerField()
    account_number = models.PositiveIntegerField()
    ifsc_code = models.CharField(max_length=50)


    def __str__(self):
        return self.name 


class Transaction(models.Model):

    MONTH_CHOICES = [

            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
    ]
    
    transaction_id = models.PositiveIntegerField(unique=True)
    beneficiary = models.ForeignKey('beneficiary.Beneficiary', related_name='transactions', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    month = models.IntegerField(choices=MONTH_CHOICES)
    year = models.CharField(max_length=4)


    def __str__(self):
        return f'{self.transaction_id} {self.beneficiary}'

    class Meta():
        unique_together = ['beneficiary', 'month', 'year']

class Fund(models.Model):

    balance = models.BigIntegerField()
    
    def __str__(self):
        return f'{self.balance}'


class Status(models.Model):

    MONTH_CHOICES = [

            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
    ]

    STATUS_CHOICES = [
        ('disapproved', 'Disapproved'),
        ('pending', 'Pending'),
    ]
    beneficiary = models.ForeignKey('beneficiary.Beneficiary', related_name='status', on_delete=models.CASCADE)
    month = models.IntegerField(choices=MONTH_CHOICES)
    year = models.CharField(max_length=4)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.beneficiary} {self.month} {self.status}'

    
    class Meta():
        unique_together = ['beneficiary', 'month', 'year']


class TempApproved(models.Model):

    beneficiary = models.ForeignKey('beneficiary.Beneficiary', related_name='tempapproved', on_delete=models.CASCADE)

    def __str__(self):
        return self.beneficiary


class Applicant(models.Model):
    
    GENDER_CHOICES = [

            ('M', 'Male'),
            ('F', 'Female'),
    ]

    scheme = models.ForeignKey('beneficiary.Scheme', related_name='applicants', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    phone_num = models.PositiveIntegerField(unique=True)
    account_number = models.PositiveIntegerField()
    ifsc_code = models.CharField(max_length=50)

    is_approved_rent = models.BooleanField(default=False)
    is_approved_clerk = models.BooleanField(default=False)
    is_approved_adc = models.BooleanField(default=False)
    is_disapproved = models.BooleanField(default=False)

    def __str__ (self):
        return self.name

    



    

