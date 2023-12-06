from django.urls import path
from .views import  UserCreateView, UserLoginView, UserLogoutView, UserProfileCreate, ProfileViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('api/', include(router.urls)), 
    # path('profile/create/', UserProfileCreate.as_view(), name='user-create'),
    # path('profile/<int:pk>/edit/', UserProfileDetailView.as_view(), name='user-profile'),

    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

