from django.shortcuts import render, redirect
from .forms import SchemaForm, ColumnFormSet
from django.contrib.auth.decorators import login_required
from .models import Schema


def index(request):
    return render(request, 'main/index.html')

@login_required
def create_schema(request):
    if request.method == 'POST':
        form = SchemaForm(request.POST)
        formset = ColumnFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            schema = form.save(commit=False)
            schema.owner = request.user
            schema.save()
            formset.instance = schema
            formset.save()
            return redirect('schema_list')
    else:
        form = SchemaForm()
        formset = ColumnFormSet()
    return render(request, 'main/create_schema.html', {
        'form': form,
        'formset': formset
    })


@login_required
def user_dashboard(request):
    user_schemas = Schema.objects.filter(owner=request.user)
    return render(request, 'main/user_dashboard.html', {
        'user_schemas': user_schemas,
    })


@login_required
def after_login_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    return redirect('/')
