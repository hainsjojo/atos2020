from django.shortcuts import render, HttpResponse, redirect
import requests
from datetime import date
from django.views.generic import View, TemplateView
from accounts.forms import HomeForm, Searchpost



# newhome is a simple view to render the login page, which will redirect the user to the main dashboard

def newhome(request):

	return render(request, 'accounts/login.html')
	return redirect(home)

# HomeView is a class-based view for the dashboard

class HomeView(TemplateView):
	tempname = 'accounts/index.html'


	def get(self, request):

# This creates a form from forms.py for submitting user input of time
		form = HomeForm()
# a dictionary is created to use form and search variables in the html using jinja template language
		return render(request, self.tempname, {'form': form })


	def post(self, request):

# the input is received from the user using POST method
		form = HomeForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['my_time']
			date_text = form.cleaned_data['my_date']
			
# the time stamp is then appended to the api link and parsed to get the data of that time

# this is for the card showing no. of people
		response = requests.get('http://127.0.0.1/csv-to-api/?source=http://127.0.0.1/dataset.csv&ds=2019-06-' + date_text +'%20' + text)
		a = response.json()
		for i in a:
			xx = i
		t = a[xx]

		gg = t['y']

		#-------------------------------------------------
		#this is for the current chart 
		counter = 1
		# limiter = text.split(':')[0]
		limiter = 11
		arr = []
		cc = int(limiter) 
		while (counter < 13):
			cc = cc + 1
			
			req = requests.get('http://127.0.0.1/csv-to-api/?source=http://127.0.0.1/dataset.csv&ds=2019-06-' + date_text + '%20' + str(cc) + ':00:00')
			n = req.json()
			for f in n:
				x1 = f
			val = n[x1]
			val2 = val['y']
			
			arr.append(val2)
			counter = counter + 1
		
	#to find the busiest time of the day 

		busy_time_indx = max(arr)
		busy_time = int(busy_time_indx) +1 

		
		#-------------------------------------------------
# predict.csv is from dates 2019-05-01 to 2019-07-05	
#for prediction chart
		new = '0' + str(int(date_text) +1) 
		
		p_counter = 1
		# limiter = text.split(':')[0]
		p_limit = 11
		arr2 = []
		int_l = int(p_limit) 

		while (p_counter < 13):
			int_l = int_l + 1 
			
			p_req = requests.get('http://127.0.0.1/csv-to-api/?source=http://127.0.0.1/predict.csv&ds=2019-06-' + str(new) + '%20' + str(int_l) + ':00:00')
			
			
			p_req.text
			j = p_req.json()
			
			for f in j:
				x1 = f
			

			p_val = j[x1]
			p_val2 = p_val['yhat']
			
			arr2.append(p_val2)
			p_counter = p_counter + 1



		args = 	{'form': form, 'text': text, 'y':t['y'], 'arr':arr, 'arr2':arr2, 'busy_time':busy_time}
		return render(request, self.tempname, args)


# for search pg to search encrypted mac id and find persons time stamps
class Search(TemplateView):
	tempname = 'accounts/core.html'

	def get(self, request):

		search = Searchpost()
		return render(request, self.tempname, {'search':search})

	def post(self, request):

		search = Searchpost(request.POST)

		if search.is_valid():
			s_text = search['search']
			val = s_text.value()
			
			mac_re = requests.get('http://127.0.0.1/csv-to-api/?source=http://127.0.0.1/macdb.csv&ds=' + val )
			mac_a = mac_re.json()
			mac_index = []
			for i in mac_a:
				xx = i
				mac_index.append(xx)
			mac_t = mac_a[xx]
			time_found = []
			for u in mac_index:
				mac_pp = mac_a[u]
				time_found.append(mac_pp['y'])


		arg = {'search':search, 'time_found':time_found}

		return render(request, self.tempname, arg)





