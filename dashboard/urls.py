from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tickets', views.ticketpage, name='tickets'),
    path('buy/<int:ticket_id>', views.buy_ticket, name='buy_ticket'),
    path('order/<int:order_id>', views.order_detail, name='order_detail'),
    path('order', views.order, name='order')
]
