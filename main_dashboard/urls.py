
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('grants', views.grant,name='grant'),
    path('add-grants', views.register_project,name='add-grant'),
    path('update-grants/<grant_id>', views.update_grants,name='update-grant'),
    path('submitted', views.submisionform,name='submitted'),
    path('graph-complete', views.grant_completed,name='completed'),
    path('graph-progress', views.grant_progress,name='progress'),
    path('graph-all', views.graph_all_grants,name='graph-all'),
    path('graph-to-be',views.graph_to_complete,name='graph-to-be'),
    path('activity-ongoing',views.ongoing_activities,name='activity-ongoing'),
    path('activity-completed',views.completed_activities,name='activity-completed'),
    path('activity-starting',views.starting_activities,name='activity-starting'),
    path('starting/<activity_id>',views.activity_countdown,name='activity-countdown')
   
   
]