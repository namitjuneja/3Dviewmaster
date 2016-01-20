from PyQt4 import QtCore, QtGui
import sys
import urllib, json.

def GoogPlac(lat,lng,radius,types,key):
  #making the url
  AUTH_KEY = key
  LOCATION = str(lat) + "," + str(lng)
  RADIUS = str(radius)
  TYPES = types
  MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
  #grabbing the JSON result
  response = urllib.urlopen(MyUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  return jsonData

#This is a helper to grab the Json data that I want in a list
def IterJson(place):
  x = [place['name'], place['reference'], place['geometry']['location']['lat'], 
         place['geometry']['location']['lng'], place['vicinity']]
  return x

print GoogPlac(32.485008,-83.612936,500,"food","AIzaSyDB5Go3Ch4N-cDHLmUux7ZAinvCrofFdxw")



app = QtGui.QApplication([])





win = QtGui.QDialog()
win.resize(300,300)
layout = QtGui.QVBoxLayout(win)
scroll = QtGui.QScrollArea()
scroll.setWidgetResizable(True)
layout.addWidget(scroll)



scrollContents = QtGui.QWidget()
layout = QtGui.QVBoxLayout(scrollContents)
scroll.setWidget(scrollContents)

pix = QtGui.QPixmap("RH.png")

def createImage():
    label = QtGui.QLabel()
    label.setPixmap(pix)
    layout.addWidget(label)

createImage()

win.setWindowTitle("fORtHEwIN")
win.setGeometry(0, 0, 450, 450)

win.show()
win.raise_()
app.exec_()
