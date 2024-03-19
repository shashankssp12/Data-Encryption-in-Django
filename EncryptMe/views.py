from django.shortcuts import render, redirect
from EncryptMe.models import *
from django.contrib import messages


# def show(request):
#     text='Encrypt ME'
#     return render(request,'index.html',context={'text': text})

def fectchData(request):
    if request.method == 'POST':
        data = request.POST
        print("shashank")
    
        f_name = data.get('first_name')
        l_name = data.get('last_name')

        PII.objects.create(
        first_name=f_name,
        last_name =l_name
        )
        return redirect('/')
    
    modelData = PII.objects.all()
    messages.info(request, "Fields Encrypted")
    return render(request, 'index.html',{'Data':modelData})



