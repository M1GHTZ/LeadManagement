from rest_framework import serializers
from api.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields='__all__'
        read_only_fields=["id","created_date","updated_et"]