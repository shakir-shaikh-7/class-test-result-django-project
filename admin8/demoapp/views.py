from django.shortcuts import render,redirect
from demoapp.models import Student, Subcriber

# Create your views here.
def home(request):
    return render(request, 'demoapp/index.html')



def st_table(request):

    data= Student.objects.all()

    context= {"data":data}


    return render(request, 'demoapp/table1.html',context)

def pass_table(request):

    # data= Student.objects.all()
    data = Student.objects.filter(mark__gt=65)

    context= {"data":data}


    return render(request, 'demoapp/pass.html',context)

def fail_table(request):

    data = Student.objects.filter(mark__lt=65)

    context= {"data":data}


    return render(request, 'demoapp/fail.html',context)

def morethan_table(request):

    data = Student.objects.filter(mark__gt=85)

    context= {"data":data}


    return render(request, 'demoapp/morethan.html',context)



def get_mark(request):

    if request.method == 'POST':
        m = request.POST.get('get_mark')
        data = Student.objects.filter(mark__gt=99)
        context = {"data":data}


    return render(request, 'demoapp/getmark.html',context)

def get_mark(request):

    m = request.POST.get('get_mark')
    data = Student.objects.filter(mark__gt=m)
    context= {"data":data}

    return render(request, 'demoapp/getmark.html',context)



def add_st(request):

    if request.method == 'POST':
        
        r = request.POST.get('roll')
        n = request.POST.get('name')
        m = request.POST.get('mark')

        s1 = Student(roll=r, name=n, mark=m)
        s1.save()
      
    return render(request, 'demoapp/form.html')


def upd_st(request,id=32):

    s1 =Student.objects.get(pk = id)
    context={
            'data': s1
        }

    if request.method == 'POST':
        
        r = request.POST.get('roll')
        n = request.POST.get('name')
        m = request.POST.get('mark')

        # s1 = Student(roll=r, name=n, mark=m)
        s1.roll =r
        s1.name =n
        s1.mark =m
        s1.save()
       
        return redirect('/students/')
      
    return render(request, 'demoapp/upd_form.html',context)


def del_st(request,id=32):
    
    s1 =Student.objects.get(pk = id)
    context={
            'data': s1
        }

    if request.method == 'POST':
        
        r = request.POST.get('roll')

        # s1 =Student.objects.get(roll=r)
        # s1 =Student.objects.get(id)
        s1.delete()
      
        return redirect('/students/')

    return render(request, 'demoapp/del_form.html',context)




def mail(request):
    
    if request.method == 'POST':

      
        mail_1 = request.POST.get('s_email')

        m1 = Subcriber(s_email=mail_1)
        m1.save()
      
    return render(request, 'demoapp/footer.html')

from demoapp.form import MobileForm

def dform(request):
    form = MobileForm()
    if request.method == 'POST':
        # print(request.POST)
        f = MobileForm(request.POST)
        f.save()


    return render(request, 'demoapp/add.html', {'form':form})



# def get_marks1(request):
#     data = request.POST.get('getmark12')
#     return render(request,'demoapp/getmark.html',{'data':data})