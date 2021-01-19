from django.shortcuts import render

# Create your views here.
from .serializers import BioSerializer
from .models import Bio
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,ListModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

#Retrieve, Update, Destroy
class Bio_RUD(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    serializer_class = BioSerializer
    queryset = Bio.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#List, Create
class Bio_CL(GenericAPIView,CreateModelMixin,ListModelMixin):
    serializer_class = BioSerializer
    queryset = Bio.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

