"""rareYosemiteServer URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from rareapi.views import register_user, login_user, CategoryViewSet, CommentViewSet, TagViewSet, PostViewSet, ReactionViewSet
from rareapi.views import register_user, login_user, CategoryViewSet, CommentViewSet, TagViewSet, PostViewSet, AuthUserViewSet, SubscriptionViewSet
from rareapi.views.rare_user import UserViewSet

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'comments', CommentViewSet, 'comment')
router.register(r'tags', TagViewSet, 'tag')
router.register(r'posts', PostViewSet, 'post')
router.register(r'users',UserViewSet, 'user')
router.register(r'reactions',ReactionViewSet, 'react')
router.register(r'auth_users', AuthUserViewSet, 'auth_user')
router.register(r'subscriptions', SubscriptionViewSet, 'subscription')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
