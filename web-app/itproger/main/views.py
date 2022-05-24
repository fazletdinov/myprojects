from django.shortcuts import render

data = {
    'title': 'Главная страница',
    'values': ['Hello', 'Spaun', 'Bomjur', 'Sharik'],
    'obj': {'car': 'BMV', 'age': 18, 'hobby': 'Footbal'}
}

def index(request):
    return render(request, 'main/index.html', data)
def about(request):
    return render(request, 'main/about.html')
