from django.shortcuts import render
from .prediction import PCOS_predict

# Create your views here.

def detection(request):
    if request.method == 'POST':

        age=int(request.POST['age'])
        height=int(request.POST['height'])/100
        weight=int(request.POST['weight'])
        BMI=weight/pow(height,2)
        bldgroup=int(request.POST['bldgroup'])
        weightgain=int(request.POST.get('weightgain',0))
        hairgrowth=int(request.POST.get('hairgrowth',0))
        skindark=int(request.POST.get('skindark',0))
        hairloss=int(request.POST.get('hairloss',0))
        pimples=int(request.POST.get('pimples',0))
        fastfood=int(request.POST.get('fastfood',0))

        if PCOS_predict(age,weight,height,BMI,bldgroup,weightgain,hairgrowth,skindark,hairloss,pimples,fastfood):
            message="You have PCOS"
        else:
            message="You do not have PCOS"

        return render(request,'index.html',{'message':message})
    else:
        return render(request,'index.html')

