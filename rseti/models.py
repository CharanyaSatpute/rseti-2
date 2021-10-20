from django.db import models


# Create your models here.


class Sponsor_bank(models.Model):
    bank_name = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=500)
    rseti_department = models.CharField(max_length=200)
    department_address = models.CharField(max_length=200)
    top_executives = models.CharField(max_length=200)
    landline_number = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.bank_name


class TrustAccountDetails(models.Model):
    name_of_the_trust = models.CharField(max_length=200)
    house_no = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    state = models.IntegerField()
    district = models.IntegerField()
    pincode = models.CharField(max_length=200)
    bank_acc_no = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    back_acc_type = models.CharField(max_length=200)
    back_acc_ifs = models.CharField(max_length=200)
    registration_certificate = models.CharField(max_length=2000)
    pan_card = models.CharField(max_length=2000)
    it_exemption = models.CharField(max_length=2000)
    mou_file = models.CharField(max_length=2000)

    def __str__(self):
        return self.name_of_the_trust


class RegionalOfficeDetails(models.Model):
    name_of_rseti = models.CharField(max_length=200)
    house_no = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    state = models.IntegerField()
    district = models.IntegerField()
    pincode = models.CharField(max_length=200)
    office_email = models.CharField(max_length=200)
    concerned_official = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)
    landline_no = models.CharField(max_length=200)
    email_add = models.CharField(max_length=200)
    details_update = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name_of_rseti


# class State(models.Model):
#     objects = models.Manager()
#     lgd_code = models.IntegerField()
#     state_name = models.CharField(max_length=250)
#     state_short_code = models.CharField(max_length=100)
#     status = models.IntegerField()
#
#     def __str__(self):
#         return self.state_name
#
#     def __unicode__(self):
#         return u'%s' % self.state_name
#
#     class Meta:
#         db_table = "master_state1"
#
#
# class District(models.Model):
#     objects = models.Manager()
#     lgd_code = models.IntegerField()
#     state_id = models.ForeignKey("State", on_delete=models.CASCADE)
#     district_name = models.CharField(max_length=250)
#     special_area = models.CharField(max_length=100)
#     status = models.IntegerField()
#
#     def __str__(self):
#         return self.district_name
#
#     def __unicode__(self):
#         return u'%s' % self.district_name
#
#     class Meta:
#         db_table = "master_district1"


class SecondInstalmentRequest(models.Model):
    secondInstalmentRequestLetterFile = models.FileField(max_length=200, blank=True)
    formGFR12AFile = models.FileField(max_length=200, blank=True)
    formFormat3File = models.FileField(max_length=200, blank=True)
    intrestFirstInstallmentFile = models.FileField(max_length=200, blank=True)
    firstInstallmentAmountFile = models.FileField(max_length=200, blank=True)
    declarationOfBankFile = models.FileField(max_length=200, blank=True)
    photoesOfBuildings = models.FileField(max_length=200, blank=True)
    notionalIntrest = models.CharField(max_length=200)
    approvalOfNIRDPR = models.CharField(max_length=200)


class SecondInstalmentRelease(models.Model):
    dateOfCredit = models.CharField(max_length=200)
    amountRecieved = models.CharField(max_length=200)
    intrestDeducted = models.CharField(max_length=200)
    tdsAmount = models.CharField(max_length=200)
    issues = models.CharField(max_length=500)
