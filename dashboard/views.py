from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import UserDetail
from dashboard.models import Ticket, Event, Order
from datetime import datetime


@login_required(login_url='login')
def dashboard(request):
    user = UserDetail.objects.get(username=request.user.username)
    total_trips = user.total_trips
    upcoming_trips = user.upcoming_trips
    total_distance = user.total_distance
    total_cost = user.total_cost

    total_order = 0
    orders = Order.objects.all()
    for order in orders:
        if order.user == request.user:
            total_order += 1

    user.total_cost = total_cost
    user.total_orders = total_order
    user.save()

    orders = Order.objects.all()
    return render(request, 'dashboard.html', {'total_trips': total_trips, 'upcoming_trips': upcoming_trips, 'total_distance': total_distance, 'total_cost': user.total_cost, 'total_orders': user.total_orders, 'orders': orders})


def ticketpage(request):
    tickets = Ticket.objects.all()

    return render(request, 'tickets.html', {'tickets': tickets})


def buy_ticket(request, ticket_id):
    user = UserDetail.objects.get(username=request.user.username)
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > ticket.quantity:
            return render(request, 'error.html', {'error': 'Not enough tickets available'})
        total_price = quantity * ticket.price
        order = Order(user=request.user, ticket=ticket,
                      quantity=quantity, total_price=total_price)
        order.save()
        ticket.quantity -= quantity
        ticket.save()

        user.total_trips += 1

        user.upcoming_trips += 1

        # convert ticket.event.date to datetime object
        # date = datetime.strptime(ticket.event.date, '%Y-%m-%d %H:%M:%S.%f')

        # if (date < datetime.now()):
        #     user.upcoming_trips -= 1

        user.total_distance += ticket.event.distance
        user.total_cost += total_price
        user.save()

        return redirect('order_detail', order_id=order.id)
    return render(request, 'buy.html', {'ticket': ticket})


def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_detail.html', {'order': order})


def order(request):
    orders = Order.objects.all()
    return render(request, 'order.html', {'orders': orders})


def settings(request):
    return render(request, 'settings.html')
