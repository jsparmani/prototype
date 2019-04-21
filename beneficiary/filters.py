from . import models
import django_filters

class BeneficiaryFilter(django_filters.FilterSet):
    """ name = django_filters.CharFilter(lookup_expr='istartswith')
    age_greater = django_filters.NumberFilter(name='age',lookup_expr='gt')
    age_lesser = django_filters.NumberFilter(name='age',lookup_expr='lt') """
    class Meta():
        model = models.Beneficiary
        fields = {
            'scheme':['exact',],
            'name':['istartswith',],
            'age':['exact', 'lt', 'gt'],
            'phone_num': ['exact'],
            'account_number': ['exact'],
            'ifsc_code': ['exact'],
        }


class StatusFilter(django_filters.FilterSet):


    class Meta():
        model = models.Status
        fields = {
            'beneficiary__scheme' : ['exact',],
            'beneficiary__name':['istartswith',],
            'beneficiary__age':['exact', 'lt', 'gt'],
            'beneficiary__phone_num': ['exact'],
            'beneficiary__account_number': ['exact'],
            'beneficiary__ifsc_code': ['exact'],
        }
