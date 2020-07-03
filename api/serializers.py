from . models import *
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank
        fields = [ 'id','name']



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = branch
        fields = [ 'ifsc','bank_id','branch','address','city','district','state']
