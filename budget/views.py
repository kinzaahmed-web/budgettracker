from django.shortcuts import render, get_object_or_404
from .models import Project, Category, Expense
from django.views.generic import CreateView
from django.utils.text import slugify
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import ExpenseForm, CreateUserForm
import json
from json import dumps 

def home(request):
	return render(request, "budget/home.html", {})

def project_list(request):
    project_list = request.user.project.all()
    return render(request, 'budget/project-list.html', {'project_list': project_list})

def project_detail(request, project_slug):
    # fetch the correct project
    project = get_object_or_404(Project, slug=project_slug)
    p = Project()
    if project not in request.user.project.all():
        return HttpResponseRedirect('list/')

    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        return render(request, 'budget/project-detail.html', {'project': project, 'expense_list': project.expenses.all().order_by('-date'), 'category_list': category_list})

    elif request.method == 'POST':
        # process the form
        form = ExpenseForm(request.POST)
        print(form.errors)
        if form.is_valid():
            date = form.cleaned_data['date']
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(Category, project=project, name=category_name)
            expense = Expense(
                project=project,
                date=date,
                title=title,
                amount=amount,
                category=category
                )
            expense.save()
        return HttpResponseRedirect(project_slug)

    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Expense, id=id)
        expense.delete()

        return HttpResponse('')

    return render(request, project_slug, {'form': form})

    
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget/add-project.html'
    fields = ('name', 'budget')

    # This method is an override method
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.user.project.add(self.object)

        # grabs the categories via the hidden input field 
        categories = self.request.POST['categoriesString'].split(',')

        # for every category we want to create a new category which is bound to the current project 
        for category in categories:
            # create and save new project
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())
    
    # we're using slug to return the correct path
    def get_success_url(self):
        return slugify(self.request.POST['name'])