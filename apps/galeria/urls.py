from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, filtrarnebulosa, filtrarestrela, filtrargalaxia, filtrarplaneta, nova_imagem, editar_imagem, deletar_imagem
# Se colocar \ dá pra descer os impportes

# urlpatterns é variável do tipo lista com todos os path
urlpatterns = [
    # deixando path em branco aqui e em app\urls.py urlpatterns = [path('admin/', admin.site.urls),
    # vc http://127.0.0.1:8000/ ou localhost que entra no index.html
    path('', index, name='index'),
    # path('', index),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    # path('imagem/', imagem)
    # incuindo todas as urls de galeria
    path("busccar", buscar, name="buscar"),
    path("nova-imagem", nova_imagem, name="nova_imagem"),
    path("editar-imagem", editar_imagem, name="editar_imagem"),
    path("deletar-imagem", deletar_imagem, name="deletar_imagem"),
    path("filtrarnebulosa", filtrarnebulosa, name="filtrarnebulosa"),
    path("filtrarestrela", filtrarestrela, name="filtrarestrela"),
    path("filtrargalaxia", filtrargalaxia, name="filtrargalaxia"),
    path("filtrarplaneta", filtrarplaneta, name="filtrarplaneta")
]
