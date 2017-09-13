from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from .models import *


# Create your views here.

def index(request):
    return render(request, 'hr/index.html')




class PositionAdd(CreateView):
    model = Position
    fields = ['name', 'description', 'requirement', 'location', 'salary', 'is_on']
    success_url = reverse_lazy('hr:position_list')


class PositionDelete(DeleteView):
    model = Position
    success_url = reverse_lazy('hr:position_list')
    pk_url_kwarg = 'position_id'


class PositionEdit(UpdateView):
    model = Position
    fields = ['name', 'description', 'requirement', 'location', 'salary', 'is_on', 'comment']
    pk_url_kwarg = 'position_id'


class PositionList(ListView):
    model = Position
    context_object_name = 'position_list'


class PositionDetail(DetailView):
    model = Position
    pk_url_kwarg = 'position_id'

    def get_context_data(self, **kwargs):
        context = super(PositionDetail, self).get_context_data(**kwargs)
        context['staff_list'] = Staff.objects.all()
        return context


class StaffAdd(CreateView):
    model = Staff
    fields = ['name_en', 'name_cn', 'sex', 'department', 'position', 'email', 'cellphone', 'is_on']


class StaffDelete(DeleteView):
    model = Staff
    success_url = reverse_lazy('hr:staff_list')
    pk_url_kwarg = 'staff_id'


class StaffEdit(UpdateView):
    model = Staff
    fields = ['name_en', 'name_cn', 'sex', 'department', 'position', 'email', 'cellphone', 'is_on', 'phone', 'address',
              'qq', 'wechat']
    pk_url_kwarg = 'staff_id'


class StaffList(ListView):
    model = Staff


class StaffDetail(DetailView):
    model = Staff
    pk_url_kwarg = 'staff_id'
