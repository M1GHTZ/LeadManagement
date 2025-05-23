from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from api.serializers import LeadSerializer
from rest_framework.response import Response
from api.models import Lead
from rest_framework import authentication,permissions


# Create your views here.
class LeadView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,*args,**kwargs):
        all_leads=Lead.objects.all()
        serializer_instance=LeadSerializer(all_leads,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):
        serializer_instance=LeadSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
class LeadRetrieveUpdateDestroyView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        lead_instance=get_object_or_404(Lead,id=id)
        serialized_instance=LeadSerializer(lead_instance)
        return Response(data=serialized_instance.data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        lead_instance=get_object_or_404(Lead,id=id)
        lead_instance.delete()
        return Response(data={"Message":"Lead Deleted"})
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        lead_instance=get_object_or_404(Lead,id=id)
        serialized_instance=LeadSerializer(data=request.data,instance=lead_instance)
        if serialized_instance.is_valid():
            return Response(data=serialized_instance.data)
        else:
            return Response(data=serialized_instance.errors)

