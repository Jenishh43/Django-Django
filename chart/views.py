from django.shortcuts import render
from django.utils import timezone
from .models import Chart

# Create your views here.
def chart_list(request):
    charts = Chart.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chart/chart_list.html',{'charts': charts})