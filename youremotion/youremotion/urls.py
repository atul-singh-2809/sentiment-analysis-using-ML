"""youremotion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('poco',views.poco,name='poco'),
    path('analyze',views.analyze,name='analyze'),
    path('realme',views.realme,name='realme'),
    path('analyze2',views.analyze2,name='analyze2'),
    path('moto',views.moto,name='moto'),
    path('analyze3',views.analyze3,name='analyze3'),
    path('rog',views.rog,name='rog'),
    path('analyze4',views.analyze4,name='analyze4'),
    path('samsung',views.samsung,name='samsung'),
    path('analyze5',views.analyze5,name='analyze5'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('msg',views.msg,name='msg'),
    path('login2',views.login2,name='login2'),
    path('msg2',views.msg2,name='msg2'),
    path('headphone',views.headphone,name='headphone'),
    path('boat',views.boat,name='boat'),
    path('analyze6',views.analyze6,name='analyze6'),
    path('realmebuds',views.realmebuds,name='realmebuds'),
    path('analyze7',views.analyze7,name='analyze7'),
    path('jbl',views.jbl,name='jbl'),
    path('analyze8',views.analyze8,name='analyze8'),
    path('skull',views.skull,name='skull'),
    path('analyze9',views.analyze9,name='analyze9'),
    path('sony',views.sony,name='sony'),
    path('analyze10',views.analyze10,name='analyze10'),
    path('laptop',views.laptop,name='laptop'),
    path('dell',views.dell,name='dell'),
    path('analyze11',views.analyze11,name='analyze11'),
    path('hp',views.hp,name='hp'),
    path('analyze12',views.analyze12,name='analyze12'),
    path('msi',views.msi,name='msi'),
    path('analyze13',views.analyze13,name='analyze13'),
    path('roglaptop',views.roglaptop,name='roglaptop'),
    path('analyze14',views.analyze14,name='analyze14'),
    path('mac',views.mac,name='mac'),
    path('analyze15',views.analyze15,name='analyze15'),
    path('tv',views.tv,name='tv'),
    path('samtv',views.samtv,name='samtv'),
    path('analyze16',views.analyze16,name='analyze16'),
    path('mitv',views.mitv,name='mitv'),
    path('analyze17',views.analyze17,name='analyze17'),
    path('onetv',views.onetv,name='onetv'),
    path('analyze18',views.analyze18,name='analyze18'),
    path('lg',views.lg,name='lg'),
    path('analyze19',views.analyze19,name='analyze19'),
    path('sonytv',views.sonytv,name='sonytv'),
    path('speaker',views.speaker,name='speaker'),
    path('zebra',views.zebra,name='zebra'),
    path('analyze21',views.analyze21,name='analyze21'),
    path('philips',views.philips,name='philips'),
    path('analyze22',views.analyze22,name='analyze22'),
    path('sonymusic',views.sonymusic,name='sonymusic'),
    path('analyze23',views.analyze23,name='analyze23'),
    path('saregama',views.saregama,name='saregama'),
    path('analyze24',views.analyze24,name='analyze24'),
    path('boatmusic',views.boatmusic,name='boatmusic'),
    path('analyze25',views.analyze25,name='analyze25')
    
]
