from django.urls import  include, path
from .views import (home,
    lista_pessoas,
    lista_veiculos, 
    lista_mov_rotativos,
    lista_mensalista,
    lista_mov_mensalista,
    pessoa_novo,
    veiculo_novo,
    mov_rotativos_novo,
    mensalista_novo,
    mov_mensalista_novo,
    pessoa_update,
    veiculo_update,
    mov_rotativos_update,
    mensalista_update,
    mov_mensalista_update,
    pessoa_delete,
    veiculo_delete,
    mov_rotativos_delete,
    mensalista_delete,
    mov_mensalista_delete
    
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name = 'core_lista_pessoas'),
    path('pessoa-novo/', pessoa_novo, name = 'core_pessoa_novo'),
    path('pessoa-update/<int:id>', pessoa_update, name = 'core_pessoa_update'),
    path('pessoa-delete/<int:id>', pessoa_delete, name = 'core_pessoa_delete'),

    path('veiculos/', lista_veiculos, name = 'core_lista_veiculos'),
    path('veiculo-novo/', veiculo_novo, name = 'core_veiculo_novo'),
    path('veiculo-update/<int:id>', veiculo_update, name = 'core_veiculo_update'),
    path('veiculo-delete/<int:id>', veiculo_delete, name = 'core_veiculo_delete'),

    path('mov-rotativo/', lista_mov_rotativos, name = 'core_lista_mov_rotativos'),
    path('mov-rotativo-novo/', mov_rotativos_novo, name = 'core_mov_rotativos_novo'),
    path('mov-rotativo-update/<int:id>', mov_rotativos_update, name = 'core_mov_rotativos_update'),
    path('mov-rotativo-delete/<int:id>', mov_rotativos_delete, name = 'core_mov_rotativos_delete'),

    path('mensalistas/', lista_mensalista, name = 'core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo, name = 'core_mensalista_novo'),
    path('mensalista-update/<int:id>', mensalista_update, name = 'core_mensalista_update'),
    path('mensalista-delete/<int:id>', mensalista_delete, name = 'core_mensalista_delete'),
    
    path('mov-mensalista/', lista_mov_mensalista, name = 'core_lista_mov_mensalista'),
    path('mov-mensalista-novo/', mov_mensalista_novo, name = 'core_mov_mensalista_novo'),
    path('mov-mensalista-update/<int:id>', mov_mensalista_update, name = 'core_mov_mensalista_update'),
    path('mov-mensalista-delete/<int:id>', mov_mensalista_delete, name = 'core_mov_mensalista_delete'),
]