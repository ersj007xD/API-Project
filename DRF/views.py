from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import User, Profession
from .serializers import UserSerializer, ProfessionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def userdetails(request):
    """Fetching User Details API"""
    get_obj = User.objects.all()
    serializer = UserSerializer(get_obj, many=True)
    if serializer:
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message": "records fetched successfully"})
    else:
        return Response({"status":False, "result":dict(), "message": "records not fetched successfully"})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def userid_details(request,pk):
    """User GET API """
    get_obj = User.objects.get(id=pk)
    serializer = UserSerializer(get_obj)
    if serializer:
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message": "records fetched successfully"})
    else:
        return Response({"status":False, "result":dict(), "message": "records not fetched successfully"})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def professiondetails(request):
    """Professon Details GET API"""
    get_obj = Profession.objects.all()
    serializer = ProfessionSerializer(get_obj, many=True)
    if serializer:
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message": "records fetched successfully"})
    else:
        return Response({"status":False, "result":dict(), "message": "records not fetched successfully"})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def professionid_details(request,pk):
    """Profession Details GET API"""
    get_obj = Profession.objects.get(id=pk)
    serializer = ProfessionSerializer(get_obj)
    if serializer:
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message": "records fetched successfully"})
    else:
        return Response({"status":False, "result":dict(), "message": "records not fetched successfully"}) 
                 


@api_view(['POST'])
def add_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message":"records created successfully"}) 
    else:
        return Response({"status":False, "result":dict(), "message":"records not created successfully"})

@api_view(['POST'])
def add_profession(request):
    data = request.data
    serializer = ProfessionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message":"records created successfully"}) 
    else:
        return Response({"status":False, "result":dict(), "message":"records not created successfully"})


@api_view(['PUT'])
def edit_user(request,pk):
    data = request.data
    get_obj = User.objects.get(id=pk)
    serializer = UserSerializer(get_obj, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message":"records created successfully"}) 
    else:
        return Response({"status":False, "result":dict(), "message":"records not created successfully"})

@api_view(['PUT'])
def edit_profession(request,pk):
    data = request.data
    get_obj = Profession.objects.get(id=pk)
    serializer = ProfessionSerializer(get_obj, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        result = dict()
        result["data"] = serializer.data
        return Response({"status":True, "result":result, "message":"records created successfully"}) 
    else:
        return Response({"status":False, "result":dict(), "message":"records not created successfully"})

@api_view(['DELETE'])
def delete_user(request,pk):
    get_obj = User.objects.get(id=pk)
    get_obj.delete()
    return Response({"status":True, "message":"Data Deleted Successfully"})  

@api_view(['DELETE'])
def delete_profession(request,pk):
    get_obj = Profession.objects.get(id=pk)
    get_obj.delete()
    return Response({"status":True, "message":"Data Deleted Successfully"}) 
