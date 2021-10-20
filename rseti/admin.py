from django.contrib import admin

# Register your models here.
from rseti.models import Sponsor_bank, TrustAccountDetails, RegionalOfficeDetails, \
    SecondInstalmentRequest, SecondInstalmentRelease

# admin.site.register(State)
# admin.site.register(District)
admin.site.register(Sponsor_bank)
admin.site.register(TrustAccountDetails)
admin.site.register(RegionalOfficeDetails)
admin.site.register(SecondInstalmentRequest)
admin.site.register(SecondInstalmentRelease)
