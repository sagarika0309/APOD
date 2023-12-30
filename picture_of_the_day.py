#streamlit run picture_of_the_day.py
import streamlit as st
import requests

st.markdown("<h1 style='text-align: center;'>AstroSnap: Celestial Wonders Unveiled</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explore the wonders of the cosmos with our daily astronomical showcase powered by NASA's vast image database. Immerse yourself in captivating celestial snapshots, from mesmerizing galaxies to stunning nebulae, bringing the beauty of the universe to your screen each day. Embark on a cosmic journey as you delve into the mysteries of space, right from the comfort of your device.</p>", unsafe_allow_html=True)

option=st.selectbox('Explore Data:',['Latest Data','Specific Date Data'],index=None)

API_KEY='e6kAvQRkuoo0g3Lzu9GETvYCE09ZyfzdztQ6dGWX'
API_URL='https://api.nasa.gov/planetary/apod'



def get_latest_data(data):
	st.markdown(f"<h2 style='text-align: center;'>{data['title']}</h2>", unsafe_allow_html=True)
	image_url=data["url"]
	image=requests.get(image_url)
	if(image.status_code==200):
		file_name='latest_image.jpeg'
		with open (file_name,'wb') as f:
			f.write(image.content)
		st.image(file_name,width=720,output_format='JPEG')
	else:
		print("No image was generated")

	date=(f"Date:{data['date']}")
	st.write(date)
	st.write(f"Description:{data['explanation']}")


def get_specific_data():

	date=st.date_input("Select a date")

	params2={
		'api_key':API_KEY,
		'date':date
	}
	res=requests.get(API_URL,params=params2)
	if(res.status_code==200):
		data=res.json()
		st.markdown(f"<h2 style='text-align: center;'>{data['title']}</h2>", unsafe_allow_html=True)
		image_url=data["url"]
		image=requests.get(image_url)
		if(image.status_code==200):
			file_name='specific_image.jpeg'
			with open (file_name,'wb') as f:
				f.write(image.content)
			st.image(file_name,width=720,output_format='JPEG')
		else:
			print("No image was generated")
		date=(f"Date:{data['date']}")
		st.write(date)
		st.write(f"Description:{data['explanation']}")
		
	else:
		st.write("!!Unable to retrieve data!!")


if(option=='Latest Data'):
	params1={
		'api_key':API_KEY
	}
	res=requests.get(API_URL,params=params1)
	if(res.status_code==200):
		data=res.json()
		get_latest_data(data)
	else:
		st.write("!!Unable to retrieve data!!")
elif(option=='Specific Date Data'):
	get_specific_data()
