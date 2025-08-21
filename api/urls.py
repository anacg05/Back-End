from django.urls import path
from .views import *    # asteriscos importa todos

urlpatterns = [
    path('autores', AutoresView.as_view()),
    path('autores/lista', visu_autor),
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view())
]

