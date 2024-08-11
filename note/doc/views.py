from django.shortcuts import render
from doc.models import book

# Create your views here.
def home(request):
    result = book.objects.all()
    if request.method == "POST":
        t = request.POST.get('title')
        c = request.POST.get('content')

        if t and c:  # Check if all fields are provided
            obj = book(title=t,content=c)
            obj.save()
        result = book.objects.all()  # Refresh the result after insertion
        return render(request, 'index.html', {'ru': result, 'ob': obj})
    return render(request, 'index.html', {'ru': result})

