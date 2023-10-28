from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
from .models import activity
from .forms import addtaskform,edittaskform,yearmonthform



wday=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


def staticpage(request):
    # tl=['Hair Cut','Meditation','Study ML','New Skill Development','Study Maths','Playing Badminton','Study Latest Research', 'Visit Dmart','Study Python','Study SQL','Read Novel','Gratitude Journaling','Speak to an Old Friend','Laundary','Gym Workout', 'Groceries','Meeting','Learn Vocab','Watch Lectures','Morning Walk','Learn a Dish','Do the Dishes','Water can order','Doing Chores','Gardening','Bike Service','Mobile Repair','To Do list','Taking Naps','Beard Setting',"Create a budget for the month","Organize a closet","Watch a classic movie","Research online courses","Schedule a doctor's appointment", "Write thank-you notes","Clean out the refrigerator","Take the dog for a walk","Try a new restaurant","Watch a documentary","Visit a local farmers market","Plan a surprise date night","Organize a game night with friends","Learn a new dance routine","Explore a nearby hiking trail","Donate clothes to a charity","Write a business proposal","Start a collection of something","Create a vision board","Plan a picnic in the park","Volunteer at a local shelter","Declutter your email inbox","Watch a TED talk","Plan a virtual hangout with friends","Create a workout playlist","Learn a magic trick","Read about a historical event","Write a blog post","Call mom","Plan a weekend getaway","Practice playing the guitar","Research healthy recipes","Attend a yoga class","Prepare for a job interview","Visit the art museum",'Hair Cut','Career Networking','Parenting Tasks','DIY Repairs','Pet Care','Language Learning','Sketching','One Hour on Personal Project','Travel Planning','Meal Planning','Health Tracking','Renewals and Subscriptions','Meditation','Playing Badminton', 'Visit Dmart','Study SQL','Read Novel','Gratitude Journaling','Speak to an Old Friend','Laundary','Gym Workout', 'Groceries','Meeting','Learn Vocab','Watch Lectures','Morning Walk','Learn a Dish','Do the Dishes','Water can order','Doing Chores','Gardening','Bike Service','Mobile Repair','To Do list','Taking Naps']
    # from random import randint
    # y=2020
    # m=[1,3,5,7,8,10,12]
    # d=31
    # m=[4,6,9,11]
    # d=30
    # m=[2]
    # d=29
    # for k in m:
    #     for i in range(1,d+1):
    #         tn=randint(2,8)
    #         for j in range(tn):
    #             dtask=activity.objects.filter(year=y,month=k,day=i)
    #             nl=len(dtask)+1
    #             tr=randint(0,99)
    #             tsk=tl[tr]
    #             ts=randint(0,1)
    #             tsl=[True,False]
    #             tj=activity(order=nl,task=tsk,status=tsl[ts],year=y,month=k,day=i)
    #             tj.save()
    return render(request, 'staticpage.html')

def dayd(request):
    form=addtaskform()
    from datetime import datetime
    dt=datetime.now().date()
    d=str(dt)
    return HttpResponseRedirect(reverse('day',args=[d]))

def day(request,d):
    from datetime import datetime,timedelta
    dt=datetime.strptime(d,'%Y-%m-%d').date()
    y=dt.year
    m=dt.month
    da=dt.day
    dtask=activity.objects.filter(year=y,month=m,day=da).order_by('order')

    weekdate=[]
    for i in range(-3,4):
        if i<0:
            dti=dt-timedelta(days=(i*-1))
            weekdate.append(dti)
        elif i>0:
            dti=dt+timedelta(days=(i))
            weekdate.append(dti)
        else:
            weekdate.append(dt)
    form1=addtaskform()
    dt2=dt.strftime('%d-%m-%Y')
    day=wday[dt.weekday()]
    return render(request,'day.html', {'day_task':dtask,'date':d,'date2':dt2,'day':day,'weekdate':weekdate,'form':form1})


def add(request,d):
    from datetime import datetime
    dt=datetime.strptime(d,'%Y-%m-%d').date()
    y=dt.year
    m=dt.month
    da=dt.day
    dtask=activity.objects.filter(year=y,month=m,day=da)
    nl=dtask.count()+1
    if request.method=='POST':
        form =addtaskform(request.POST)
        if form.is_valid():
            fd=form.cleaned_data
            a=activity(order=nl,task=fd['activity'],year=y,month=m,day=da)
            a.save()
        return HttpResponseRedirect(reverse('day',args=[d]))

def delete(request,d,t):
    if request.method=='POST':
        from datetime import datetime
        dt=datetime.strptime(d,'%Y-%m-%d').date()
        y=dt.year
        m=dt.month
        da=dt.day
        dtask=activity.objects.filter(year=y,month=m,day=da)
        nl=dtask.count()
        taskt=activity.objects.get(year=y,month=m,day=da,task=t)
        on=taskt.order
        taskt.delete()
        if on<nl:
            for i in dtask:
                if i.order>on:
                    i.order-=1
                    i.save()
        return HttpResponseRedirect(reverse('day',args=[d]))
    
def up(request,d,o):
    if request.method=='POST':
        from datetime import datetime
        dt=datetime.strptime(d,'%Y-%m-%d').date()
        y=dt.year
        m=dt.month
        da=dt.day
        
        if o!=1:
            
            taskt1=activity.objects.get(year=y,month=m,day=da,order=o)
            taskt2=activity.objects.get(year=y,month=m,day=da,order=(o-1))
            taskt1.order=o-1
            taskt1.save()
            taskt2.order=o
            taskt2.save()
            
        return HttpResponseRedirect(reverse('day',args=[d]))
 
def down(request,d,o):
    if request.method=='POST':
        from datetime import datetime
        dt=datetime.strptime(d,'%Y-%m-%d').date()
        y=dt.year
        m=dt.month
        da=dt.day
        dtask=activity.objects.filter(year=y,month=m,day=da)
        nl=dtask.count()
        if o!=nl:
            
            taskt1=activity.objects.get(year=y,month=m,day=da,order=o)
            taskt2=activity.objects.get(year=y,month=m,day=da,order=(o+1))
            taskt1.order=o+1
            taskt1.save()
            taskt2.order=o
            taskt2.save()
            
        return HttpResponseRedirect(reverse('day',args=[d]))   





def edit1(request,d,o):
    from datetime import datetime
    dt=datetime.strptime(d,'%Y-%m-%d').date()
    y=dt.year
    m=dt.month
    da=dt.day
    dtask=activity.objects.filter(year=y,month=m,day=da).order_by('order')
    dtask1=[]
    dtask2=[]
    for i in dtask:
        if i.order<o:
            dtask1.append(i)
        elif i.order>o:
            dtask2.append(i)
        else:
            et=i

    form1=addtaskform()
    forme=edittaskform(initial={'activity':et.task,'st':et.status})
    
    return render(request,'dayedit.html', {'day_task1':dtask1,'day_task2':dtask2,'et':et,'date':d,'form':form1,'et':et,'o':o,'forme':forme})


def edit2(request,d,o):
    from datetime import datetime
    dt=datetime.strptime(d,'%Y-%m-%d').date()
    y=dt.year
    m=dt.month
    da=dt.day
    etask=activity.objects.get(year=y,month=m,day=da,order=o)
    if request.method=='POST':
        form =edittaskform(request.POST)
        if form.is_valid():
            fd=form.cleaned_data
            etask.task=fd['activity']
            etask.status=fd['st']
            etask.save()
        return HttpResponseRedirect(reverse('day',args=[d]))


# def monthd(request):
    
#     from datetime import datetime
#     dt=datetime.now().date()
#     y=dt.year
#     m=dt.month
#     #form=yearmonthform()
#     return HttpResponseRedirect(reverse('month',args=[y,m]))


def leap(y):
        if y%4==0:
            if y%100==0:
                if y%400==0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def graph(m,y,d,td,tt):
    import time
    # Create the graph using Matplotlib
    x = d
    y1 =td
    y2=tt
    plt.plot(x, y1,color='green', label='Tasks Completed')
    plt.plot(x, y2,color='blue', label='Total Task')
    plt.xlabel('Days')
    plt.ylabel('Number of Task')

    plt.xticks([i for i in range(1,len(x)+1,3)])

    # Set y-axis ticks as integers
    plt.yticks(range(int(min(y1 + y2)), int(max(y1 + y2)) + 1))

    plt.legend()
    plt.title(f'Performance Graph for {m} {y}') 

    #destination_path = f'C:/Users/Vatsal_Fast/Desktop/ToDolist/todolist/plot/{m}{y}.png'  
    # plt.savefig(destination_path)
    # time.sleep(2)
    # plt.close()
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()

    # Convert the figure to a base64-encoded image string
    buffer.seek(0)
    fig = base64.b64encode(buffer.read()).decode()

    
    
    return fig



def month(request):
    from datetime import datetime
    if request.method=='POST':
        form =yearmonthform(request.POST)
        
        if form.is_valid():
            fd=form.cleaned_data
            
            ms=fd['m']
            m = datetime.strptime(ms,"%B").month
            y=fd['y']
            month=['January','February','March','April','May','June','July','August','September','October','November','December']
            mnum={month[i]:i+1 for i in range(12)}
            monthday={('January','March','May','July','August','October','December'):31,
                    ('April','June','September','November'):30,
                    ('February'):28}
            #mn=mnum[m.lower()]
            md=0

            if ms=='February':
                monthday[('February')]=leap(int(y))

            for i in monthday:
                if ms in i:
                    md=monthday[i]
            tasksummary={}
            dm=[]
            td=[]
            tt=[]

            for i in range(2,md+1):
                mdtaskt=activity.objects.filter(year=y,month=m,day=i,status=True).count()
                mdtaskf=activity.objects.filter(year=y,month=m,day=i,status=False).count()
                # di=str(y)+'-'+str(m)+'-'+str(i)
                # mddate=datetime.strptime(di,'%Y-%m-%d').date()
                # mddate=str(mddate)
                tasksummary[i]=[mdtaskt,(mdtaskf+mdtaskt)]
                dm+=[i]
                td+=[mdtaskt]
                tt+=[mdtaskf+mdtaskt]
            dl=list(range(md))
            formmy=yearmonthform(initial={'m':ms,'y':y})
            fig=graph(ms,y,dm,td,tt)
            return render(request,'month.html', {'figure':fig,'dl':dl,'dm':dm,'td':td,'tt':tt,'month_task_summary':tasksummary,'month':m,'months':ms,'year':y,'monthday':md,'formmy':formmy})


        # else:
        #     dt=datetime.now().date()
        #     y=dt.year
        #     m=dt.month
        #     ms=dt.strftime('%B')
    
    dt=datetime.now().date()
    y=dt.year
    m=dt.month
    ms=dt.strftime('%B')

    from datetime import datetime,timedelta
    d=str(y)+'-'+str(m)+'-'+'01'
    dt=datetime.strptime(d,'%Y-%m-%d').date()
    if m==12:
        md=31
    else:
        d2=str(y)+'-'+str(m+1)+'-'+'01'
        dt2=datetime.strptime(d,'%Y-%m-%d').date()
        dti=dt2-timedelta(days=(1))
        md=dti.day

    tasksummary={}
    dm=[]
    td=[]
    tt=[]


    for i in range(1,md+1):
        mdtaskt=activity.objects.filter(year=y,month=m,day=i,status=True).count()
        mdtaskf=activity.objects.filter(year=y,month=m,day=i,status=False).count()
        tasksummary[i]=[mdtaskt,(mdtaskf+mdtaskt)]
        dm+=[i]
        td+=[mdtaskt]
        tt+=[mdtaskf+mdtaskt]
    fig=graph(ms,y,dm,td,tt)
    formmy=yearmonthform(initial={'m':ms,'y':y})
    return render(request,'month.html', {'figure':fig,'month_task_summary':tasksummary,'date':d,'month':m,'months':ms,'year':y,'monthday':md,'formmy':formmy})


def daym(request,k,m,y):

    from datetime import datetime
    d=str(y)+'-'+str(m)+'-'+str(k)
    dt=datetime.strptime(d,'%Y-%m-%d').date()
    d=str(dt)
    return HttpResponseRedirect(reverse('day',args=[d]))



tl=['Hair Cut','Meditation','Study ML','New Skill Development','Study Maths','Playing Badminton','Study Latest Research', 'Visit Dmart','Study Python','Study SQL','Read Novel','Gratitude Journaling','Speak to an Old Friend','Laundary','Gym Workout', 'Groceries','Meeting','Learn Vocab','Watch Lectures','Morning Walk','Learn a Dish','Do the Dishes','Water can order','Doing Chores','Gardening','Bike Service','Mobile Repair','To Do list','Taking Naps','Beard Setting',"Create a budget for the month","Organize a closet","Watch a classic movie","Research online courses","Schedule a doctor's appointment", "Write thank-you notes","Clean out the refrigerator","Take the dog for a walk","Try a new restaurant","Watch a documentary","Visit a local farmers market","Plan a surprise date night","Organize a game night with friends","Learn a new dance routine","Explore a nearby hiking trail","Donate clothes to a charity","Write a business proposal","Start a collection of something","Create a vision board","Plan a picnic in the park","Volunteer at a local shelter","Declutter your email inbox","Watch a TED talk","Plan a virtual hangout with friends","Create a workout playlist","Learn a magic trick","Read about a historical event","Write a blog post","Call mom","Plan a weekend getaway","Practice playing the guitar","Research healthy recipes","Attend a yoga class","Prepare for a job interview","Visit the art museum",'Hair Cut','Career Networking','Parenting Tasks','DIY Repairs','Pet Care','Language Learning','Sketching','One Hour on Personal Project','Travel Planning','Meal Planning','Health Tracking','Renewals and Subscriptions','Meditation','Playing Badminton', 'Visit Dmart','Study SQL','Read Novel','Gratitude Journaling','Speak to an Old Friend','Laundary','Gym Workout', 'Groceries','Meeting','Learn Vocab','Watch Lectures','Morning Walk','Learn a Dish','Do the Dishes','Water can order','Doing Chores','Gardening','Bike Service','Mobile Repair','To Do list','Taking Naps']

