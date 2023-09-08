from django.shortcuts import render , redirect
from store.models import Store
from store.forms import StoreForm
# Create your views here.


def store(request):
    template_html = 'store.html'
    stores = Store.objects.all()
    
    return render(request , template_html, {'stores' : stores} )



def create_store(request):


    templates_html = 'create_store.html'
    form = StoreForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('store:store')
        else:
            print(form.errors)

    return render(request, templates_html, {'form': form})


