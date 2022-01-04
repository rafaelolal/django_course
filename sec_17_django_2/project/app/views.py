from django.shortcuts import render

# from app.models import User
from app.forms import NewUserForm

# Create your views here.
def main_page(request):
    return render(request, 'app/main_page.html')

# Create your views here.
def index(request):
    form = NewUserForm()

    if request.method == 'POST': # meaning someone submitted
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return main_page(request)

        else:
            print('FORM NOT VALID')

    return render(request, 'app/index.html', {'form': form})