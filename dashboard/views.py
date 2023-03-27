from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import UserDetail
from dashboard.models import Ticket, Event, Order


@login_required(login_url='login')
def dashboard(request):
    total_trips = UserDetail.objects.get(
        username=request.user.username).total_trips
    upcoming_trips = UserDetail.objects.get(
        username=request.user.username).upcoming_trips
    total_distance = UserDetail.objects.get(
        username=request.user.username).total_distance
    total_cost = UserDetail.objects.get(
        username=request.user.username).total_cost

    orders = Order.objects.all()
    return render(request, 'dashboard.html', {'total_trips': total_trips, 'upcoming_trips': upcoming_trips, 'total_distance': total_distance, 'total_cost': total_cost, 'orders': orders})


def ticketpage(request):
    tickets = Ticket.objects.all()

    return render(request, 'tickets.html', {'tickets': tickets})


def buy_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > ticket.quantity:
            return render(request, 'error.html', {'error': 'Not enough tickets available'})
        order = Order(user=request.user, ticket=ticket,
                      quantity=quantity, total_price=quantity*ticket.price)
        order.save()
        ticket.quantity -= quantity
        ticket.save()
        return redirect('order_detail', order_id=order.id)
    return render(request, 'buy.html', {'ticket': ticket})


def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_detail.html', {'order': order})


def settings(request):
    return render(request, 'settings.html')
