# views.py

from django.shortcuts import render, redirect
from .models import Pao

def registrar_paes(request):
    if request.method == 'POST':
        quantidade = request.POST.get('quantidade')
        # Verificar se a quantidade é um número válido
        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                raise ValueError("A quantidade não pode ser negativa")
        except ValueError:
            return render(request, 'registrar_paes.html', {'error_message': 'Quantidade inválida'})

        # Atualizar a quantidade de pães feitos
        pao = Pao.objects.first()
        if pao:
            pao.quantidade += quantidade
            pao.save()
        else:
            Pao.objects.create(quantidade=quantidade)

        # Redirecionar de volta para a página de registro
        return redirect('registrar_paes')

    return render(request, 'registrar_paes.html')
