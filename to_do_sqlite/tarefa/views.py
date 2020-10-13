from django.shortcuts import render,redirect
from .models import TarefaBd
from .forms import ConteudoForm
# Create your views here.
'''
def show_tarefa(request):
    conteudo_bd=TarefaBd.objects.all()
    context={'conteudos_bd':conteudo_bd}
    return render(request,"lista.html",context)
'''
def show_add_tarefa(request):
    conteudo_bd=TarefaBd.objects.all()
    form=ConteudoForm()
    if request.method=='POST':
        form=ConteudoForm(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect ('/')
    context={
        'conteudos_bd':conteudo_bd,

        'form':form
        }
    return render(request,'lista.html',context)

def delete_tarefa(request,id):
    deleteTarefa=TarefaBd.objects.get(id=id)
    deleteTarefa.delete()
    return redirect('/')


def edit_tarefa(request,id):
    conteudo_bd=TarefaBd.objects.get(id=id)
    form=ConteudoForm(instance=conteudo_bd)
    if request.method=='POST':
        form=ConteudoForm(request.POST, instance=conteudo_bd)
        if form.is_valid():
            form=form.save()
            return redirect ('/')
    context={
        'conteudo_bd':conteudo_bd,

        'form':form
        }
    return render(request,'editar.html',context)

    