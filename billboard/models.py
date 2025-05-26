from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class AddPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="nouser")
    name=models.CharField("Advert name", max_length=50)
    desc=models.CharField("Description", max_length=150)
    opd=(
    ("1s","1s"),("2s","2s"),("3s","3s"),("4s","4s"),("5s","5s"),("6s","6s"),("7s","7s"),("8s","8s"),("9s","9s"),("10s","10s"),("11s","11s"),("12s","12s"),
    ("13s","13s"),("14s","14s"),("15s","15s"),("16s","16s"),("17s","17s"),("18s","18s"),("19s","19s"),("20s","20s"),("21s","21s"),("22s","22s"),("23s","23s"),
    ("24s","24s"),("25s","25s"),("26s","26s"),("27s","27s"),("28s","28s"),("29s","29s"),("30s","30s"),)
    time=models.CharField("Time Frame", max_length=150, choices=opd)
    opm=(
    ("Fade","Fade"),
    ("Cross Fade","Cross Fade"),
    ("Fade With Black","Fade With Black"),
    ("Fade With White","Fade With White"),
    ("Fade With Color","Fade With Color"),)
    plan=models.CharField("Advert Transition", max_length=150, choices=opm)
    date=models.DateField("start Date to Display Advert")
    opt=(
    ("Digital(Gantry)","Digital(Gantry)"),
    ("Digital(Mega Site)","Digital(Mega Site)"),
    ("Digital(Light Box)","Digital(Light Box)"),
    ("Digital(Unipole)","Digital(Unipole)"),
    ("Digital(Wall Drape)","Digital(Wall Drape)"),
    ("Digital(Roof Top)","Digital(Roof Top)"),
    ("Digital(Super 48 Sheet)","Digital(Super 48 Sheet)"),
    ("Traditional(Gantry)","Traditional(Gantry)"),
    ("Traditional(Mega Site)","Traditional(Mega Site)"),
    ("Traditional(Light Box)","Traditional(Light Box)"),
    ("Traditional(Unipole)","Traditional(Unipole)"),
    ("Traditional(Wall Drape)","Traditional(Wall Drape)"),
    ("Traditional(Roof Top)","Traditional(Roof Top)"),
    ("Traditional(Super 48 Sheet)","Traditional(Super 48 Sheet)"),)
    options=models.CharField("Type of Billboard", max_length=150, choices=opt)
    Sunday=models.BooleanField(default=False)
    Monday=models.BooleanField(default=False)
    Tuesday=models.BooleanField(default=False)
    Wednesday=models.BooleanField(default=False)
    Thursday=models.BooleanField(default=False)
    Friday=models.BooleanField(default=False)
    Saturday=models.BooleanField(default=False)
    image=models.ImageField("Select Advert Image to Upload", upload_to="")
    location=models.CharField("Location", max_length=150)
    created=models.DateTimeField(default=now, editable=False)
    updated=models.DateTimeField(default=now, editable=False)
    def __str__(self):
            return self.user.username
  
class Contact(models.Model):
    name=models.CharField("Full Name", max_length=50)
    email=models.CharField("Email", max_length=150)
    opt=(("Send me a brochure","Send me a brochure"),
    ("I want more details from Keesha Billboard","I want more details from Keesha Billboard"),
    ("I want to partner with Keesha Billboard","I want to partner with Keesha Billboard"),)
    options=models.CharField("Informations", max_length=150, choices=opt)
    info=models.TextField("More Information", max_length=150)
    created=models.DateTimeField(default=now, editable=False)
    updated=models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return self.name 

class Items(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="nouser")
    itemname=models.CharField("Product name", max_length=50)
    created=models.DateTimeField(default=now, editable=False)
    updated=models.DateTimeField(default=now, editable=False)
    def __str__(self):
            return self.itemname

class SetUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="nouser")
    compname=models.CharField("Company Name", max_length=50)
    compemail=models.CharField("Company Email", max_length=50, default='youremail@gmail.com')
    opta=(
    ("100000","100000"),
    ("200000","200000"),
    ("300000","300000"),
    )
    phone=models.CharField("Company Phone Number", max_length=150)
    pricing=models.CharField("Select Subscription Billings", max_length=150, choices=opta)
    created=models.DateTimeField(default=now, editable=False)
    updated=models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return self.user.username 

    