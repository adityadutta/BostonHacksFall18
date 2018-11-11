import requests
import xml.dom.minidom

#BY ME
# set the params:

ipaddr = "192.168.137.102" # enter your speaker IP address here 
url = "http://www.nasa.gov/mp3/590331main_ringtone_smallStep.mp3" # enter the URL of the file you want to play here
service = "service" 
reason = "reason"
message = "message"
key = "SlP3uE5Oxz1X8yrcrCdxGWPCJpyleZih" # enter your API key here 
volumeVal = "60" # enter volume here, a number between 10 and 70

# form and send the /speaker POST request

sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

# print a pretty version of the response - not required but can be helpful for reading errors if they occur

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)
