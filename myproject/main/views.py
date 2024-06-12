from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return render(request, 'home.html', {'name': name})
    return render(request, 'home.html')