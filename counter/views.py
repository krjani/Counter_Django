from django.shortcuts import render

# Create your views here.

def counter(request):
    initial = request.session.get('count',0)
    count = initial + 1
    request.session['count'] = count
    return render(request,'counter/count.html',{'count':count})