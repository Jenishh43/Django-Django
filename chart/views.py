from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Chart

# Create your views here.
def chart_list(request):
    charts = Chart.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chart/chart_list.html',{'charts': charts})

def chart_detail(request, pk):
    chart = get_object_or_404(Chart, pk=pk)
    return render(request, 'chart/chart_detail.html', {'chart': chart})