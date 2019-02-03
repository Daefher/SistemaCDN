from django.contrib import admin
from django.urls import path,include,re_path
from usuarios import views as usuarios_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
# from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/proyectos/',include('proyectos.api.urls', namespace="api-inventory")),
    #path('proyecto/', TemplateView.as_view(template_name='vista_general.html'),name ='general'),
    path('proyectos/', include('proyectos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('captcha/', include('captcha.urls')),
    path('', usuarios_views.login_view, name='home'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
