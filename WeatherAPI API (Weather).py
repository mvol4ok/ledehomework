#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[6]:


import requests


# In[ ]:





# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[11]:


url = "http://api.weatherapi.com/v1/current.json?key=45d5c414258a4e0e84222902221606&q=Lviv"
response = requests.get(url)
data = response.json()


# In[ ]:





# In[ ]:





# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[13]:


wind_mph = data['current']['wind_mph']
print(wind_mph, "miles per hour")


# In[19]:


temp_c = data['current']['temp_c']

feelslike_c = data['current']['feelslike_c']

difference= feelslike_c - temp_c

print( f'It feels,{difference},degrees celcius warmer than it actually is')


# In[ ]:





# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[39]:


moon_url = "https://api.weatherapi.com/v1/forecast.json?key=45d5c414258a4e0e84222902221606&q=Lviv&days=2"
moon_response = requests.get(moon_url)
moon_data = moon_response.json()

print(moon_data.keys())


# In[56]:


#print(moon_data['forecast']['forecastday'][1])

next_day = moon_data['forecast']['forecastday'][1]
next_day_illumination= next_day['astro']['moon_illumination']
print(next_day.keys())

print(next_day['astro'])

print(next_day['astro']['moon_illumination'])

print(f'The moon illumination for tomorrow will be {next_day_illumination}')



# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[72]:


temp_url = "https://api.weatherapi.com/v1/forecast.json?key=45d5c414258a4e0e84222902221606&q=Lviv&days=1"
temp_response = requests.get(temp_url)
temp_data = temp_response.json()

max_temp = temp_data["forecast"]['forecastday'][0]['day']['maxtemp_c']
min_temp = temp_data["forecast"]['forecastday'][0]['day']['mintemp_c']

print(f'Difference in temperature today was {max_temp - min_temp} celcius')


# In[ ]:





# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[ ]:


#rename the URL variable/ response variable and data variable!


# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[73]:


forecast_url = 'https://api.weatherapi.com/v1/forecast.json?key=45d5c414258a4e0e84222902221606&q=Lviv&days=3'
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()


# In[91]:


for day in forecast_data["forecast"]["forecastday"]:
    print(day['day']['maxtemp_c'])
    

    if day['day']['maxtemp_c'] >= 30:
        print("It is hot!")
    elif day['day']['maxtemp_c'] <= 18:
        print("It is cold!")
    else:
        print("It is warm!")


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[ ]:


#Can't access unless you pay money for subscription 


# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[105]:


biggest_number_of_them_all = 0
day_with_hottest_temp = ''

for item_in_forecast in forecast_data["forecast"]["forecastday"]:

    print(f"Im looking at: {item_in_forecast['day']['maxtemp_c']}")
    print(f"Biggest one I remember is {biggest_number_of_them_all}")
    print('--------------')

    if item_in_forecast['day']['maxtemp_c'] > biggest_number_of_them_all:
        biggest_number_of_them_all = item_in_forecast['day']['maxtemp_c']
        day_with_hottest_temp = item_in_forecast['date']
    

print(biggest_number_of_them_all)
print(day_with_hottest_temp)



# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[119]:


miami_url = "https://api.weatherapi.com/v1/forecast.json?key=45d5c414258a4e0e84222902221606&q=Miami&days=1"
miami_response = requests.get(miami_url)
miami_data = miami_response.json()

for time in miami_data['forecast']['forecastday'][0]['hour']:
    if time['cloud'] > 50:
        print(f"The temperature is {time['temp_c']} and cloudy")
    else:
        print(f"The temperature is {time['temp_c']}" )


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[126]:


count = 0 

for time in miami_data['forecast']['forecastday'][0]['hour']:
    if time['temp_f'] > 85:
      count  = count + 1
 
 
print(f"{count/ len(miami_data['forecast']['forecastday'][0]['hour']):.1%}")


        


# In[ ]:





# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[ ]:


#$4 dollars per month


# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[ ]:


#Create another account

