"""gru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from api import views
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumni/', views.alumni_get, name = "alumni"),
    path('alumni/<str:pk>', views.alumni_getspecific, name = "alumni-specific"),
    path('alumni-create/', views.alumni_post,name ="alumni-create"),
    path('alumni-update/<str:pk>', views.alumni_put,name ="alumni-update"),
    path('alumni-delete/<str:pk>', views.alumni_delete,name ="alumni-delete"),
    path('professor/', views.professor_get, name = "professor"),
    path('professor/<str:pk>', views.professor_getspecific, name = "professor-specific"),
    path('professor-create/', views.professor_post,name ="professor-create"),
    path('professor-update/<str:pk>', views.professor_put,name ="professor-update"),
    path('professor-delete/<str:pk>', views.professor_delete,name ="professor-delete"),
    
]

urlpatterns += [
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('', RedirectView.as_view(url='api/', permanent=True)),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]