from django.urls import path

from rseti import views

urlpatterns = [
    path('', views.index),
    path('new/', views.newPage),
    path('next/', views.next),
    path('new1/', views.savePage),
    path('2nd-installment-request/', views.secondInstallmentRequest),
    path('2nd-installment-release/', views.secondInstallmentRelease),

    path('loadDistricts/', views.loadDistricts)
]