from django.shortcuts import render, get_object_or_404, redirect
from .models import Chart
from django.utils import timezone
from .forms import ChartForm

# Create your views here.
def chart_list(request):
    charts = Chart.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chart/chart_list.html',{'charts': charts})

def chart_detail(request, pk):
    # Chart.objects.get(pk=pk)
    chart = get_object_or_404(Chart, pk=pk)
    return render(request, 'chart/chart_details.html', {'chart': chart})

def chart_new(request):
    if request.method == "POST":
        form = ChartForm(request.POST)
        if form.is_valid():
            chart = form.save(commit=False)
            chart.author = request.user
            chart.published_date = timezone.now()
            chart.save()
        return redirect('chart_detail', pk=chart.pk)
    else:
        form = ChartForm()
    return render(request, 'chart/chart_edit.html', {'form': form})

def chart_edit(request, pk):
    chart = get_object_or_404(Chart, pk=pk)
    if request.method == "POST":
        form = ChartForm(instance=chart)
        if form.is_valid():
            chart = form.save(commit=False)
            chart.author = request.user
            chart.published_date = timezone.now()
            chart.save()
        return redirect('chart_detail', pk=chart.pk)
    else:
        form = ChartForm(instance=chart)
    return render(request, 'chart/chart_edit.html', {'form': form})