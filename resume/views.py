from resume.models import Bio, Contact_form, School, SkillSet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.
class CvView(ListView):
    model = Bio
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(CvView, self).get_context_data(**kwargs)
        context['education'] = School.objects.all()
        context['skills'] = SkillSet.objects.all()
        return context

class About(ListView):
    model = Bio
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['education'] = School.objects.all()
        context['skills'] = SkillSet.objects.all()
        return context

class Success(ListView):
    model = Bio
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super(Success, self).get_context_data(**kwargs)
        context['contact_form'] = Contact_form.objects.all()
        return context

class Contact(CreateView):
    model = Contact_form
    template_name = 'contact_me.html'
    fields = '__all__'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        super().form_valid(form)
        form.save()
        return super(Contact, self).form_valid(form)
