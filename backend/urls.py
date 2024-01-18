from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token  
from rest_framework import routers 
 
 
router = routers.DefaultRouter()
router.register('shop',views.ShopSetView) 
router.register('review',views.ReviewSetView)   

urlpatterns = [  
     path('', include(router.urls)),
]
