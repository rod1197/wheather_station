import tkinter as tk
import requests
import time
import pywhatkit as kit

global final_info
global final_data

# get weather 
def getWeather(): # function to get weather
    global final_info 
    global final_data
    # if key error occurs, then the city name is wrong
    try:
        city = textField.get() # get city name from text field
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f" # api link
        
        json_data = requests.get(api).json() # get data in json format
        condition = json_data['weather'][0]['main'] # main weather condition
        temp = int(json_data['main']['temp'] - 273.15) # temperature in celsius
        min_temp = int(json_data['main']['temp_min'] - 273.15) # minimum temperature in celsius
        max_temp = int(json_data['main']['temp_max'] - 273.15) # maximum temperature in celsius
        pressure = json_data['main']['pressure'] # pressure
        humidity = json_data['main']['humidity']   # humidity
        wind = json_data['wind']['speed'] # wind speed
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600)) # sunrise time
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600)) # sunset time

        final_info = condition + "\n" + str(temp) + "°C" # final info
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        label1.config(text = final_info) # show final info
        label2.config(text = final_data) # show final data
        label3.config(text = "") # clear label3

        # saving data to a file 
        with open('D:\AGH\python\weather_data.txt', 'w') as f: 
            f.write(final_info) 
            f.write(final_data)
        
        # saving data to a file in csv format
        with open('D:\AGH\python\weather_data.csv', 'w') as f:
            f.write('Weather, Temperature, Min Temp, Max Temp, Pressure, Humidity, Wind Speed, Sunrise, Sunset\n')
            f.write(final_info)
            f.write(final_data)
        
        # saving data in xml file but new row 
        with open('D:\AGH\python\weather_data.xml', 'w') as f:
            f.write('<xml version="1.0" encoding="UTF-8">') 
            f.write('')
            f.write('<weather>')
            f.write('')
            f.write('<condition>'+condition+'</condition>')
            f.write('')
            f.write('<temp>'+str(temp)+'</temp>')
            f.write('')
            f.write('<min_temp>'+str(min_temp)+'</min_temp>')
            f.write('')
            f.write('<max_temp>'+str(max_temp)+'</max_temp>')
            f.write('')
            f.write('<pressure>'+str(pressure)+'</pressure>')
            f.write('')
            f.write('<humidity>'+str(humidity)+'</humidity>')
            f.write('')
            f.write('<wind>'+str(wind)+'</wind>')
            f.write('')
            f.write('<sunrise>'+sunrise+'</sunrise>')
            f.write('')
            f.write('<sunset>'+sunset+'</sunset>')
            f.write('')
            f.write('</weather>')
            f.write('')
            f.write('</xml>')


        #show all searched cities in a list 
        with open('D:\AGH\python\weather_data.html', 'w') as f:
            f.write('<html>')
            f.write('')
            f.write('<table>')
            f.write('')
            f.write('<tr>')
            f.write('')
            f.write('<th>Weather</th>')
            f.write('')
            f.write('<th>Temperature</th>')
            f.write('')
            f.write('<th>Min Temp</th>')
            f.write('')
            f.write('<th>Max Temp</th>')
            f.write('')
            f.write('<th>Pressure</th>')
            f.write('')
            f.write('<th>Humidity</th>')
            f.write('')
            f.write('<th>Wind Speed</th>')
            f.write('')
            f.write('<th>Sunrise</th>')
            f.write('')
            f.write('<th>Sunset</th>')
            f.write('')
            f.write('</tr>')
            f.write('')
            f.write('<tr>')
            f.write('')
            f.write('<td>'+condition+'</td>')
            f.write('')
            f.write('<td>'+str(temp)+'</td>')
            f.write('')
            f.write('<td>'+str(min_temp)+'</td>')
            f.write('')
            f.write('<td>'+str(max_temp)+'</td>')
            f.write('')
            f.write('<td>'+str(pressure)+'</td>')
            f.write('')
            f.write('<td>'+str(humidity)+'</td>')
            f.write('')
            f.write('<td>'+str(wind)+'</td>')
            f.write('')
            f.write('<td>'+sunrise+'</td>')
            f.write('')
            f.write('<td>'+sunset+'</td>')
            f.write('')
            f.write('</tr>')
            f.write('')
            f.write('</table>')
            f.write('')
            f.write('</html>')
            f.write('')
            f.write('</html>')

            
    except KeyError:
        # if city name is wrong, then show a warning

        label1.config(text = "") # clear label1
        label2.config(text = "") # clear label2
        label3.config(text = "Wrong City Name") # show label3



# GUI

canvas = tk.Tk() # create a window
canvas.geometry("600x500") # set the size of the window
canvas.title("Weather App") # set the title of the window
f = ("poppins", 15, "bold") # set the font
t = ("poppins", 35, "bold") # set the font

# Text Field
textField = tk.Entry(canvas, justify='center', width = 20, font = t) # create a text field
textField.pack(pady = 20) # pack the text field
textField.focus() # set the focus on the text field
#textField.bind('<Return>', getWeather) # bind the enter key with the function getWeather
# get weather button
button = tk.Button(canvas, text = "Get Weather", font = f, command = getWeather, bg = "blue", fg = "white", width = 15) # create a button
button.pack(pady = 20) # pack the button

# Labels
label1 = tk.Label(canvas, font=t) # create a label
label1.pack() # pack the label
label2 = tk.Label(canvas, font=f)
label2.pack()

# wrong city name warning color yellow and black background
label3 = tk.Label(canvas, font=f, fg = "yellow", bg = "black")
label3.pack()

canvas.mainloop() # run the window

