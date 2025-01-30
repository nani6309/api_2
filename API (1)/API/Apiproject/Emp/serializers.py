from rest_framework import serializers
from . models import Empdetails

class empdetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = Empdetails
        fields ='__all__'



    def validate_age(self, value):
        if value >= 100:
            raise serializers.ValidationError("Age must be below 100 years.")
        return value
        

    def validate_mobile(self,value):
        value=str(value)
        if len(value) == 10:
            return value
        raise serializers.ValidationError('Mobile Number Required 10 Numbers But You Give The Bellow 10 Numbers')