from django.urls import path
from . import views

app_name = 'beneficiary'

urlpatterns = [
    path('populate/', views.populate, name='populate'),
    path('add_applicant/', views.add_applicant, name='add_applicant'),
    path('search/', views.search, name='search' ),
    path('search_admin/', views.search_admin, name='search_admin' ),
    path('status_approve/<int:pk>/', views.status_approve, name='status_approve'),
    path('status_disapprove/<int:pk>/', views.status_disapprove, name='status_disapprove'),
    path('status_pending/<int:pk>/', views.status_pending, name='status_pending'),
    path('status_temp_approve/<int:pk>/', views.status_temp_approve, name='status_temp_approve'),
    path('check_url/', views.check_url, name='check_url'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('make_temp_payment/', views.make_temp_payment, name='make_temp_payment'),
    path('edit_transactions_admin/', views.edit_transactions_admin, name='edit_transactions_admin'),
] 