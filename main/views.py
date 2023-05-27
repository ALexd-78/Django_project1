from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from main.models import Student


def index(request):
    context = {
        'object_list': Student.objects.all()[:3],
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)

class StudentListView(generic.ListView):
    model = Student
    extra_context = {
        'title': 'Список студентов'
    }



# def students(request):
#     context = {
#         'object_list': Student.objects.all(),
#         'title': 'Список студентов'
#     }
#     return render(request, 'main/index.html', context)


class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['title'] = context_data['object']
        #  #то же самое
        context_data['title'] = self.get_object()
        return context_data

# def student(request, pk):
#     student_item = Student.objects.get(pk=pk)
#     context = {
#         'object': student_item,
#         'title': student_item
#     }
#     return render(request, 'main/student_detail.html', context)

class StudentCreateView(generic.CreateView):
    model = Student
    fields = ('first_name', 'last_name',)
    success_url = reverse_lazy('main:students_list')

def contacts(request):
    '''контроллер'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'User {name} with email {email} send message: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)
