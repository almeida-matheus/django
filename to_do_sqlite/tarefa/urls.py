from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path('tarefas/',views.show_add_tarefa), #views.nome da funcao
    path('tarefas/delete/<slug:id>',views.delete_tarefa),#caminho da url para excutar a funcao delete do views
    path('tarefas/edit/<int:id>',views.edit_tarefa),
    path('',RedirectView.as_view(url='tarefas/'))#quando redirecionar para a pagina principal ira ir pra url /tarefas
]