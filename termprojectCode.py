import time
import random
import webbrowser
import subprocess
import speech_recognition as sr
import datetime
import wikipedia
import sys
import os
from weather import Weather, Unit
import smtplib
import codecs

#string
a = 'How you doin''?'
b = 'Greetings and salutations!'    
c = 'Whaddup.'
d = 'Would you like a hug? '
e = 'Are experiencing mood swings? '
f = 'It is ok to cry '
r = [a,b,c,d,e,f]                           #list

aa = 'Top of the morning to you! '
bb = 'Have a Lovely day! '
cc = 'Como Estas! '
dd = 'Namaste! '
ee = 'Holo! '  
greetings =(aa,bb,cc,dd,e)                  #tuple
   
class Personal_assistant:
    
    def __init__(self,passw):
        self.passw=passw
            
    def __str__(self): 
        return ('I am a command line assistant. My name is '+self.passw)
    
    def bootuppeebo(self):
        time.sleep(0.5)
        print()
        print('Starting PEEBO... ')
        print()
        time.sleep(0.5)
        print('Testing... ')
        time.sleep(0.25)
        print( 'DONE. ')
        time.sleep(0.25)
        print('------------------------------------------------------------------')
        time.sleep(0.5)
        print('------------------------------------------------------------------')
        print()
        time.sleep(1)
        print('I AM PEEBO! YOUR PERSONAL COMMAND LINE ASSISTANT! ' )
        print()
        time.sleep(1)
   
    def logon(self):
       while True:
           password='peebo123'
           username=input('Enter username: ')
           userpassword=input('Enter password: ')
           if userpassword==password:
               time.sleep(1)
               print(username)
               print('Login successful! ')
               break
           else:
               print('Incorrect password! ')     
        
    def greetings(self):

	    user = input('What is your name? ')
	    print()
	    time.sleep(1)
	    print(random.choice(greetings)+' '+user+' I will be your personal command line assistant. ')
	    time.sleep(1)
	    print(random.choice(r))
        
    def telljoke(self):  
        resultfile=open('jokess.txt','r')
        lines=resultfile.read().splitlines()
        res=random.choice(lines)
        print(res)
        
    def openurl(self): 	
	     new=2;  	
	     url=input('Enter url you want to open: ');   
	     webbrowser.open(url,new=new); 
         
    def openapps(self): 
        # Here the path for the applications to be opened should be changed according to the systems applications path
        a=eval(input('Enter number between 1-5:\n 1.Skype\n 2.Notepad\n 3.Microsoft Word\n 4.Microsoft Powerpoint\n 5.Wordpad\n Please enter a number: '))
        if a==1:
            subprocess.Popen(r'C:\Program Files (x86)\Skype\Phone\Skype.exe')              
        elif a==2:
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk')           
        elif a==3:
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016.lnk') 
        elif a==4:
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint 2016.lnk')            
        elif a==5:
            subprocess.Popen(r'C:\Program Files (x86)\Windows NT\Accessories\wordpad.exe')
                      
    def moodanalysis(self):
        mood=input('On a scale of 1 to 10 how do you feel today? ')
        print()
        if int(mood)<5:
            print('Confirmed')
            print('Your mood could be improved')
            print('I will call your family and friends to improve your mood')
            time.sleep(1)
            print('....CALLING....')
            time.sleep(1)
            print('Done')
            print()
    	    
        else:
    	    print('Confirmed ')
    	    time.sleep(1)
    	    print('Glad you are feeing well. ')
            
    def helpfile(self):
        print()
        print('> helpfile')
        print('Here is a list of the commands you are can use. ')
        print()
        print('Enter these          Operation of those functions')
        print('-----------------------------------------------') 
        print('helpfile   	         Show this help message ') 
        print('open maps  	         I will open google maps  ') 
        print('analyze mood              I will perform a mood check ')
        print('open url        	         I will open the url you type ')
        print('telljoke   	         I will tell you a joke ')
        print('open apps       	         I will open the applications you ask for ')
        print('personal diary            I will update your daily vlogs ')
        print('wikipedia search          I will do wikipedia search and give info for data you enter ')
        print('weather info   	         I will provide weather conditions for the place you want to know ')
        print('send email   	         I will emails for you ')
        print('exit   	                 I will shutdown ')
        
    def OpenGoogleMaps(self):
        message=input('Enter message: ')
        if ('google maps') in message:
            q = message
            words = {'google', 'maps'}                      #set        
            qwords = q.split()
            reswords  = [word for word in qwords if word.lower() not in words]
            result = ' '.join(reswords)
            # Here the path for chrome should be the path of that particular systems google chrome
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            
    def personaldairy(self):
        resultfile=codecs.open('diary.rtf','a','utf-8')
        now = datetime.datetime.now() 
        languages={'English':'en-US','Tamil':'ta-IN','Telugu':'te-IN','Afrikaana':'af-ZA','Malay':'ms-MY',
                   'Japanese':'ja-JP','Chinese':'cmn-Hans-CN','Korean':'ko-KR','Thai':'th-TH','Hindi':'hi-IN',
                   'Arabic':'ar-AE','Russian':'ru-RU','Greek':'el-GR','Urdu':'ur-IN','Turkish':'tr-TR',
                   'Vietnamese':'vi-VN','Sinhala':'si-LK','Polish':'pl-PL','Croatian':'hr-HR','Gujarati':'gu-IN',
                   'French':'fr-FR','Spanish':'es-US','German':'de-DE','Danish':'da-DK','Bengali':'bn-IN'}
        print('The available languages are')
        for i in languages:
           print(i, languages[i])
        command=input('enter language: ')  
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("SAY TODAYS LOG: ")
            audio=r.listen(source)
            print("TIMEs OVER")    
        try:
            print('\n'+now.strftime("DATE: %Y-%m-%d TIME: %H:%M"))
            print("TEXT: "+r.recognize_google(audio,language=languages[command])+'\n')
            l='\n'+now.strftime("DATE: %Y-%m-%d TIME: %H:%M")+'\n'
            r="\nTEXT: "+r.recognize_google(audio,language=languages[command])+'\n'
            resultfile.writelines(l+'\n'+r)
            resultfile.writelines('\n')
        except:
            print('Entered wrong request.')
            pass;
        resultfile.close()
        
    def wikipedia_search(self):
        while True:
            i=input('Enter 1. to perform wikipedia search. 2. exit')
            if i=='1':
                input1 = input("Q: ")
                try:
                    print(wikipedia.summary(input1))
                except:
                    print('ambiguity error')
            elif i=='2':
                return
    
    def weather_info(self):
        weather = Weather(unit=Unit.CELSIUS)

        place=input('Enter the area you want to check the weather: ')
        location = weather.lookup_by_location(place)
        condition = location.condition
        print(condition.date)
        print('I t will be '+condition.text)
        print(condition.temp+ u"\u2103")
    
    def send_email(self):
        try:    
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            username=input('enter username: ')
            password=input('enter password: ')
            server.login(username,password)
 
            msg = input('Enter the message to be sent: ')
            to_mail=input('Enter the email id the message should be sent to: ')
            server.sendmail(username,to_mail,msg)
            server.quit()
            print('done')
    
        except:
            print('error sending notification')
            server.quit()    
    
    def goodbye(self):
        sys.exit('Thanks!')
         
            
ob1=Personal_assistant('peebo')    
func_dict = {                                   #dictionary           
    'helpfile':ob1.helpfile,              	
	 'telljoke':ob1.telljoke,
    'open maps':ob1.OpenGoogleMaps,
	'analyze mood':ob1.moodanalysis,
    'open url':ob1.openurl,
    'open apps':ob1.openapps,
    'personal diary':ob1.personaldairy,
    'wikipedia search':ob1.wikipedia_search,
    'weather info':ob1.weather_info,
    'send email':ob1.send_email,
    'exit':ob1.goodbye
}  

ob1.logon()
ob1.bootuppeebo()
ob1.greetings()

def cmdprompt():
    input('Press enter to begin command prompt')
    print()
    print('Type helpfile to see a list of available commands')
    while True:
        if __name__=="__main__":
            command=input(">>")
            func_dict[command]()
cmdprompt()                      	   