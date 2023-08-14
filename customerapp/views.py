from django.shortcuts import render,redirect
from .models import customer
from django.http import HttpResponse
from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class SubmitInput(View):
    def get(self,request):
        return render(request,'customerinput.html')
class Submit(View):
    def get(self,request):
        c_id=int(request.GET["t1"])
        c_name=request.GET["t2"]
        c_job=request.GET["t3"]
        c_branch=request.GET["t4"]
        c_balance=float(request.GET["t5"])
        c=customer(cid=c_id,cname=c_name,cjob=c_job,cbranch=c_branch,cbalance=c_balance)
        c.save()
        return HttpResponse("customer submitted successfully")
class Display(View):
    def get(self,request):
        qs=customer.objects.all()
        condic={"records":qs}
        return render(request,'display.html',context=condic)
class DeleteInput(View):
    def get(self,request):
        qs=customer.objects.all()
        condic={"records": qs}
        return render(request,'deleteinput.html',context=condic)
class Delete(View):
    def get(self,request):
        c_id=int(request.GET["t1"])
        c=customer.objects.get(cid=c_id)
        c.delete()
        return redirect('customerapp/display')
class UpdateInput(View):
    def get(self,request):
        qs = customer.objects.all()
        condic = {"records": qs}
        return render(request,'updateinput.html',context=condic)
class UpdateDetails(View):
    def get(self,request):
        c_id=int(request.GET["t1"])
        c=customer.objects.get(cid=c_id)
        condic={'rec':c}
        return render(request,'update.html',context=condic)
class Update(View):
    def get(self,request):
        c_id=int(request.GET["t1"])
        c=customer.objects.get(cid=c_id)
        c.cname=request.GET["t2"]
        c.cjob=request.GET["t3"]
        c.cbranch=request.GET["t4"]
        c.cbalance=float(request.GET["t5"])
        c.save()

        return redirect('/customerapp/display')
