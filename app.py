import requests
import xml.dom.minidom
import open_content

#BY ME
# set the params:

dataList = []
dataList = open_content.csv_to_dict(r'/data.csv')

time_list = []
message_list = []
url_list = []
temp_dict = []
temp_dict = open_content.csv_to_dict(r'/data.csv')
for line in temp_dict:
    time_list.append(line['ï»¿TIME'])
    message_list.append(line['MESSAGE'])
    url_list.append(line['URL'])

data_d = {
            'time_list' : time_list,
            'message_list' : message_list,
            'url_list' : url_list
        }

ipaddr = "192.168.137.102" # enter your speaker IP address here 
url = data_d["url_list"][0] # enter the URL of the file you want to play here
service = "service" 
reason = "reason"
message =  data_d["message_list"][0]
key = "SlP3uE5Oxz1X8yrcrCdxGWPCJpyleZih" # enter your API key here 
volumeVal = "30" # enter volume here, a number between 10 and 70

# form and send the /speaker POST request

sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

# print a pretty version of the response - not required but can be helpful for reading errors if they occur

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)
