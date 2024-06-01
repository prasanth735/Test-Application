from django.shortcuts import render,redirect
from django.views.generic import View

from myapp.forms import StudentForm
from myapp.models import Sudent

# Create your views here.


class AddStudentView(View):

    def get(self,request,*args,**kwargs):

        form=StudentForm()

        return render (request,"add.html",{"form":StudentForm})
    

    def post(self,request,*args,**kwargs):

        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            return render (request,"add.html",{"form":form})
        

class ListStudentView(View):

    def get(self,request,*args,**kwargs):

        data=Sudent.objects.all()

        return render(request,"list.html",{"data":data})




class StudentDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        st=Sudent.objects.get(id=id)
        return render(request,"detail.html",{"st":st})
    

class UpdateStudentView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        st=Sudent.objects.get(id=id)
        form=StudentForm(instance=st)

        return render (request,"update.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        st=Sudent.objects.get(id=id)
        

        form=StudentForm(request.POST,request.FILES,instance=st,)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            return render (request,"update.html",{"form":form})

            
    

class DeleteSudentView(View):


    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        Sudent.objects.get(id=id).delete()
        return redirect("list")
