"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from rest_framework import permissions, serializers, viewsets, routers
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework.authtoken import views
from django.views.generic import TemplateView
from rest_framework.decorators import action


# 自动创建用户token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
       
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods=['GET'],detail=False)
    def reqister(self) :
        username = self.request.username
        password = self.request.password
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)      

class GroupViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'rocky/users', UserViewSet)
router.register(r'rocky/groups',GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^rocky/api-token-auth/', views.obtain_auth_token),
    path('rocky/', include('rocky.urls'))
]

