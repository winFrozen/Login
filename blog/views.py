from allauth.account.views import login
from django.http import Http404
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.fields import IntegerField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class LoginPostAPIView(APIView):
    def get(self, request):
        client = Login.objects.all()
        serializer = LoginSerializer(client, many=True).data
        data = {
            'natija': serializer
        }
        return Response(data)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)