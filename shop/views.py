from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.template.loader import render_to_string
from django.views.generic import RedirectView

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import *
from .serializer import *

# Create your views here.
class ListUsersView(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)

    queryset = Profile.objects.all().order_by('name')
    serializer_class = MerchSerializer


class ListProductsView(viewsets.ModelViewSet):

    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductsSerializer
