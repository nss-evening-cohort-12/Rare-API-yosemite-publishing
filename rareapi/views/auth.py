import json
from datetime import date
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rareapi.models import RareUser
from django.core.files.base import ContentFile
import base64
import uuid



@csrf_exempt
def login_user(request):
    req_body = json.loads(request.body.decode())

    if request.method == "POST":
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            current_user = authenticated_user
            data = json.dumps({"valid": True, "token": token.key, "user_id": current_user.id})
            return HttpResponse(data, content_type='application/json')

        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register_user(request):
    import pdb
   
    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username= req_body['username'],
        email = req_body['email'],
        password = req_body['password'],
        first_name  = req_body['first_name'],
        last_name = req_body['last_name']
    )
    


    rare_user = RareUser.objects.create(

        user=new_user,
        bio = req_body['bio'],
        created_on = date.today(),
        active = True
    )

    format, imgstr = req_body['avatar_url'].split(';base64,')
    ext = format.split('/')[-1]
    image_data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
    pdb.set_trace()
    rare_user.profile_image_url = image_data

    rare_user.save()

    token = Token.objects.create(user=new_user)

    data = json.dumps({'token': token.key, "user_id": new_user.id})
    return HttpResponse(data, content_type="application/json")
