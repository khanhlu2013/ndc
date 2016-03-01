from rest_framework import serializers
from membership.models import Membership

class Membership_serializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('id','start_date','membership_type','is_issue_key')