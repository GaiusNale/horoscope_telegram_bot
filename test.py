# import requests

# def get_horoscope(sign, day):
#     params = {
#         'sign': sign,
#         'day': day,
#     }

#         # Send the request to the API
#     response = requests.post('https://aztro.sameerkumar.website/', params=params)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the JSON response
#         horoscope_data = response.json()
        
#         # Print the horoscope details
#         print(f"Horoscope for {sign.capitalize()} on {day.capitalize()}:")
#         print(f"Date Range: {horoscope_data['date_range']}")
#         print(f"Current Date: {horoscope_data['current_date']}")
#         print(f"Description: {horoscope_data['description']}")
#         print(f"Compatibility: {horoscope_data['compatibility']}")
#         print(f"Mood: {horoscope_data['mood']}")
#         print(f"Color: {horoscope_data['color']}")
#         print(f"Lucky Number: {horoscope_data['lucky_number']}")
#         print(f"Lucky Time: {horoscope_data['lucky_time']}")
#     else:
#         print ("Error")

# get_horoscope('aries', 'today')