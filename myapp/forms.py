from django import forms

class MyInputForm(forms.Form):
	start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control',}))
	end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control',}))

	def clean(self):
		x = self.cleaned_data.get('start_date')
		y = self.cleaned_data.get('end_date')
		if (y-x).days < 0 or (y-x).days > 7:
			# print((y-x).days, "inside")
			raise forms.ValidationError("Invalid Date / Enter a range of 7 days.")
		# print((y-x).days, "outside")
		return self.cleaned_data