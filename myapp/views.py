import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .forms import MyInputForm
from .utils import this_main
# Create your views here.


def get_dates(request):
	if request.method == 'POST':
		form = MyInputForm(request.POST or None)
		if form.is_valid():
			START_DATE = form.cleaned_data['start_date'].strftime('%Y-%m-%d')
			END_DATE = form.cleaned_data['end_date'].strftime('%Y-%m-%d')
			return redirect('show', date1=START_DATE, date2=END_DATE)
			# print(START_DATE, END_DATE)
			# r = requests.get()
	else:
		form = MyInputForm()
	context = {'form': form, 'inp': 1,}
	return render(request, 'inp.html', context)

def show_data(request, date1, date2):
	st_dt, ed_dt = date1, date2
	# print(st_dt, ed_dt)
	x, fastest_asteroid, closest_asteroid, y = this_main(st_dt, ed_dt)
	# print(x)
	temp = x.to_dict('list')['date']
	dates = []
	for each in temp:
		dates.append(str((each))[:10])
	context = {
		'DATES': dates, 'OCCRS': x.to_dict('list')['name'], 'VAR2': fastest_asteroid.to_dict(),
		'VAR3': closest_asteroid.to_dict(), 'VAR4': zip(y.to_dict('list')['date'], y.to_dict('list')['average_diameter']),
		'VAR5': zip(dates, x.to_dict('list')['name']),
	}
	# print(closest_asteroid)
	# print(x.to_dict('list'))
	# print(fastest_asteroid.to_dict('list'))
	# print(closest_asteroid.to_dict('list'))
	return render(request, 'inp.html', context)
