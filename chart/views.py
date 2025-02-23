from django.shortcuts import render

# Create your views here.
def chart_list(request):
    return render(request, 'chart/chart_list.html',{})