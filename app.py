import requests
import xml.dom.minidom

#BY ME
# set the params:



def speak(url):
    ipaddr = "192.168.137.102" # enter your speaker IP address here 
    url = url # enter the URL of the file you want to play here
    service = "service" 
    reason = "reason"
    message = "message"
    key = "SlP3uE5Oxz1X8yrcrCdxGWPCJpyleZih" # enter your API key here 
    volumeVal = "50" # enter volume here, a number between 10 and 70

    voice_line(ipaddr,url,service,reason,message,key,volumeVal)
    
def voice_line(ipaddr,url,service,reason,message,key,volumeVal):

    sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
    send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

    # print a pretty version of the response - not required but can be helpful for reading errors if they occur

    print("<Speaking>")

