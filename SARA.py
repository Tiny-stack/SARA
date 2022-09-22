import pandas as pd
import numpy as np
import os
from csv import writer
from random import randint
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
from playsound import playsound
try:
    language = 'en'
    commands = {'openxampp': 'sudo xampp start','open android studio': 'android-studioopen eclipse','open eclipse':'eclipse','open sublime text':'subl','open chrome':'google-chrome-stable','open google chrome':'google-chrome-stable'}
    audio = {'open android studio':'opening android studio','open eclipse':'opening eclipse','open sublime text':'opening text editor sublime text','open chrome':'opening google chrome','open google chrome':'opening google chrome'}
    r = sr.Recognizer()
    rest=[",",".","*","&","^","%","#","@","!","'",'"',":"," "]
    logo = """ 
           ██████    ██  ██    █████    ████     █████
           ██▒▒▒▒    ██  ██    ██▒▒▒█  ██▒▒██    ██▒▒▒█
           ██████    ██  ██    █████▒  ██████    █████▒
           ▒▒▒▒██    ██  ██    ██▒▒▒   ██▒▒██    ██▒▒██
           ██████    ▒████▒    ██      ██  ██    ██  ▒██
           ▒▒▒▒▒▒ ██  ▒▒▒▒  ██ ▒▒ ██   ▒▒  ▒▒ ██ ▒▒   ▒▒
      """
    def clear():
        os.system('clear')
        print(logo)
    def SpeakText(mytext):
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        playsound("welcome.mp3")
        # Initialize the engine
        #engine = pyttsx3.init()
        #engine.say(command)
        #engine.runAndWait()
    # Loop infinitely for user to
    # speak
    wait = ['Please say something!','Talk to me','Ask me a question!','Hello! speak something','why are you so calm?']
    clear()
    z=""
    print("welcome sir! how can i help you?")
    SpeakText("welcome sir! how can i help you?")
    def hear():
        print("listening")
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                z = MyText
                if(MyText=="YES"):
                    print("You said:- ",MyText)
                    return True
                else:
                    print(MyText)
                    return MyText
        except sr.RequestError as e:
            SpeakText("Say that Again")
            return hear()
            #print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("I can't hear, Sorry!")
            SpeakText("I can't hear Sorry!")
            return hear()
    df=pd.read_csv('SARA.csv')
    print(df)
    size=df.shape
    print(size)
    clear()
    while True:
        try:
            with sr.Microphone() as source2:
                clear()
                print("___________________________________________________________\nCommand: ")
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize aulidio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                li = MyText.split()
                web = ['.com','.in','.org','.edu','.tech','.online']
                if(li[0]=='open'):
                    if(li[1][-4:] in web):
                        SpeakText("opening "+li[1][:-4])
                        os.system("xdg-open https://"+li[1])
                        clear()
                        continue
                    if(MyText=="exit"):
                        print("Exit")
                        print("Okay sir! Exiting! Have a nice day!")
                        SpeakText("Okay sir! Exiting! Have a nice day!")
                        exit()
                    else:
                        try:
                            SpeakText(audio[MyText])
                            os.system(commands[MyText])
                        except(KeyError):
                            SpeakText("Sorry! Command not found")
                        continue

                    """if(MyText=="open sublime text" or MyText=="open text editor"):
                        SpeakText("opening Text editor sublime text")
                        os.system("subl")
                        continue
                    if(MyText=="how are you"):
                        print("i am fine sir")
                        SpeakText("i am fine sir")
                        continue
                    if MyText == "clear screen":
                        clear()
                        SpeakText("Screen Cleared")
                        continue"""
                z = MyText
                #print("Did you say "+MyText)
               # SpeakText(MyText)
                
        except sr.RequestError as e:
            pass
            #print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("I can't hear, Sorry!")

        z=z.upper()
        print("    ",z)
        rest=[",",".","*","&","^","%","#","@","!","'",'"',":"," "]
        str2=""
        for char in z:
            if char in rest:
                continue
            str2+=char
        
        z=str2
        p=0
        flag=0
        q=0
        if len(z)==0:
            temp = randint(0,len(wait)-1)
            print(wait[temp])
            SpeakText(wait[temp])
            #playsound("audio/wait.mp3")
            continue
        if z.upper()=="EXIT":
            print("Responce: ",end="")
            print("Okk,we will Meet again soon...... Good bye!")
            SpeakText("Okay we will Meet again,soon, Good bye!")
            #playsound("audio/exit.mp3")
            break
        for i in range(size[0]):
            
            p=0
            que=df[['ques']][i:i+1]
            que=str(que).split()
            
            que=que[2:]
            string=""
            for char in que:
                string+=char
            string=string.upper()
            count=0
                    
            for j in string:
                try:
                    if j not in rest:
                        if z[count]==j:
                            p+=1
                except IndexError:
                    break
                count+=1
            try:
                if p/len(z)>0.80:
                    
                    try:
                        print("Responce: ",end="")
                        answer=df[['ans']][i:i+1]
                        answer=str(answer).split()
                        answer=answer[2:]
                        ko=i
                        
                        t=""
                        for i in answer:
                            t+=i+" "
                        print('(---',t,'---)')

                        print("Location in Forest: ",ko)
                        print("Correct Probability: ",round(p/len(string),2))
                        SpeakText(t)
                        #playsound("audio/ans_"+str(ko+1)+".mp3")
                        z=""
                        p=0
                        flag=1
                        break
                    except IndexError:
                        pass
            except ZeroDivisionError:
                print("Please Enter Some Ques: ")
                break
            q+=1
        if flag==0:
            print("I don't know can you tell me plaese?")
            SpeakText("I don't know, can you tell me please? ")
            if(hear()):
                print(i)
            
                print("Please speak the answer: ")
                SpeakText("please! speak the answer")
                ans = hear()
                print("Thanks You Sir!")
                SpeakText("Thank you Sir!")
                #playsound("audio/thank.mp3")
                del(df)
                with open('SARA.csv','a') as file:
                    write=writer(file)
                    write.writerow([z,ans])
                    file.close()
                df=pd.read_csv('SARA.csv')
                size=df.shape
                
            else:
                print("No problem I will find it later____")
                SpeakText("No problem I will find it later")

                #playsound("audio/nop.mp3")
except(Exception):
    print("Kindly check you internet connection And restart")
    playsound('check.mp3')

