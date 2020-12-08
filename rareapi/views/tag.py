from django.http import HttpResponseServerError
from django.views.generic.base import View
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import GameType
