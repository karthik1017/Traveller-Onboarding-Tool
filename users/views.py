from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.contrib.sessions.models import Session
from users.models import *


def index(request):
    try:
        # if bool(stafflogin.objects.filter(user_id=request.session['uid'])):
        return render(request, 'users/index.html')
    # else:
    #     return redirect("users:login")
    except:
        return redirect("users:login")


def admindex(request):
    try:
        # if bool(stafflogin.objects.filter(user_id=request.session['uid'])):
        return render(request, 'users/admindex.html')
    # else:
    #     return redirect("users:login")
    except:
        return redirect("users:login")


def user_login(request):
    Session.objects.all().delete()
    try:
        if request.method == 'POST':
            uname = request.POST.get('uname')
            otp = request.POST.get('otp')
            db = clientlogin.objects.filter(mobile_number=uname, one_time_password=otp)
            db1 = clientlogin.objects.get(mobile_number=uname, one_time_password=otp)
            if bool(db):
                request.session['uid'] = db1.passportnumber
                return redirect("users:userregister")
            else:
                return render(request, 'users/userlogin.html', {'error': 'Invalid Login Credentials'})
        else:
            return render(request, 'users/userlogin.html')
    except:
        return render(request, 'users/userlogin.html', {'error': 'Invalid Login Credentials'})


def login(request):
    try:
        if request.method == 'POST':
            uname = request.POST.get('uname')
            password = request.POST.get('pwd')
            if bool(stafflogin.objects.filter(user_id=uname, password=password, status='Active', designation='staff')):
                return redirect("users:index")
            elif bool(
                    stafflogin.objects.filter(user_id=uname, password=password, status='Active', designation='admin')):
                return redirect("users:admindex")
            else:
                return render(request, 'users/stafflogin.html', {'error': 'Invalid Login Credentials'})
        else:
            return render(request, 'users/stafflogin.html')
    except:
        return render(request, 'users/stafflogin.html', {'error': 'Invalid Login Credentials'})


def register(request):
    # try:
    if request.method == 'POST':
        dbtable = userdata()
        dbtable.first_name = request.POST.get("fname", "")
        dbtable.last_name = request.POST.get("sname", "")
        dbtable.passport_number = request.POST.get("pno", "")
        dbtable.mother_name = request.POST.get("moname", "")
        dbtable.father_name = request.POST.get("faname", "")
        dbtable.mother_passport_number = request.POST.get("mpno", "")
        dbtable.father_passport_number = request.POST.get("fpno", "")
        dbtable.date_of_birth = request.POST.get("dob", "")
        dbtable.place_of_birth = request.POST.get("pob", "")
        dbtable.residential_address = request.POST.get("radd", "")
        dbtable.permanent_address = request.POST.get("padd", "")
        dbtable.gender = request.POST.get("gender", "")
        dbtable.email = request.POST.get("email", "")
        dbtable.phone_number = request.POST.get("pnumber", "")
        dbtable.alternate_phone_number = request.POST.get("anumber", "")
        dbtable.batch_number = request.POST.get("bnumber", "")
        img = request.POST.get("file", "")
        dbtable.file_upload = img
        if bool(userdata.objects.filter(passport_number=request.POST.get("pno", ""))):
            return render(request, 'users/register.html', {'error': 'user Already Exists'})
        dbtable.save()
        return render(request, 'users/register.html')
    else:
        # if bool(stafflogin.objects.filter(user_id=request.session['uid'])):
        return render(request, 'users/register.html')
        # pass
    # else:
    #     return redirect("users:login")


# except:
#     return redirect("users:login")
#     pass


def user_register(request):
    if request.method == 'POST':
        dbtable = userdata()
        dbtable.passport_number = request.POST.get("pno", "")
        dbtable.first_name = request.POST.get("fname", "")
        dbtable.last_name = request.POST.get("sname", "")
        dbtable.mother_name = request.POST.get("moname", "")
        dbtable.father_name = request.POST.get("faname", "")
        dbtable.father_passport_number = request.POST.get("fpno", "")
        dbtable.mother_passport_number = request.POST.get("mpno", "")
        dbtable.date_of_birth = request.POST.get("dob", "")
        dbtable.place_of_birth = request.POST.get("pob", "")
        dbtable.residential_address = request.POST.get("radd", "")
        dbtable.permanent_address = request.POST.get("padd", "")
        dbtable.phone_number = request.POST.get("pnumber", "")
        dbtable.alternate_phone_number = request.POST.get("anumber", "")
        dbtable.batch_number = request.POST.get("batch", "")
        dbtable.gender = request.POST.get("gender", "")
        dbtable.email = request.POST.get("email", "")
        dbtable.file_upload = request.POST.get("file", "")
        if bool(userdata.objects.filter(passport_number=request.POST.get("pno", ""))):
            return render(request, 'users/userregister.html', {'error': 'user Already Exists'})
        dbtable.save()
        return redirect("users:userregister")
    else:
        return render(request, 'users/userregister.html')


def staffreg(request):
    if request.method == 'POST':
        if bool(staffregistration.objects.filter(staff_id=request.POST.get("staff", ""))):
            return render(request, 'users/adminregister.html', {'error': 'Staff Already Exists'})
        # pass
        else:
            dbtable = staffregistration()
            dbtable.staff_id = request.POST.get("staff", "")
            dbtable.first_name = request.POST.get("first name", "")
            dbtable.last_name = request.POST.get("lname", "")
            dbtable.date_of_birth = request.POST.get("dob", "")
            dbtable.gender = request.POST.get("gender", "")
            dbtable.contact_number = request.POST.get("contact_number", "")
            dbtable.alternate_contact_number = request.POST.get("alternate_contact_number", "")
            to = request.POST.get("email_id", "")
            dbtable.residential_address = request.POST.get("residential_address", "")
            dbtable.permanent_address = request.POST.get("permanent_address", "")
            dbtable.email_id = to
            code = get_random_string(length=32)
            dbtable.otp = code
            # message = "http://127.0.0.1:8000/users/resetpass?email=" + to + "&rand=" + code
            # res = send_mail("Passwordreset", message, "TOT@Jagli.com", [to])
            # return HttpResponse('%s' % res)
            # if bool(userdata.objects.filter(passport_number=request.POST.get("pno", ""))):
            dbtable.save()
            dbtable = stafflogin()
            dbtable.user_id = to
            dbtable.password = request.POST.get("pwd", "")
            dbtable.designation = "Staff"
            dbtable.status = "Active"
            dbtable.save()
            return render(request, 'users/adminregister.html')

    else:
        return render(request, 'users/adminregister.html')


def pnrupdate(request):
    if request.method == 'POST':
        dbtable = pnrstatus()
        dbtable.passport_number = request.POST.get("pkey", "")
        dbtable.pnrno = request.POST.get("cheque", "")
        dbtable.ticket_number = request.POST.get("bname", "")
        dbtable.save()
        return render(request, 'users/ticket.html')
    else:
        # if bool(stafflogin.objects.filter(user_id=request.session['uid'])):
        return render(request, 'users/ticket.html')
    # else:
    #     return redirect("users:login")


def updatefeedback(request):
    if request.method == 'POST':
        dbtable = feedback()
        dbtable.name = request.POST.get("name", "")
        dbtable.email_id = request.POST.get("mail", "")
        dbtable.comment = request.POST.get("comment", "")
        dbtable.save()
        pass
    else:
        return render(request, 'users/feedback.html')


def payment(request):
    if request.method == 'POST':
        dbtable = payments()
        dbtable.passport_number = request.POST.get("pkey", "")
        dbtable.cheque_number = request.POST.get("cheque", "")
        dbtable.bank_name = request.POST.get("bname", "")
        dbtable.branch_name = request.POST.get("Bname", "")
        dbtable.net_amount = request.POST.get("amt", "")
        dbtable.date = request.POST.get("date", "")
        dbtable.save()
        return render(request, 'users/payments.html')
        pass
    else:
        # if bool(stafflogin.objects.filter(user_id=request.session['uid'])):
        return render(request, 'users/payments.html')
        # pass
    # else:
    #     return redirect("users:login")


def feedback(request):
    # method to load data
    return render(request, 'users/viewfeedback.html')


def register1(request):
    return render(request, 'users/register1.html')


def customer_support(request):
    # data = userdata.objects.get(passport_number=request.session['uid'])
    # ds = {"arr": data}
    return render(request, 'users/customer_support.html')


def visa(request):
    if request.method == 'POST':
        dbtable = visadetails()
        dbtable.passport_number = request.POST.get("pno", "")
        dbtable.application_number = request.POST.get("apno", "")
        dbtable.file_upload = request.POST.get("doc", "")
        dbtable.save()
        return render(request, 'users/visa.html')
        pass
    else:
        # if bool(stafflogin.objects.filter(user_id=request.session['uid'])):
        return render(request, 'users/visa.html')
        # pass
    # else:
    #     return redirect("users:login")


def accommodation(request):
    if request.method == 'POST':
        dbtable = accomodation()
        dbtable.batch_number = request.POST.get("pkey", "")
        dbtable.file_upload = request.POST.get("bname", "")
        dbtable.save()
        return redirect("users:accommodation")
    else:
        # if bool(stafflogin.objects.get(user_id=request.session['uid'])):
        return render(request, 'users/accommodation.html')
        # pass
    # else:
    #     return redirect("users:login")


mail = ""
otp = ""


def reset(request):
    return render(request, 'users/resetpass.html')


#     mail = request.GET.get("email")
#     otp = request.GET.get("rand")
#     if request.method == 'POST':
#         # return HttpResponse(mail)
#         if bool(staffregistration.objects.filter(email_id=mail, otp=otp)):
#             pas = request.POST.get("pwd", "")
#             conpas = request.POST.get("pwd1", "")
#             if bool(stafflogin.objects.filter(user_id=mail)):
#                 return render(request, 'users/stafflogin.html')
#                 pass
#             else:
#                 if pas == conpas:
#                     dbtable = stafflogin()
#                     dbtable.user_id = mail
#                     dbtable.password = pas
#                     dbtable.designation = "Staff"
#                     dbtable.status = "Active"
#                     dbtable.save()
#                     return HttpResponse("Submited")
#                 else:
#                     return render(request, 'users/hi.html')
#                     pass
#         else:
#             return HttpResponse('users/hi.html')
#             pass
#     else:
#         return render(request, 'users/resetpass.html')


def updatenumber(request):
    if request.method == 'POST':
        dbtable = clientlogin()
        number = request.POST.get("number")
        dbtable.mobile_number = number
        dbtable.one_time_password = get_random_string(length=6)
        dbtable.status = 'active'
        if bool(clientlogin.objects.filter(mobile_number=number)):
            return render_to_response('users/rigister.html')
            pass
        else:
            dbtable.save()
            return render(request, 'users/rigister.html')
            pass
    else:
        return render(request, 'users/rigister.html')


def logout(request):
    Session.objects.all().delete()
    return render(request, 'users/stafflogin.html')


def logoutuser(request):
    Session.objects.all().delete()
    return render(request, 'users/userlogin.html')


def block(request):
    if request.method == 'POST':
        if bool(userdata.objects.filter(passport_number=request.POST.get("pno", ""))):
            return render(request, 'users/blockuser.html', {'error': 'user not exists'})
        else:
            stafflogin.objects.filter(user_id=request.POST.get('sid')).update(status='Blocked')
            return render(request, 'users/blockuser.html')
    else:
        return render(request, 'users/blockuser.html')


def details(request):
    return render(request, 'users/viewdetails.html')


def updateplan(request):
    if request.method == 'POST':
        dbtable = tripplan()
        dbtable.tripid = request.POST.get("tid", "")
        dbtable.batch = request.POST.get("batch", "")
        dbtable.designation = request.POST.get("designation", "")
        dbtable.year = request.POST.get("year", "")
        dbtable.save()
        return redirect("users:tripplan")
    else:
        return render(request, 'users/tripplan.html')
