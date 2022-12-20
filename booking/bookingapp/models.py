from django.db import models

# Create your models here.
class loginModel(models.Model):
    mobile = models.CharField(max_length=12)
    dateTime = models.DateTimeField()
    otp = models.CharField(max_length=10)


def __str__(self):
    return 'Mobile = {}, Time = {}, OTP = {}'.format(self.mobile, self.dateTime, self.otp)




class BookingSlot(models.Model):
    bsthh = models.IntegerField()
    bstmm = models.IntegerField()
    bethh = models.IntegerField()
    betmm = models.IntegerField()
    ppd = models.IntegerField()
    bstt = models.IntegerField()
    bett = models.IntegerField()
    totalslot = models.IntegerField()

def __str__(self):
    return "bsthh={0},bstmm={1},bethh={2},betmm={3},ppd={4},bstt={5},bett={6},totalslot={7}".format(self.bsthh,self.bstmm,self.bethh,self.betmm,self.ppd,self.bstt,self.bett,self.totalslot)



class PatientDetails(models.Model):
    patientname = models.CharField(max_length = 50)
    patientage = models.IntegerField()
    mobile = models.CharField(max_length = 12)
    gender = models.CharField(max_length = 10)
    address = models.CharField(max_length = 200)

