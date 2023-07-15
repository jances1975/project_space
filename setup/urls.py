from django.contrib import admin
from django.urls import path, include
# from galeria.views import index
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns é variável do tipo lista com todos os path
urlpatterns = [
    path('admin/', admin.site.urls),
    # deixando path em branco aqui e em app\urls.py urlpatterns = [path('admin/', admin.site.urls),
    # vc http://127.0.0.1:8000/ ou localhost que entra no index.html
    path('', include('apps.galeria.urls')),
    # incuindo todas as urls de galeria
    path('', include('apps.usuarios.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
