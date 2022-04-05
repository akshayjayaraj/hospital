from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from hosapp.models import*
import random
import string
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.



def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def services(request):
	return render(request,'services.html')

def patient(request):
	if request.method =='POST':
		Name=request.POST['Name']
		email=request.POST['email']
		password=request.POST['password']
		location=request.POST['locations']
		number=request.POST['Phoneno']
		time=request.POST['time']
		about=request.POST['problem']

		check=patient_tb.objects.filter(email=email)
		if check:
			return render(request,'about.html',{'error':'Email already exist'})
		else:
			query=patient_tb(Name=Name,email=email,location=location,number=number,time=time,about=about,password1=password)
			query.save()
		return render(request,'patient.html')
	else:
		return render(request,'patient.html')


def patientlogin(request):
	if request.method=='POST':
		email=request.POST['email1']
		password=request.POST['password']

		check= patient_tb.objects.all().filter(email=email,password1=password)
		if check:
			for x in check:
				request.session['userid']=x.id
			return render(request,'about.html')
		else:
			return render(request,'patientlogin.html')
	else:
		return render(request,'patientlogin.html')
			

def logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
	return render(request,'patientlogin.html')	



def doctors(request):
	if request.method=='POST':
		dname=request.POST['drname']
		specailised=request.POST['special']
		available=request.POST['times']
		password=request.POST['password']
		Email=request.POST['Email']
		check=Doctors_tb.objects.filter(Email=Email)
		if check:
			return render(request,'doctor.html',{'error':'Email already exist'})
		else:
			query=Doctors_tb(dname=dname,specailised=specailised,available=available,password=password,Email=Email)
			query.save()
		return render(request,'doctor.html')
	else:
		return render(request,'doctor.html')
		


def drlogin(request):
	if request.method=='POST':
		Name=request.POST['drname1']
		password=request.POST['password1']
		check=Doctors_tb.objects.all().filter(dname=Name,password=password)
		if check:
			for x in check:
				request.session['userid']=x.id
			return render(request,'services.html')
		else:
			return render(request,'drlogin.html')
	else:
		return render(request,'drlogin.html')


def drlogout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
	return render(request,'drlogin.html')


def booking(request):
	if request.session.has_key('userid'):
		if request.method=='POST':
			drids=request.POST['drn']
			time=request.POST['time2']
			date=request.POST['date']
			problems=request.POST['des1']
			pid=request.session['userid']
			drid=Doctors_tb.objects.get(id=drids)
			paid=patient_tb.objects.get(id=pid)
			query=token_tb(time=time,date=date,problems=problems,pid=paid,drid=drid)
			query.save()
		viewquery=Doctors_tb.objects.all()
		return render(request,'booking.html',{'viewquery':viewquery})
	else:
		return render(request,'patientlogin.html')



def view(request):
	viewquery=Doctors_tb.objects.all()
	return render(request,'viewajas.html',{'viewquery':viewquery})



def viewajas(request):
	print("xxxxxxxxxxxxxxxxxxxxxxxx")
	doct=request.GET.get('docid')
	doid=Doctors_tb.objects.all().filter(id=doct)
	print(doid)
	for x in doid:
		doname=x.dname
		dospecial=x.specailised
		dotime=x.available
		doctr={"dname":doname,"dspecial":dospecial,"dtime":dotime}
		print(doctr)
		return JsonResponse(doctr)
			

def viewdr(request):
	viewquery=Doctors_tb.objects.all()
	return render(request,'dr loginajax.html',{'viewquery':viewquery})

def viewdrajax(request):
	dpass=request.GET.get('drid')
	drpassw=Doctors_tb.objects.all().filter(id=dpass)
	print(drpassw)
	for x in drpassw:
		dname=x.dname
		drpass=x.password
	drforgot={"dname2":dname,"dpassword":drpass}
	print(drforgot)
	return JsonResponse(drforgot)

def passforgot(request):
	if request.method=='POST':
		email=request.POST['email2']
		check=Doctors_tb.objects.filter(Email=email)
		if check:
			print(check)
			for x in check:
				userid=x.id
				print("xxxxxxxxxxxxxxxxx------------------------")
				x = ''.join(random.choices(email + string.digits, k=8))
				y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
				subject = 'Change password'
				url = f'Hi Change password    http://127.0.0.1:8000/newpassword/?uid={userid}'
				message = f'click on the link {url}'
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [email, ] 
				send_mail( subject, message, email_from, recipient_list ) 
			return render(request,'passwordforgot.html',{'change':'Change password'})
	else:
		return render(request,'passwordforgot.html')


def newpassword(request):
	if request.method=='POST':
		usid=request.POST['uid']
		print(usid,'vvvvvvvvvvvvv')
		passn=request.POST['passwordn']
		passc=request.POST['passwordc']
		if usid:
			query=Doctors_tb.objects.all().filter(id=usid).update(password=passn)
		return render(request,'drlogin.html',{'alert':'Sucessfully password changed'})
	else:
		usid=request.GET['uid']
		print(usid)
		return render(request,'newpassword.html',{'same':'Use different Password','uid':usid})



def patpassforgot(request):
	if request.method=='POST':
		email=request.POST['email3']
		check=patient_tb.objects.filter(email=email)
		if check:
			print(check)
			for x in check:
				userid=x.id
				print("xxxxxxxxxxxxxxxxx------------------------")
				x = ''.join(random.choices(email + string.digits, k=8))
				y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
				subject = 'Change password'
				url = f'Hi Change password    http://127.0.0.1:8000/patconfirmpass/?uid={userid}'
				message = f'click on the link {url}'
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [email, ] 
				send_mail( subject, message, email_from, recipient_list ) 
			return render(request,'patpassforgot.html',{'change':'Change password'})
	else:
		return render(request,'patpassforgot.html')



def patconfirmpass(request):
	if request.method=='POST':
		usid=request.POST['uid']
		print(usid,'vvvvvvvvvvvvv')
		passn=request.POST['passwordn']
		passc=request.POST['passwordc']
		if usid:
			query=patient_tb.objects.all().filter(id=usid).update(password1=passn)
		return render(request,'patientlogin.html',{'alert':'Sucessfully password changed'})
	else:
		usid=request.GET['uid']
		print(usid)
		return render(request,'patconfirmpass.html',{'same':'Use different Password','uid':usid})

	
	
#send email

# def passforgot(request):
#     if request.method=='POST':
#         email = request.POST['email2']
#         tb = Doctors_tb.objects.filter(Email=email)
#         for x in tb:
#             emails=x.Email
#             if emails==email:
#                  message = f'please click this link and reset your password: http://127.0.0.1:8000/newpassword/?sid={x.id}'
#                  subject = 'welcome to Whats App'
#                  email_from = settings.EMAIL_HOST_USER 
#                  recipient_list = [email, ] 
#                  print(recipient_list)
#                  send_mail( subject,message, email_from, recipient_list) 
#                  b = Doctors_tb(Email=email)
#                  b.save()
#                  return render(request,'passwordforgot.html') 
#             else:
#                  return render(request,"passwordforgot.html") 
#     else:
#         return render(request,"passwordforgot.html") 




def drviewdata(request):
	viewqurey = Doctors_tb.objects.all()
	return render(request,'drtable.html',{'viewqurey':viewqurey})
