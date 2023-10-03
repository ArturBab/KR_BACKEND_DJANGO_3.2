from django.contrib import admin
from django.urls import path, include, re_path

from backend.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="KR ST BACKEND SWAGGER METHODS DOC",
        default_version='1.0.0',
        description="Swagger KR Backend doc",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # маршрут для использования авторизации на основе сессий.
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/article/', ArticleAPIListAndPost.as_view()),
    path('api/article/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('api/author/', AuthorAPIPost.as_view()),
    path('api/authorAdm/', AuthorAPIAdmList.as_view()),
    path('api/register/', RegisterAPIView.as_view()),
    path('api/login/', LoginAPIView.as_view()),
    path('api/auth/', UserAPIAuthView.as_view()),
    path('api/logout/', LogoutAPIView.as_view()),
    # path('api/users/', UserAPIList.as_view()),
    # path('api/auth', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
]
