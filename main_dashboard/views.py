
from django.shortcuts import render,redirect
from .models import Grant,Activity,ActivityType
import pandas as pd
import datetime
from . forms import CreateProjectForm
import plotly.express as px
import plotly.graph_objects as go

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%Y-%m-%d")
d2 = today.strftime("%Y-%m")
year=today.strftime("%Y")
month= today.strftime("%m")
year= float(year)
month= float(month)
current_year_month=round(month/12,3)+year

def progress(col):
    if col< current_year_month:
        return 'Completed'
    elif col == current_year_month:
        return 'To be completed this month'
    else:
        return 'In Progress'


def comp(col):
    if col >100:
        return 100
    else:
        return col
# Create your views here.def \
def home(request):
    graph_grants()
    graph_all_activities()
    participant_detail()
    

    # date for this month
    today = date.today()
    d2 = today.strftime("%Y-%m")

    global total_grants,total_completed,total_in_progress,total_to_be,graph_trend,graph_activity,graph_org
    global com_len,ong_len,soon_len,total_activivity

    context={
        'total_grants':total_grants,
        'total_completed':total_completed,
        'total_in_progress':total_in_progress,
        'total_to_be':total_to_be,
        'month_year':d2,
        'graph_activity':graph_activity,
        'graph_trend':graph_trend,
        'graph_organization':graph_org,
        'activity_completed':com_len,
        'activity_starting_soon':soon_len,
        'activity_ongoing':ong_len,
        'total_activity':total_activivity
    }
    return render(request,'home.html',context)

def grant( request):
    global df1
    all_grants=Grant.objects.all()
    grants=Grant.objects.all().values()

    df= pd.DataFrame(grants)

    

    return render(request,'grants/grant.html', {'df':df.to_html,'all_grants':all_grants })
   

def register_project(request):
    forms=CreateProjectForm
    if request.method== 'POST':
        forms=CreateProjectForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        
    else:

        forms=CreateProjectForm()
    context={
        'forms':forms,
        
    }
    return render(request,'grants/add_grants.html',context)

def update_grants(request,grant_id):
    grants=Grant.objects.get(pk=grant_id) 
    forms=CreateProjectForm(instance=grants)
    if request.method=='POST':
        forms=CreateProjectForm(request.POST,request.FILES,instance=grants)
        if forms.is_valid():
            forms.save()
            return redirect('submitted')  
    return render(request,'grants/update_grants.html',{'grants':grants,'forms':forms})

def submisionform(request):
    return render(request,'grants/submit.html',{})


def graph_grants():
    global graph_compl,graph_all,graph_pro,total_completed,total_grants,total_in_progress,graph_to_be,total_to_be,graph_trend
    grants=Grant.objects.all().values()

    df= pd.DataFrame(grants)

    # working on years and months
   

    df['year_start']= df['project_start'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'([0-9]{4})\S[0-9]{2}\S[0-9]{2}')
    df['month_start']= df['project_start'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'[0-9]{4}\S([0-9]{2})\S[0-9]{2}')
    df['year_end']= df['project_end'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'([0-9]{4})\S[0-9]{2}\S[0-9]{2}')
    df['month_end'] = df['project_end'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'[0-9]{4}\S([0-9]{2})\S[0-9]{2}')

    df['year_start']=df['year_start'].astype(int)
    df['month_start']=df['month_start'].astype(float)
    df['year_end']=df['year_end'].astype(float)
    df['month_end']=df['month_end'].astype(float)
    df['year_month_start']=round(df['month_start']/12,3) + df['year_start']
    df['year_month_end']=round(df['month_end']/12,3) + df['year_end']


    df['Progress'] = df['year_month_end'].apply(progress)
    df['completion_todate'] = current_year_month-df['year_month_start']
    df['total_time'] = df['year_month_end']-df['year_month_start']
    df['completion'] = round((df['completion_todate']/df['total_time'])*100,2)
    df['completion'] = df['completion'].apply(comp)
    df['Duration(in months)'] = round(df['total_time']*12)

    # TREND
    df['number of Projects'] =int(len(df['project_name'])/int(df.shape[0]))
    df_year=df[['year_start','number of Projects']]
    df_year['year-start']=df_year['year_start'].astype(int)
    df_year=df_year.groupby('year_start').sum()
    df_year=df_year.reset_index()

    fig = px.line(df_year, x="year_start", y="number of Projects", text="number of Projects",
              title='Number of projects acquired per year', height=240)
    fig.update_traces(textposition="bottom center" ,textfont_size=10)
    graph_trend=fig.to_html(full_html=False)
    
    #graph all
    df.sort_values('year_month_start',ascending=False,inplace=True)
    fig_compl = px.timeline(df, x_start="project_start", x_end="project_end", y="project_name", color="Progress")
    fig_compl.update_yaxes(autorange="reversed")
    fig_compl.update_yaxes(automargin=True)
    graph_all=fig_compl.to_html(full_html=False)
    total_grants=len(df)

    # graph in progress
    df_pro=df[df['Progress'] =='In Progress']
    df_pro.sort_values('year_month_start',ascending=False,inplace=True)
    fig_compl = px.timeline(df_pro, x_start="project_start", x_end="project_end", y="project_name", color="Progress")
    fig_compl.update_yaxes(autorange="reversed")
    fig_compl.update_yaxes(automargin=True)
    graph_pro=fig_compl.to_html(full_html=False)
    total_in_progress=len(df_pro)

    # to be completed this month
    df_pro=df[df['Progress'] =='To be completed this month']
    df_pro.sort_values('year_month_start',ascending=False,inplace=True)
    fig_compl = px.timeline(df_pro, x_start="project_start", x_end="project_end", y="project_name", color="Progress")
    fig_compl.update_yaxes(autorange="reversed")
    fig_compl.update_yaxes(automargin=True)
    graph_to_be=fig_compl.to_html(full_html=False)
    total_to_be=len(df_pro)

    
    # completed
    df_compl=df[df['Progress']=='Completed']
    df_compl.sort_values('completion',ascending=False,inplace=True)
    fig_compl = px.timeline(df_compl, x_start="project_start", x_end="project_end", y="project_name", color="completion")
    fig_compl.update_yaxes(autorange="reversed")
    fig_compl.update_yaxes(automargin=True)
    graph_compl=fig_compl.to_html(full_html=False)
    total_completed=len(df_compl)
   
    


def grant_completed(request):
    global graph_compl,total_completed
    return render(request,'grants/graph/completed.html',{'graph_compl':graph_compl,'total_completed':total_completed})

def grant_progress(request):
    global graph_pro,total_in_progress
    return render(request,'grants/graph/progress.html',{'graph_pro':graph_pro,'total_in_progress':total_in_progress})

def graph_all_grants(request):
    global graph_all,total_grants
    return render(request,'grants/graph/all.html',{'graph_all':graph_all,'total_grants':total_grants})

def graph_to_complete(request):
    today = date.today()
    d2 = today.strftime("%Y-%m")
    global graph_to_be,total_to_be
    return render(request,'grants/graph/to_be.html',{'graph_to_be':graph_to_be,'total_to_be':total_to_be,'month_year':d2})



def activity_status(col):
    if col<0.0:
        return 'Starting Soon'
    elif  (col>=0.0)and(col<1.0):
        return 'Ongoing'
    else:
        return 'Completed'




def graph_all_activities():
    global activity_completed,activity_starting_soon,activity_ongoing
    global graph_activity,com_len,soon_len,ong_len,total_activivity
    today = date.today()
    time_now = today.strftime("%Y%m%d")
    all_activity=Activity.objects.all().values()
    df_activity= pd.DataFrame(all_activity)
    df_activity['duration']=df_activity['date_end'].apply(lambda x: x.strftime("%Y%m%d")).astype(float)-df_activity['date_start'].apply(lambda x: x.strftime("%Y%m%d")).astype(float)
    df_activity['to_date']=float(time_now)-df_activity['date_start'].apply(lambda x: x.strftime("%Y%m%d")).astype(float)
    df_activity['ratio']=round(df_activity['to_date']/df_activity['duration'],2)
    df_activity['status']=df_activity['ratio'].apply(activity_status)
    print(df_activity)

    activity_ongoing=df_activity[df_activity['status']=='Ongoing']
    activity_completed=df_activity[df_activity['status']=='Completed']
    activity_starting_soon=df_activity[df_activity['status']=='Starting Soon']

    total_activivity=len(df_activity)
    ong_len=len(activity_ongoing)
    com_len=len(activity_completed)
    soon_len=len(activity_starting_soon)
 

    labels = ['Training','Meetings','Workshop']
    values = [20, 5, 3]
    # pull is given as a fraction of the pie radius
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0.2, 0.2, 0.2,])])
    fig.update_layout(height=240,title='Number of activities conducted')
    graph_activity=fig.to_html(full_html=False)

def ongoing_activities(request):
    today = date.today()
    time_now = today.strftime("%Y-%m-%d %H:%M:%S")
    ongoing_act=Activity.objects.filter(date_start__lte=time_now).filter(date_end__gte=time_now)
    return render(request,'activities/ongoing.html',{'ongoings':ongoing_act})
def completed_activities(request):
    today = date.today()
    time_now = today.strftime("%Y-%m-%d %H:%M:%S")
    completed_act=Activity.objects.filter(date_end__lt=time_now)
    return render(request,'activities/completed.html',{'completed':completed_act})
def starting_activities(request):
    today = date.today()
    time_now = today.strftime("%Y-%m-%d %H:%M:%S")
    starting_act=Activity.objects.filter(date_start__gt=time_now)
    return render(request,'activities/starting.html',{'starting':starting_act})
def activity_countdown(request,activity_id):
    today = date.today()
    time_now = today.strftime("%Y-%m-%d %H:%M:%S")
    countdown_act=Activity.objects.filter(date_start__gt=time_now)
    countdown_act=Activity.objects.get(pk=activity_id)
  
    return render(request,'activities/countdown.html',{'countdown_act':countdown_act})



def participant_detail():
    global graph_org
    dummy_list=[
        ['NGOs',8],
        ['CBOs',4],
        ['Law Firms',5],
        ['Hospitals',6],
    ]
    dummy_data=pd.DataFrame(dummy_list,columns=['Organization','Number'])
    fig = px.bar(dummy_data, x='Organization', y='Number')
    fig.update_layout(height=240,title='Organization Reached')
    graph_org=fig.to_html(full_html=False)



   