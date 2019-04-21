from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Scheme)
admin.site.register(models.Beneficiary)
admin.site.register(models.Transaction)
admin.site.register(models.Fund)
admin.site.register(models.Status)
admin.site.register(models.TempApproved)
admin.site.register(models.Applicant)
