from django.db import models


# Create your models here.


class userdata(models.Model):
    first_name = models.TextField(max_length=20, null=True, blank=True)
    last_name = models.TextField(max_length=20, null=True, blank=True)
    passport_number = models.CharField(max_length=6, null=True, blank=True)
    mother_name = models.TextField(max_length=30, null=True, blank=True)
    father_name = models.TextField(max_length=30, null=True, blank=True)
    mother_passport_number = models.CharField(max_length=6, null=True, blank=True)
    father_passport_number = models.CharField(max_length=6, null=True, blank=True)
    date_of_birth = models.TextField(max_length=10, null=True, blank=True)
    place_of_birth = models.TextField(max_length=100, null=True, blank=True)
    residential_address = models.TextField(max_length=100, null=True, blank=True)
    permanent_address = models.TextField(max_length=100, null=True, blank=True)
    gender = models.TextField(max_length=6, null=True, blank=True)
    email = models.TextField(max_length=50, null=True, blank=True)
    phone_number = models.TextField(max_length=10, null=True, blank=True)
    alternate_phone_number = models.TextField(max_length=10, null=True, blank=True)
    batch_number = models.TextField(max_length=10, null=True, blank=True)
    file_upload = models.ImageField(upload_to='media/passport/', null=True, blank=True)


class clientlogin(models.Model):
    mobile_number = models.CharField(max_length=10, null=True, blank=True)
    one_time_password = models.CharField(max_length=6, null=True, blank=True)
    passportnumber = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)


class staffregistration(models.Model):
    staff_id = models.CharField(max_length=6, null=True, blank=True)
    first_name = models.TextField(max_length=20, null=True, blank=True)
    last_name = models.TextField(max_length=20, null=True, blank=True)
    date_of_birth = models.TextField(max_length=10, null=True, blank=True)
    gender = models.TextField(max_length=6, null=True, blank=True)
    contact_number = models.TextField(max_length=10, null=True, blank=True)
    alternate_contact_number = models.TextField(max_length=10, null=True, blank=True)
    email_id = models.TextField(max_length=30, null=True, blank=True)
    residential_address = models.TextField(max_length=100, null=True, blank=True)
    permanent_address = models.TextField(max_length=100, null=True, blank=True)
    otp = models.TextField(max_length=32, null=True, blank=True)


class stafflogin(models.Model):
    user_id = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=6, null=True, blank=True)
    designation= models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)


class modification(models.Model):
    staff_id = models.CharField(max_length=6, null=True, blank=True)
    client_id = models.CharField(max_length=6, null=True, blank=True)
    passport_number = models.CharField(max_length=6, null=True, blank=True)
    action_done = models.TextField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(max_length=20, null=True, blank=True)


class feedback(models.Model):
    name = models.TextField(max_length=20, null=True, blank=True)
    email = models.TextField(max_length=30, null=True, blank=True)
    comment = models.TextField(max_length=300, null=True, blank=True)


class pnrstatus(models.Model):
    passport_number = models.CharField(max_length=6, null=True, blank=True)
    pnrno = models.CharField(max_length=8, null=True, blank=True)
    ticket_number = models.CharField(max_length=15, null=True, blank=True)


class customersupport(models.Model):
    name = models.TextField(max_length=20, null=True, blank=True)
    email = models.TextField(max_length=30, null=True, blank=True)
    message = models.TextField(max_length=300, null=True, blank=True)
    status = models.TextField(max_length=10, null=True, blank=True)


class payments(models.Model):
    passport_number = models.TextField(max_length=6, null=True, blank=True)
    cheque_number = models.TextField(max_length=30, null=True, blank=True)
    bank_name = models.TextField(max_length=30, null=True, blank=True)
    branch_name = models.TextField(max_length=30, null=True, blank=True)
    net_amount = models.TextField(max_length=10, null=True, blank=True)
    date = models.DateTimeField(max_length=20, null=True, blank=True)


class accomodation(models.Model):
    batch_number = models.TextField(max_length=6, null=True, blank=True)
    file_upload = models.ImageField(upload_to='accomodation/', null=True, blank=True)


class visadetails(models.Model):
    passport_number = models.CharField(max_length=6, null=True, blank=True)
    application_number = models.CharField(max_length=14, null=True, blank=True)
    file_upload = models.ImageField(upload_to='visa/', null=True, blank=True)


class passwordset(models.Model):
    staffid = models.CharField(max_length=6, null=True, blank=True)
    security_question = models.CharField(max_length=100, null=True, blank=True)
    answer = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)


class tripplan(models.Model):
    tripid = models.CharField(max_length=6, null=True, blank=True)
    batch = models.CharField(max_length=6, null=True, blank=True)
    designation = models.CharField(max_length=70, null=True, blank=True)
    year = models.CharField(max_length=6, null=True, blank=True)


