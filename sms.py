 #!/usr/bin/python
import urllib2
import http.cookiejar as cookiejar
from getpass import getpass
import sys
import http
 
username = "UserNumber"
passwd = "Password"
message = "Water Level is Low Please refill"
number = "number"
message = "+".join(message.split(' '))
print ("entered to send sms")
#Logging into the SMS Site
url = 'http://site24.way2sms.com/Login1.action?'
data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
 
#For Cookies:
cj = cookiejar.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
# Adding Header detail:
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
def smssend():
    try:
        usock = opener.open(url, data)
    except IOError:
        print ("Error while logging in.")
        sys.exit(1)
     
     
    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
     
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print ("Error while sending message")
        

    print ("SMS has been sent.")
