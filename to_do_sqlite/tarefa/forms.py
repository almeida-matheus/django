from django import forms
from .models import TarefaBd

class ConteudoForm(forms.ModelForm):
    class Meta:
        model=TarefaBd
        fields='__all__' #mostrar todos os campos do formulario
    
    '''
    def __init__(self, *args, **kwargs):
        super(ConteudoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Conteúdo...'
    })
    '''
    def __init__(self, *args, **kwargs):
        super(ConteudoForm, self).__init__(*args, **kwargs)
        self.fields['conteudo'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Conteúdo...'
    })