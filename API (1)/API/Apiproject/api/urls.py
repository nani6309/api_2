from django.urls import path
from Emp import views

urlpatterns=[
    path('view',views.getemp),
    path('add',views.addemp),
    path('addview',views.addview),
    # path('delete/<pk>', views.deleteEmployee),
    path('delete/<int:pk>', views.deleteEmployee)
]