import streamlit as st
import datetime
import requests

'''
# NY Taxi Fare
'''

st.markdown('''
The purpose of this is to provide you with a fare based on your pickup and dropoff
locations, your pickup time and number of passengers.
''')

'''
Information needed for a fare
'''
d = st.date_input("On which date do you need a ride?")
st.write("Your Date",d)
#hour = st.number_input("What time do you need the ride")
#st.write("Hour", hour)
time = st.time_input("What time do you need the ride?")
st.write("Your Time", time)
pickup_longitude = st.number_input("Pickup Longitude")
st.write("Your Pickup Longitude", pickup_longitude)
pickup_latitude = st.number_input("Pickup Latitude")
st.write("Your Pickup Latitude", pickup_latitude)
dropoff_longitude = st.number_input("Dropoff Longitude")
st.write("Your Dropoff Longitude", dropoff_longitude)
dropoff_latitude = st.number_input("Dropoff Latitude")
st.write("Your Dropoff Latitude",dropoff_latitude)
passenger_count = st.number_input("Number of Passengers")
st.write("Your Passenger number",passenger_count)

url = 'https://lewagon-taxi-fare-7uhpc5vsza-ez.a.run.app/predict'

'''
## Your predicted fare can be found below
'''

date_time = f'{d} {time}'
'''
Based on your conditions:
'''
params = {
    "pickup_datetime":date_time,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude" : pickup_latitude,
    "dropoff_longitude" : dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count" : int(passenger_count)
}
st.write(params)
'''
Your predicted fare is
'''
response = requests.get(url,params=params).json()
st.write("Fare",response["fare"])
