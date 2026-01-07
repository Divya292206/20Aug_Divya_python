from django.shortcuts import render
from .serilizers import *
from myapp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getuser(request):
    user= userinfo.objects.all()
    serializer= UserInfoSerializer(user,many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def getuserbyid(request,id):
    try:
        user= userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer= UserInfoSerializer(user)
    return Response(data=serializer.data)

@api_view(['DELETE','GET'])
def deletestid(request,id):
    try:
        stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=UserInfoSerializer(stid)
        return Response(data=serial.data)
    if request.method=='DELETE':
        userinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def createuser(request):
    if request.method=='POST':
        serializer=UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT','GET'])
def updateuser(request,id):
    try:
        user=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=UserInfoSerializer(user)
        return Response(data=serializer.data)
    elif request.method=='PUT':
        serializer=UserInfoSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)