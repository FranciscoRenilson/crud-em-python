from django.urls import path
from .views import list_pizzas, create_pizza, update_pizza, delete_pizza

urlpatterns = [
    path('', list_pizzas, name='list_pizzas'),  # cria a lista de pizzas
    path('new', create_pizza, name='create_pizzas'),  # torna possível cadastrar novas pizzas
    path('update/<int:id>/', update_pizza, name='update_pizzas'),
    path('delete/<int:id>/', delete_pizza, name='delete_pizzas'),
]


