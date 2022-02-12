import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
Information needed for a fare
'''
d = st.date_input("On which date do you need a ride")
st.write("Date",d)
hour = st.number_input("What time do you need the ride")
st.write("Hour", hour)
time = st.number_input("What minute do you need the ride")
st.write("Time", time)
pickup_longitude = st.number_input("Pickup Longitude")
st.write("Pickup Longitude", pickup_longitude)
pickup_latitude = st.number_input("Pickup Latitude")
st.write("Pickup Latitude", pickup_latitude)
dropoff_longitude = st.number_input("Dropoff Longitude")
st.write("Dropoff Longitude", dropoff_longitude)
dropoff_latitude = st.number_input("Dropoff Latitude")
st.write("Dropoff Latitude",dropoff_latitude)
passenger_count = st.number_input("Passengers")
st.write("Passengers",passenger_count)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://lewagon-taxi-fare-7uhpc5vsza-ez.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

date_time = f'{d} {int(hour)}:{int(time)}:00'

params = {
    "pickup_datetime":date_time,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude" : pickup_latitude,
    "dropoff_longitude" : dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count" : int(passenger_count)
}
st.write(params)
response = requests.get(url,params=params).json()
st.write("Fare",response["fare"])
