from django import forms

from rseti.models import SecondInstalmentRequest, SecondInstalmentRelease


class SecondInstalmentRequestForm(forms.ModelForm):
    class Meta:
        model = SecondInstalmentRequest
        fields = '__all__'
        widgets = {
            "secondInstalmentRequestLetterFile": forms.FileInput(attrs={"class": "form-control "}),
            "formGFR12AFile": forms.FileInput(attrs={"class": "form-control "}),
            "formFormat3File": forms.FileInput(attrs={"class": "form-control "}),
            "intrestFirstInstallmentFile": forms.FileInput(attrs={"class": "form-control "}),
            "firstInstallmentAmountFile": forms.FileInput(attrs={"class": "form-control "}),
            "declarationOfBankFile": forms.FileInput(attrs={"class": "form-control "}),
            "photoesOfBuildings": forms.FileInput(attrs={"class": "form-control "}),
            "notionalIntrest": forms.TextInput(attrs={"class": "form-control req"}),
            "approvalOfNIRDPR": forms.TextInput(attrs={"class": "form-control req"})

        }


class SecondInstalmentReleaseForm(forms.ModelForm):
    class Meta:
        model = SecondInstalmentRelease
        fields = "__all__"
        widgets = {
            "dateOfCredit": forms.TextInput(attrs={"class": "form-control req"}),
            "amountRecieved": forms.TextInput(attrs={"class": "form-control req"}),
            "intrestDeducted": forms.TextInput(attrs={"class": "form-control "}),
            "tdsAmount": forms.TextInput(attrs={"class": "form-control req"}),
            "issues": forms.Textarea(attrs={"class": "form-control req"})
        }
