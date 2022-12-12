
from django.urls import path,include
from . import views

urlpatterns = [
   
   path('',views.home,name="home"),
   path("balance/",views.balance,name="balance"),
   path("transaction/",views.transaction,name="transaction"),
   path("pay/",views.pay,name="pay"),
   path("history/",views.history,name="pay"),



 
]
