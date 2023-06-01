from . import views
from django.urls import path

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('offer',views.offer,name='offer'),
    path('cata',views.cata,name='cata'),
    path('skin',views.skin,name='skin'),
    path('hair',views.hair,name='hair'),
    path('makeup',views.makeup,name='makeup'),
    path('about',views.about,name='about'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('checkout',views.checkout,name='checkout'),
    path('lakme',views.lakme,name='lakme'),
    path('loreal',views.loreal,name='loreal'),
    path('foxt',views.foxt,name='foxt'),
    path('contact',views.contact,name='contact'),
    path('msg',views.msg,name='msg'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('account',views.account,name='account'),
    path('whishlist',views.whishlist,name='whishlist'),
]