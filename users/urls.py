from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^admindex', views.admindex, name='admindex'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register1'),
    url(r'^register1', views.register1, name='register2'),
    url(r'^user_login/$', views.user_login, name='userlogin'),
    url(r'^user_register', views.user_register, name='userregister'),
    url(r'^staffreg', views.staffreg, name='staffregister'),
    url(r'^pnrupdate', views.pnrupdate, name='pnrupdate'),
    url(r'^updatefeedback', views.updatefeedback, name='updatefeedback'),
    url(r'^payment', views.payment, name='payments'),
    url(r'^feedback', views.feedback, name='feedbackview'),
    url(r'^customer_support', views.customer_support, name='support'),
    url(r'^accommodation', views.accommodation, name='accommodation'),
    url(r'^visa', views.visa, name='visa'),
    url(r'^resetpass', views.reset, name='resetpassword'),
    url(r'^updatenumber', views.updatenumber, name='updatenumber'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^logoutuser', views.logoutuser, name='logoutuser'),
    url(r'^blockuser', views.block, name='block'),
    url(r'^tripplan', views.updateplan, name='tripplan'),
    url(r'^viewdetails', views.details, name='details'),

]
