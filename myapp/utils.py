import requests
import pandas as pd
import numpy as np

def get_avg_diameter(d, *args):
	s = 0.00
	for x,y in d.items():
		s += y 
	return (s/2)


def this_main(START_DATE, END_DATE, *args):
	API_KEY = "QtlD0PMOlMYXcN3HS5QZeX0AmKIVvw0opRlT9ivq"
	org_url = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+START_DATE+"&end_date="+END_DATE+"&api_key="+API_KEY
	r = requests.get(org_url)
	data = r.json()


	my_temp_dict = {}
	arr_name = []
	arr_diameter = []
	arr_date = []
	arr_velocity = []
	arr_closest = []

	for x,y in data['near_earth_objects'].items():
		# print("Dated at:", x)
		# print('Name:\nEstimated Diameter in KM:')
		for each in y:
			# print('Name: ', each['name'])
			arr_name.append(each['name'])
			# print(each['estimated_diameter']['kilometers'], 'KM')
			x = get_avg_diameter(each['estimated_diameter']['kilometers'])
			# print('Avg. estimated:', x, 'KM')
			arr_diameter.append(np.float64(x))
			for every in each['close_approach_data']:
				# print('Dated at:', every['close_approach_date'])
				arr_date.append(np.datetime64(every['close_approach_date']))
				arr_closest.append(np.float64(every['miss_distance']['kilometers']))
				# print('Relative Velocity: ',every['relative_velocity']['kilometers_per_second'], 'KM/s')
				arr_velocity.append(np.float64(every['relative_velocity']['kilometers_per_second']))


	my_temp_dict['name'] = arr_name
	my_temp_dict['date'] = arr_date
	my_temp_dict['average_diameter'] = arr_diameter
	my_temp_dict['velocity'] = arr_velocity
	my_temp_dict['miss_distance'] = arr_closest

	# print(my_temp_dict)

	df = pd.DataFrame(my_temp_dict)
	# df.to_csv('neo-nasa.csv', encoding='utf-8', index=False)
	# print(df.head())
	# print(df.info())
	# print(df.describe())
	# print(df['velocity'].astype('float64').max())
	# print(df.loc[df['velocity'].idxmax()])
	# print(df['velocity'].head())
	# print(df['name'].head())
	# print(df['date'].head())
	# print(df['average_diameter'].head())
	x = df.groupby('date').count().reset_index()
	y = df.groupby('date').mean()['average_diameter'].reset_index()
	# y = x['name']
	# x = x['date']
	# plt.plot(x[])
	# print(x['velocity'])
	# print(x)
	fastest_asteroid = df.loc[df['velocity'].idxmax()]
	closest_asteroid = df.loc[df['miss_distance'].idxmin()]

	return (x, fastest_asteroid, closest_asteroid, y)

# plt.hist(x['date'], x['velocity'])
# print(x['date'])
'''
plt.plot(x['date'], x['velocity'])
plt.xlabel('Date')
plt.ylabel('Asteriod Occurrences')

textstr = 'Fastest Asteroid: '+str(fastest_asteroid['name'])+' on '+str(fastest_asteroid['date'])[:10]+' at '+str(fastest_asteroid['velocity'])+' KM/s'+'\n'+'Closest Asteroid: '+str(closest['name'])+' on '+str(closest['date'])[:10]+' at '+str(closest['velocity'])+' KM/s'
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.5)
plt.figtext(0.05, 0.95, textstr, fontsize=12,
        verticalalignment='top', bbox=props)
# print(df.groupby('date').mean())
# fileHandle.close()
plt.show()
'''