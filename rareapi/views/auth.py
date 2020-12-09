import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rareapi.models import RareUser
from datetime import date


@csrf_exempt
def login_user(request):
    req_body = json.loads(request.body.decode())

    if request.method == "POST":
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')

        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register_user(request):
    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username= req_body['username'],
        email = req_body['email'],
        password = req_body['password'],
        first_name  = req_body['first_name'],
        last_name = req_body['last_name']
    )

    rare_user = RareUser.objects.create(
        bio = req_body['bio'],
        profile_image = req_body['profile_image'],
        created_on = date.today(),
        active = True
    )

    rare_user.save()

    token = Token.objects.create(user=new_user)

    data = json.dumps({'token': token.key})
    return HttpResponse(data, content_type="application/json")
