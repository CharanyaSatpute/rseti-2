from django.shortcuts import render

# Create your views here.
from rseti.forms import SecondInstalmentRequestForm, SecondInstalmentReleaseForm
from rseti.models import TrustAccountDetails, Sponsor_bank, RegionalOfficeDetails


def index(res):
    # content = {
    #     'states': State.objects.all()
    # }
    return render(res, 'trust-details.html',)


def newPage(request):
    bank_name = request.POST.get("bank_name")
    postal_address = request.POST.get('postal_address')
    rseti_department = request.POST.get('rseti_department')
    department_address = request.POST.get('department_address')
    top_executives = request.POST.get('top_executives')
    landline_number = request.POST.get('landline_number')
    address = request.POST.get('address')

    name_of_the_trust = request.POST.get('name_of_the_trust')
    house_no = request.POST.get('house_no')
    street = request.POST.get('street')
    village = request.POST.get('village')
    state = request.POST.get('statedrop')
    district = request.POST.get('districtdrop')
    pincode = request.POST.get('pincode')
    bank_acc_no = request.POST.get('bank_acc_no')
    branch_name = request.POST.get('bank_name')
    back_acc_type = request.POST.get('back_acc_type')
    back_acc_ifs = request.POST.get('back_acc_ifs')
    registration_certificate = request.POST.get('registration_certificate')
    pan_card = request.POST.get('pan_card')
    it_exemption = request.POST.get('it_exemption')
    mou_file = request.POST.get('mou_file')

    TrustAccountDetails(name_of_the_trust=name_of_the_trust, house_no=house_no, street=street, village=village,
                        state=state, district=district, pincode=pincode, bank_acc_no=bank_acc_no, bank_name=branch_name,
                        back_acc_type=back_acc_type, back_acc_ifs=back_acc_ifs,
                        registration_certificate=registration_certificate, pan_card=pan_card, it_exemption=it_exemption,
                        mou_file=mou_file).save()
    Sponsor_bank(bank_name=bank_name, postal_address=postal_address, rseti_department=rseti_department,
                 department_address=department_address, top_executives=top_executives, landline_number=landline_number,
                 address=address).save()
    return index(request)


def loadDistricts(res):
    # e = res.GET.get('e')
    # content = {
    #     'District': District.objects.filter(state_id=e)
    # }
    return render(res, 'districts.html',)


def next(res):
    # content = {
    #     'states': State.objects.all()
    # }
    return render(res, 'regional-office-details.html',)


def savePage(request):
    name_of_rseti = request.POST.get('name_of_rseti')
    house_no = request.POST.get('house_no')
    street = request.POST.get('street')
    village = request.POST.get('village')
    state = request.POST.get('statedrop2')
    district = request.POST.get('districtdrop2')
    pincode = request.POST.get('pincode')
    office_email = request.POST.get('office_email')
    concerned_official = request.POST.get('concerned_official')
    designation = request.POST.get('designation')
    mobile_no = request.POST.get('mobile_no')
    landline_no = request.POST.get('landline_no')
    email_add = request.POST.get('email_add')
    details_update = request.POST.get('details_update')

    RegionalOfficeDetails(name_of_rseti=name_of_rseti, house_no=house_no, street=street, village=village, state=state,
                          district=district, pincode=pincode, office_email=office_email,
                          concerned_official=concerned_official, designation=designation, mobile_no=mobile_no,
                          landline_no=landline_no, email_add=email_add, details_update=details_update).save()
    return next(request)


def secondInstallmentRequest(req):
    if req.method == 'POST':
        form = SecondInstalmentRequestForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SecondInstalmentRequestForm()
    return render(req, '2nd-instalment-request-view.html', {"form": form})


def secondInstallmentRelease(req):
    if req.method == 'POST':
        form = SecondInstalmentReleaseForm(req.POST)
        if form.is_valid():
            form.save()
    else:
        form = SecondInstalmentReleaseForm()
    return render(req, '2nd-instalment-release-view.html', {"form": form})
