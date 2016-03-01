from django.db import models,DataError
from ndc_user.models import Ndc_user
import datetime

class Attendance(models.Model):
    CASH = 0
    CREDIT = 1

    PAYMENT_TYPE_LST = (
        (CASH,'Cash'),
        (CREDIT,'Credit')
    )

    date_time = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey('event.Event')
    user = models.ForeignKey(Ndc_user,blank=True,null=True)
    anonymous_first_name = models.CharField(max_length=100,blank=True,null=True)
    anonymous_last_name = models.CharField(max_length=100,blank=True,null=True)
    event_rate = models.ForeignKey('event.Event_rate')
    payment_type = models.IntegerField(choices=PAYMENT_TYPE_LST,blank=True,null=True)

    def save(self, *args, **kwargs):
        if self.event_rate.amount != 0 and self.payment_type == None:
            raise DataError
            
        super(Attendance, self).save(*args, **kwargs)

class Venue(models.Model):
    name = models.CharField(max_length=100,unique=True)
    start_time = models.TimeField()
    duration = models.IntegerField()
        
    def __str__(self):
        return self.name

class Event(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField()
    venue = models.ForeignKey(Venue)
    attend_user_lst = models.ManyToManyField(Ndc_user,blank=True,through=Attendance)

    class Meta:
        unique_together = ('date', 'venue',)

    def get_start_date_time(self):
        return datetime.datetime.combine(self.date, self.start_time)

    def get_end_date_time(self):
        return self.get_start_date_time() + datetime.timedelta(hours=self.duration)

    def is_live(self):
        now = datetime.datetime.now()
        now = now - datetime.timedelta(hours=8)#hardcode timezone to be PST which is where SBF located.
        return self.get_start_date_time() <= now and now <= self.get_end_date_time()

class Event_rate(models.Model):
    """
        For past events to be self-contained, each event have to know about each own rate.
    """
    DANCE_ONLY_MEMBER = 0
    DANCE_AND_LESSON_MEMBER = 1
    DANCE_ONLY_NON_MEMBER = 2
    DANCE_AND_LESSON_NON_MEMBER = 3
    TIP_FOR_BLUES = 4
    UCSC = 5
    EXEMPT = 6
    DJ_INSTRUCTOR = 7
    VOLUNTEER = 8
    COMP = 9

    DANCE_RATE_LST = (
        (DANCE_ONLY_MEMBER,'Member dance only'),
        (DANCE_AND_LESSON_MEMBER,'Member lesson and dance'),
        (DANCE_ONLY_NON_MEMBER,'Non-member dance only'),
        (DANCE_AND_LESSON_NON_MEMBER,'Non-member lesson and dance'),
        (TIP_FOR_BLUES,'Tips for blues'),
        (UCSC,'UC Santa Cruz student'),
        (EXEMPT,'Exempt'),
        (DJ_INSTRUCTOR,'DJ / Instructor'),
        (VOLUNTEER,'Volunteer'),
        (COMP,'Comp')
    )

    event = models.ForeignKey('event.Event',related_name='event_rate_lst')
    rate = models.IntegerField(choices=DANCE_RATE_LST)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

class Default_rate(models.Model):
    rate = models.IntegerField(choices=Event_rate.DANCE_RATE_LST,unique=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)    


