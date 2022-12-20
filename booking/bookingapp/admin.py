from django.contrib import admin
from .models import loginModel
from .models import BookingSlot
from .models import PatientDetails
# Register your models here.
admin.site.register(loginModel)
admin.site.register(BookingSlot)
admin.site.register(PatientDetails)