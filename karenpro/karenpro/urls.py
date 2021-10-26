"""karenpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from karen import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('mainpage/', views.mainpage),
    path('cutkum/<str:word>', views.get_queryset, name='cutkum'),
    path('getquestion/<str:word>', views.get_question,),
    path('getanswer/<str:id>', views.get_setanswer, name='answer'),
    path('addquestion/', views.addanswer),
    path('username_pass', views.username_pass),
    path('logout/', views.logout),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('addword', views.addword),
    path('editword/<int:pk>', views.editword, name='editword'),
    path('addques/<int:number>', views.addquestion, name='addques'),
    path('deleteques/<int:id>', views.deleteques, name='deleteques'),
    path('editques/<int:id>/<int:number>', views.editques, name='editques'),




    # path('url',views.get_context_data)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
