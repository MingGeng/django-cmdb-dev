"""cmdbManager URL Configuration

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


# ============== i18n demo =========================================================

# from django.conf.urls.i18n import i18n_patterns
# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from django.urls import path, include
# from django.utils.translation import gettext_lazy
# from rest_framework import serializers, generics, viewsets, routers
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email',)
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # 通过 ModelViewSet 创建 UserViewSet
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_fields = ('id', 'username',)
#
#
# router = routers.SimpleRouter()
# # 注册 ViewSet
# router.register('users', UserViewSet)
#
# urlpatterns = [
#     # include 所有 DRF 注册的 ViewSet 到 api/
#     path('api/', include(router.urls)),
# ]
#
# # 只处理需要多语言支持的URL
# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls),
#     path('hello/',
#          lambda x: JsonResponse({'data': gettext_lazy('hello Kuakexing')},
#                                 json_dumps_params={'ensure_ascii': False})),
#     prefix_default_language=False
# )

# ===============================================================================

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, re_path

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language=False
)

urlpatterns += [
    re_path(r'^(.*)$', lambda r, s: TemplateResponse(r, 'base.html')),
]
