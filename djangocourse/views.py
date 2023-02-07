from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from djangocourse.models import Client, Message, DistributionList


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'middle_name', 'email', 'comment')
    success_url = reverse_lazy('djangocourse:client')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('djangocourse:client')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'middle_name', 'email', 'comment')
    success_url = reverse_lazy('djangocourse:client')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('theme', 'text')
    success_url = reverse_lazy('djangocourse:message')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('djangocourse:message')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('theme', 'text')
    success_url = reverse_lazy('djangocourse:message')


class DistributionListView(ListView):
    model = DistributionList


class DistributionCreateView(CreateView):
    model = DistributionList
    fields = ('__all__')
    success_url = reverse_lazy('djangocourse:distribution')


class DistributionUpdateView(UpdateView):
    model = DistributionList
    fields = ('__all__')
    success_url = reverse_lazy('djangocourse:distribution')


class DistributionDeleteView(DeleteView):
    model = DistributionList
    success_url = reverse_lazy('djangocourse:distribution')