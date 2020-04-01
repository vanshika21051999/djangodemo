"""
from django.http import HttpResponse as response
from django.shortcuts import render


def home(request):
	return render(request,'pages/home.html')
def index(request):
	text=request.GET['text']
	#text1=text.split()
	text2={}
	for i in text:
		if i in text2:
			text2[i]+=1
		else:
			text2[i]=1
	return render(request,'pages/index.html',{'text2':text2})
	"""