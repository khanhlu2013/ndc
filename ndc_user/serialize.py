from rest_framework import serializers,fields
from ndc_user.models import Ndc_user
from membership.serialize import Membership_serializer
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType

class ContentType_serializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ('app_label','model','name')

class Permission_serializer(serializers.ModelSerializer):
    content_type = ContentType_serializer(many=False)

    class Meta:
        model = Permission
        fields = ('codename','content_type')

class Group_serializer(serializers.ModelSerializer):
    permissions = Permission_serializer(many=True)

    class Meta:
        model = Group
        fields = ('name','permissions')

class Ndc_user_serializer(serializers.ModelSerializer):

    membership_lst = Membership_serializer(many=True)
    groups = Group_serializer(many=True)

    class Meta:
        model = Ndc_user
        fields = (
            'id',
            'email',
            'is_email_verify',
            'ndc_old_id',
            'create_date',
            'first_name',
            'last_name',
            'phone',
            'gender',
            'is_active',
            'is_exempt',
            'membership_lst',
            'groups'
        )