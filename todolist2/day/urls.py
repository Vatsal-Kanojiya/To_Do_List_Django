
from django.urls import path
from . import views



urlpatterns=[
    path('staticpage',views.staticpage,name='staticpage'),
    path('',views.dayd,name='dayn'),
    path('day/<str:d>',views.day,name='day'),
    path('add/<str:d>',views.add,name='add'),
    path('delete/<str:d>/<str:t>',views.delete,name='delete'),
    path('up/<str:d>/<int:o>',views.up,name='up'),
    path('down/<str:d>/<int:o>',views.down,name='down'),
    path('edit1/<str:d>/<int:o>',views.edit1,name='edit1'),
    path('edit2/<str:d>/<int:o>',views.edit2,name='edit2'),

    # path('month/',views.monthd,name='monthn'),
    path('day/<int:k>/<int:m>/<int:y>',views.daym,name='daym'),
    path('month/',views.month,name='month'),

    #path('perf/<str:d>',views.perfw,name='perfw'),
    #path('perf/<str:d>',views.perfm,name='perfm'),
]
    


