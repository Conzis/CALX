from django import forms

from django import forms

gender_choice =(
    ("ชาย", 'ชาย'),
    ("หญิง", 'หญิง'),
)

class BMRform(forms.Form):
    gender = forms.ChoiceField(choices = gender_choice, required=True, label="เพศ")
    weight = forms.IntegerField(required=True, label="น้ำหนัก")
    high = forms.IntegerField(required=True, label="ส่วนสูง")
    age = forms.IntegerField(required=True, label="อายุ")