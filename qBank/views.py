import uuid
from .models import *
from django.conf import settings
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from qBank.forms import signUpForm
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template
import qBank.context_processors as custom_context_variables
from  django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from pytz import timezone 



def home(request):
    if request.user.is_authenticated and request.user.role=='submitter':
        return render(request,'submitter/submitterHome.html')
    elif request.user.is_authenticated and request.user.role=='manager':
        return redirect('managerHome')
    
    # return render(request,'questions.html')

def newFileName(originalFilename):
    ext = originalFilename.split('.')[-1]
    newName = "%s.%s" % (uuid.uuid4(), ext)
    return newName

def uploadImage(request): #function to upload the imageFiles from the editor to the server
    file=request.FILES.get("file")
    file = request.FILES.get("file")
    file.name=newFileName(file.name)
    fileUploads.objects.create(doc=file)
    imageLink="/media/images/"+file.name #creating the link to the image file
    return JsonResponse({'status':'success','imageLink':imageLink})

def sendEmail(to_email, subject, otpCode):
    date=datetime.now(timezone(settings.TIME_ZONE))
    expiration_time=(datetime.now(timezone(settings.TIME_ZONE))+ timedelta(seconds=300)) # 5 minutes expiration time
    contextData={'date':date,'otp':otpCode,'expiration_time':str(expiration_time.strftime("%I:%M %p, %d %B %Y"))}

    if(type(to_email)!=list):
        to_email=[to_email]
    else:
        to_email=to_email

    subject=subject
    from_email=settings.EMAIL_HOST_USER
    message=get_template('common/otpEmail.html').render(contextData)
    msg = EmailMessage(subject, message, to=to_email ,from_email=from_email)
    msg.content_subtype = "html"
    msg.send()
    # send_mail(subject, message, from_email, to_email)

    

def signupPage(request):
    form = signUpForm()
    context = {'form':form}
    return render(request,"common/signup.html",context)

def signupProcess(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            print(form.cleaned_data)
            last_name = form.cleaned_data['last_name']
            email_initial = form.cleaned_data['email_initial']
            member_email=email_initial+custom_context_variables.client_domain_url
            institution_id = form.cleaned_data['institution_id']
            otpcode = form.cleaned_data['otpcode']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                if member.objects.filter(email=member_email).exists():
                    messages.error(request, 'User already exists')
                    return redirect('signupPage')
                if (otp_table.objects.filter(member_email=member_email,purpose='signup').exists() ):
                    otp_data = otp_table.objects.get(member_email=member_email)
                    otp_time=otp_data.expire_time
                    if otp_data.otp_code == otpcode and datetime.now(timezone(settings.TIME_ZONE)) < otp_time:
                        username = first_name+uuid.uuid4().hex[:6].upper()
                        user = member.objects.create_user(email=member_email, password=password, username=username)
                        user.first_name = first_name
                        user.last_name = last_name
                        user.inst_emp_id = institution_id
                        user.role = 'submitter'
                        user.save()
                        # print("User created")
                        return render(request,'common/successfulSignup.html')
                    else:
                        # return JsonResponse({'status':'error', 'message':'Invalid OTP'})
                        messages.error(request, 'OTP Expired')
                        return redirect('signupPage')
                else:
                    # return JsonResponse({'status':'error', 'message':'Invalid OTP'})
                    messages.error(request, 'Invalid OTP')
                    return redirect('signupPage')
            else:
                # return JsonResponse({'status':'error', 'message':})
                messages.error(request, 'Password did not match')
                return redirect('signupPage')
        else:
            # messages.error(request, form.errors.as_data())
            messages.error(request, 'Invalid Form Data')
            return redirect('signupPage')
    else:
        messages.error(request, 'Invalid Request.')
        context={'messageDetail':"Please make sure you are requesting the page the proper way."}
        return redirect('signupPage')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,"common/login.html")

def loginProcess(request):
    email_initial=request.POST.get('email_initial')
    password=request.POST.get('password')
    remember=request.POST.get('rememberMe')
    useremail=email_initial+custom_context_variables.client_domain_url
    if request.method == 'POST':
        user = authenticate(request, email=useremail, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if remember is None:
                request.session.set_expiry(0)

         
            request.session['userName']=user.first_name
            # request.session['userID']=user.member_id
            print(request.session)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('loginPage')


def logoutProcess(request):
    logout(request)
    return redirect('loginPage')

def getOTP(request):
    email_initial=request.POST.get('email_initial') #getting the email from the ajax request of getOTP function in otp.js file 
    email=email_initial+custom_context_variables.client_domain_url

    if(email_initial!="" and request.method=="POST"):
        random_otp=str(uuid.uuid4()).split('-')[0]
        zone=timezone(settings.TIME_ZONE)
        expiration_time=datetime.now(zone)+ timedelta(seconds=300)
        
        # print(expiration_time)
        otp_table.objects.update_or_create(member_email=email, defaults={'otp_code':random_otp,'expire_time':expiration_time})
        sendEmail(email,"AQMAN OTP",random_otp)
        return JsonResponse({'status':'success','otp':random_otp})
    else:
        return JsonResponse({'status':'error','message':'Invalid Email'})
    

def submitQuestion(request):
    if request.method == 'POST' and request.user.is_authenticated and request.user.role=='submitter':
        qsubmitter_id = request.user.member_id
        title = request.POST.get('qTitle')
        module = request.POST.get('module')
        chapter = request.POST.get('chapter')
        topic = request.POST.get('topic')
        subTopic = request.POST.get('subTopic')
        questionText = request.POST.get('question')
        choice1 = request.POST.get('choice1')
        choice2 = request.POST.get('choice2')
        choice3 = request.POST.get('choice3')
        choice4 = request.POST.get('choice4')
        answer = request.POST.get('answer')
        submitter=member.objects.get(member_id=qsubmitter_id)
        print(submitter,title,module,chapter,topic,subTopic,question,choice1,choice2,choice3,choice4,answer)
        question.objects.create(submitter_id=submitter,question_title=title, module_no=module, chapter_no=chapter, topic_no=topic, sub_topic_no=subTopic, question_text=questionText, choice_1=choice1, choice_2=choice2, choice_3=choice3, choice_4=choice4, answer=answer)
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'error','message':'Invalid Request'})

def mySubmissionPage(request):
    if request.user.is_authenticated and request.user.role=='submitter':
        questions=question.objects.filter(submitter_id=request.user.member_id)
        questions= questions.order_by('-submission_date')
        # for q in questions:
        #     print(q.question_title)
        return render(request,'submitter/mySubmissions.html',{'questions':questions})
    else:
        return redirect('loginPage')
    

def submitterEditRequest(request):
    return render(request,'submitter/editRequest.html')


def managerHome(request):
    if request.user.is_authenticated and request.user.role=='manager':
        questions=question.objects.filter(question_status='pending')
        questions= questions.order_by('module_no','chapter_no','topic_no','sub_topic_no')
        return render(request,'manager/managerQBank.html',{'questions':questions})
    else:
        return redirect('loginPage')



def managerPrintQuestion(request):
    if request.user.is_authenticated and request.user.role=='manager':
        questions=question.objects.all()
        questions= questions.order_by('module_no','chapter_no','topic_no','sub_topic_no') #('SELECT module_no*1000+chapter_no*100+topic_no*10+sub_topic_no as refNum from qBank_question ORDER BY refNum ASC;')
        
        totalQuestions=questions.count()
        examDuration=int(totalQuestions*1.5)
        examDate=datetime.now().strftime("%d %B, %Y")
        nameOfExam="General Module Test"

        context={'questions':questions,'totalQuestions':totalQuestions,'examDuration':examDuration,'examDate':examDate,'nameOfExam':nameOfExam}
        
        return render(request,'manager/managerPrintQuestion.html',context)
    else:
        return redirect('loginPage')

def managerApprovalPoint(request):
    if request.user.is_authenticated and request.user.role=='manager':
        questions=question.objects.filter(question_status='pending')
        # questions= questions.order_by('module_no','chapter_no','topic_no','sub_topic_no')
        questions= questions.order_by('submission_date')
        return render(request,'manager/managerApprovalPoint.html',{'questions':questions})
    else:
        return redirect('loginPage')
    

def managerEditRequest(request):
    if request.user.is_authenticated and request.user.role=='manager':
        return render(request,'manager/editRequest.html')

def managerSetExam(request):
    if request.user.is_authenticated and request.user.role=='manager':
        return render(request,'manager/managerSetExam.html')

def managerSettings(request):
    if request.user.is_authenticated and request.user.role=='manager':
        return render(request,'manager/managerSettings.html')


def forgotPassword(request):
    return render(request,'common/forgotPassword.html')




def testPage(request):
   
    return render(request,'manager/managerPrintQuestion.html')