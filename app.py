import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt","w")
file.write("they are currently "+
            str(result["number"]) + "astonauts on the ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p["name"]+" - on board" + "\n")
g = geocoder.ip('me')
file.write("\nyour latitude and longtitude is " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")
screen = turtle.Screen()
screen.setup(1200,609)
screen.setworldcoordinates(-180,-90,180,90)
map_img = "C:/Users/yousef/Desktop/tracker_2d_1/map.gif"
iss_img = "C:/Users/yousef/Desktop/tracker_2d_1/iss1.gif" 
screen.bgpic(map_img)
screen.register_shape(iss_img)
iss = turtle.Turtle()
iss.shape(iss_img)
iss.setheading(45)
iss.penup()

while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    
    lat = float(lat)
    lon = float(lon)
    print("\n latitude : "+str(lat) +"\n longitude : "+ str(lon))
    iss.goto(lon,lat)
    time.sleep(2)
    if str(f'[{lat}, {lon}]') == str(g.latlng) :
        pen = turtle.Turtle()
        pen.write("The iss is over your head right now !", font=("Calibri", 8, "bold"))