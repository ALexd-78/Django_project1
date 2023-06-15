from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject
from main.servises import send_deactivate_email


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
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        #  #то же самое
        # context_data['title'] = self.get_object()
        return context_data


class StudentCreateView(generic.CreateView):
    model = Student
    # fields = ('first_name', 'last_name',)
    form_class = StudentForm
    success_url = reverse_lazy('main:students_list')




class StudentUpdateView(generic.UpdateView):
    model = Student
    # fields = ('first_name', 'last_name',)
    form_class = StudentForm
    template_name = 'main/student_form_with_formset.html'
    # success_url = reverse_lazy('main:students_list')

    def get_success_url(self, *args, **kwargs):
        return reverse('main:students_update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('main:students_list')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
        # send_deactivate_email(student_item)
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:student_item', args=[student_item.pk]))

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
