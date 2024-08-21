"""
URL configuration for core_files project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from qBank import views as qBank_func

from  django.views.static import serve
from  django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', qBank_func.loginPage,name='loginPage'),
    path('home/', qBank_func.home,name='home'),
    # path('', qBank_func.home,name='home'),
    path('uploadImage/', qBank_func.uploadImage,name='uploadImage'), #url to upload image files from the editor
    path('signupPage/', qBank_func.signupPage,name='signupPage'),
    path('signUp/', qBank_func.signupProcess,name='signUp'),
    path('loginPage/', qBank_func.loginPage,name='loginPage'),
    path('login/', qBank_func.loginProcess,name='login'),
    path('getOTP/', qBank_func.getOTP,name='getOTP'),
    path('logout/', qBank_func.logoutProcess,name='logout'),
    path('submitQuestion/', qBank_func.submitQuestion,name='submitQuestion'),
    path('mySubmissions/', qBank_func.mySubmissionPage,name='mySubmissionPage'),
    path('managerHome/', qBank_func.managerHome,name='managerHome'),
    path('approvalPoint/', qBank_func.managerApprovalPoint,name='approvalPoint'),
    path('managerEditRequest/', qBank_func.managerEditRequest,name='managerEditRequest'),
    path('managerSetExam/', qBank_func.managerSetExam,name='managerSetExam'),
    path('managerSettings/', qBank_func.managerSettings,name='managerSettings'),
    path('printQuestion/', qBank_func.managerPrintQuestion,name='printQuestion'),
    path('forgotPassword/', qBank_func.forgotPassword,name='forgotPassword'),
    path('editRequest/',qBank_func.submitterEditRequest,name='editRequest'),
    

    path('test/', qBank_func.testPage,name='test'),
    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), # This is the code will let the server know where to find the media files and serve them
]   


# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    