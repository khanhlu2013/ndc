from django.db import models,IntegrityError

class MembershipOverlapError(IntegrityError):
    pass

class Membership(models.Model):

    BRONZE = 0
    SILVER = 1
    GOLD = 2
    MEMBERSHIP_TYPE_LST = (
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
    )

    start_date = models.DateField()
    membership_type = models.IntegerField(choices=MEMBERSHIP_TYPE_LST)    
    is_issue_key = models.BooleanField(default=False)
    user = models.ForeignKey('ndc_user.Ndc_user',related_name='membership_lst')

    def get_membership_year(self):
        day = self.start_date.day
        month = self.start_date.month
        year = self.start_date.year

        if month == 1 and day <= 14:
            return year + 1
        else:
            return year


    def save(self, *args, **kwargs):
        membership_lst = list(self.user.membership_lst.all())
        if(self.id != None):
            for membership in membership_lst:
                if membership.id == self.id:
                    membership_lst.remove(membership)
                    break

        membership_year_lst = [membership.get_membership_year() for membership in membership_lst]
        membership_year_lst.append(self.get_membership_year())

        if len(membership_year_lst) > len(set(membership_year_lst)):
            raise MembershipOverlapError()
        else:
            super(Membership, self).save(*args, **kwargs)