from django.shortcuts import render

# Create your views here.
def index (request):
    context ={ # isso é um dicionário
        'hello': 'hello world',
        'pj': 'poli junior',
    }
    return render(request,'core/index.html',context)

