from django.shortcuts import render, redirect
from .models import Pizza
from .forms import PizzaForm  # importa o formulário de pizza


def list_pizzas(request):  # acessa a lista de produtos no banco e devolve para o navegador
    pizzas = Pizza.objects.all()  # este comando em particular é equivalente a um 'SELECT * FROM pizza' em sql
    return render(request, 'pizzas.html', {'pizzas': pizzas})  # devolverá um template para exibir o conteúdo


def create_pizza(request):
    form = PizzaForm(request.POST or None)  # pega informações do request.POST, se for o primeiro acesso, cria um form
    # em branco. Se for entregue assim, dará erro. Se for preenchido, será redirecionado à list product.

    if form.is_valid():
        form.save()
        return redirect('list_pizzas')

    return render(request, 'pizzas-form.html', {'form': form})


def update_pizza(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm(request.POST or None, instance=pizza)

    if form.is_valid():
        form.save()
        return redirect('list_pizzas')
    return render(request, 'pizzas-form.html', {'form': form, 'pizza': pizza})


def delete_pizza(request, id):
    pizza = Pizza.objects.get(id=id)

    if request.method == 'POST':
        pizza.delete()
        return redirect('list_pizzas')

    return render(request, 'pizza-delete-confirm.html', {'pizza': pizza})
