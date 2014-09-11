#-*- coding: UTF-8 -*- 
from django.http import HttpResponse
from log.models import Log, Category, User
from django.core import serializers
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt

logs = Log.objects.all()

def timeToString(datetime):
	return datetime.strftime("%Y-%m-%d %H:%M")

def userToJson(user):
	return json.dumps({'name': user.name, 'email': user.email, 'userid': user.userid})

def home(request):
	data = json.dumps([{'message': log.message, 
		'log_date': timeToString(log.log_date),
		'user': userToJson(log.user),
		'category': log.error_type.title
		} for log in logs])
	return HttpResponse(data)

@csrf_exempt 
def createLog(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		
		users = User.objects.filter(userid=data['userid'])
		if len(users) == 0:
			user = User.objects.create(userid=data['userid'], name=data['name'], email=data['email'])
		else:
			user = users[0]

		error_type = Category.objects.get(pk=data['error_type'])

		log = Log.objects.create(user=user, error_type=error_type, message=data['message'], log_date=timezone.now())
		print log
	return HttpResponse('success')