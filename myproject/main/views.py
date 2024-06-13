from django.shortcuts import render
from main.calculator import calculate

def home(request):
    result = None
    greeting = None

    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST.get('name')
            greeting = f"Hello, {name}."
        elif 'num1' in request.POST and 'num2' in request.POST:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')
            result = calculate(operation, num1, num2)

    return render(request, 'main/home.html', {'result': result, 'greeting': greeting})