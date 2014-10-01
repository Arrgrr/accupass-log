from django.shortcuts import render
from django.http import HttpResponse
from log.models import Log, Category, User
import json

def timeToString(datetime):
	return datetime.strftime("%Y-%m-%d %H:%M")

def userToJson(user):
	return json.dumps({'name': user.name, 'email': user.email, 'userid': user.userid})
'''
def home(request):
	logs = Log.objects.all()
	data = json.dumps([{'message': log.message,
		'pltform': log.platform, 
		'log_date': timeToString(log.log_date),
		'user': userToJson(log.user),
		'category': log.error_type.title
		} for log in logs])
	return HttpResponse(data, content_type='application/json')
'''
def home(request):
	logs = Log.objects.all()
	print logs
	context = {'logs': logs}
	return render(request, 'log/home.html', context)
	#return HttpResponse(context, content_type='application/json')