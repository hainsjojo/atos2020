from django import forms


class Searchpost(forms.Form):
	search = forms.CharField(widget=forms.TextInput(attrs={'style': 'margin: 10px;'}))


Time_slots= [
    ('12:00:00', '12:00'),
    ('13:00:00', '1:00'),
    ('14:00:00', '2:00'),
    ('15:00:00', '3:00'),
    ('16:00:00', '4:00'),
    ('17:00:00', '5:00'),
    ('18:00:00', '6:00'),
    ('19:00:00', '7:00'),
    ('20:00:00', '8:00'),
    ('21:00:00', '9:00'),
    ('22:00:00', '10:00'),
    ('23:00:00', '11:00'),

   ]

Date_slots= [
	('01','1'),
	('02','2'),
	('03','3'),
	('04','4'),
	('05','5'),
	('06','6'),
	('07','7'),

	]


class HomeForm(forms.Form):
	my_date= forms.CharField(label='Date ', widget=forms.Select(choices=Date_slots, attrs={'style': 'margin: 10px;'}))  
	my_time= forms.CharField(label='Time', widget=forms.Select(choices=Time_slots, attrs={'style': 'margin: 10px;'}))





