from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
# from .import
# from . import models
from .models import loginModel, BookingSlot, PatientDetails
from . import utilities as ut
import pytz


# Create your views here.
def index(request):
    if request.GET:
        mobile = request.GET['mobile']
        getOtp = ut.generateOtp(5)
        # ut.mailSend()

        #Delete all previous mobile data
        # previous = \
        loginModel.objects.filter(mobile = mobile).delete()
        # if previous != 0:
        #     previous.delete()

        date = datetime.now() + timedelta(minutes=5)
        data = loginModel()
        data.mobile = mobile
        data.otp = getOtp
        data.dateTime = date
        data.save()
        return render(request, "otpVerification.html", {"mobile": mobile})

    return render(request, "index.html")


def otp(request):
    getOtp = ut.generateOtp(5)
    return HttpResponse(getOtp)


def otpVerification(request):
    print ('Here')
    userotp = request.GET['otpverification']

    if request.GET:
        mobile = request.GET['mobile']
        userotp = request.GET['otpverification']
        data = loginModel.objects.filter(mobile=mobile)
        print (data[0].dateTime)
        print (data[0].otp)
        currdate = datetime.now()
        maxDate = data[0].dateTime
        utc = pytz.UTC

        c = utc.localize(currdate)

        if userotp == data[0].otp and c < maxDate:
            return HttpResponse("Account Successfully Created")

        # n=len(data)
        # print (n)
        # print (data[0])
        # print (data[0].mobile)
        # print (data[0].dateTime)
        # print (data[0].otp)
        # print(userotp)
        return HttpResponse("Mismatch OTP")

    return render(request, "otpVerification.html")

def bookingPage(request):
    if request.GET:
        bsthh = request.GET['bsthh']
        bstmm = request.GET['bstmm']
        bethh = request.GET['bethh']
        betmm = request.GET['betmm']
        ppd = request.GET['ppd']
        # data changing into minutes
        bstt =  (int(bsthh) * 60) + int(bstmm)
        bett =  (int(bethh) * 60) + int(betmm)
        sittingtime = abs(bett - bstt)
        totalslot = sittingtime/int(ppd)
        # return HttpResponse("booking Chart")
        # return render(request, "opdForm.html", {"bstt": bstt, "bstt": bett, "totalslot": totalslot})
        d = BookingSlot()
        d.bsthh = bsthh
        d.bstmm = bstmm
        d.bethh = bethh
        d.betmm = betmm
        d.ppd = ppd
        d.bstt = bstt
        d.bett = bett
        d.totalslot = totalslot
        d.save()
    return render(request, "bookingPage.html")

def opdForm(request):
    if request.GET:
        patientname = request.GET['patientname']
        patientage = request.GET['patientage']
        mobile = request.GET['mobile']
        gender = request.GET['gender']
        address = request.GET['address']

        d = PatientDetails()
        d.patientname = patientname
        d.patientage = patientage
        d.mobile = mobile
        d.gender = gender
        d.address = address
        d.save()

    return render(request, "opdForm.html")
