from datetime import datetime
from gtts import gTTS
from playsound import playsound
import os
import webbrowser
import wikipedia

import datetime

count=0
def speak(text):
    global count
    myobj=gTTS(text=text,lang='en',slow=False)
    myobj.save("temp"+ str(count)+ ".mp3")
    #os.system("start temp"+ str(count)+".mp3")
    playsound("temp"+str(count)+".mp3")
    count= count+1


def wakeupsharon():

   

    name=input('enter the name of the user::')
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning')
        speak("good morning. hey {:s} this is sharon the interactive virtual assistant at your service! how may i help you".format(name))
    elif hour>=12 and hour<18:
        print('Good Afternoon')
        speak('good afternoon. hey {:s} this is sharon the interactive virtual assistant at your service! how may i help you'.format(name))
    else:
        print('Good Evening!')
        speak('good evening hey {:s} this is sharon the interactive virtual assistant at your service! how may i help you'.format(name))

    query=input("  Hey {:s} This is Sharon: The Interactive Virtual Assistant,at your service! how may I help you?   " .format(name)). lower()
    
    while True:

        if 'pictures' in query:
            codepath="Pictures"
            os.startfile(codepath)

        elif 'calculator' in query:
            os.system("start Calculator")

        elif 'music' in query:
            music_dir='Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[2]))
        
        elif 'google' in query:
            print('connecting....')
            webbrowser.open("https://www.google.com")

        elif 'youtube' in query:
            print("connectivity on..")
            webbrowser.open_new_tab("youtube.com")

        elif 'jec' in query:
            print('connectiong to the college site:')
            webbrowser.open('jecjabalpur.ac.in')

        elif 'fiitjee' in query:
            print('connecting you to the punjabi bagh center...')
            webbrowser.open_new_tab('fiitjeenorthwest.com')

        elif 'irctc' in query:
            webbrowser.open('www.irctc.co.in')

        elif 'air' in query:
            tpe=input('which..air travel would you prfer? private>> or government>>')
            if tpe=='private':
                x=input('which one would you prefer?....')
                webbrowser.open(('{:s}.com').format(x))
            else:
                print('connectivity....to airindia!!!')
                webbrowser.open('www.airindia.in')

        elif 'folder' in query:

            while True:
                hint=input("Hint the location:::")
                if 'document' in hint:
                    path="C:\\Users\\baksh\\Documents\\"
                    break
                elif 'desktop' in hint:
                    path="C:\\Users\\baksh\\Desktop\\"
                    break
                elif 'downloads' in hint:
                    path="C:\\Users\\baksh\\Downloads\\"
                    break
                else:
                    print("you have entered the wrong file location! please try again ! ")
                    continue

            fold=input('name the target folder... ')
            try:
                locate_folder=os.path.join(path,fold)
                print(os.startfile(locate_folder))
                file=input("Mention the target file ::")
                try:
                    print(os.startfile(locate_folder+"\\{:s}".format(file)))
                except Exception as e:
                    print("No, such file present in your PC")
            except Exception as e:
                print("NO, such folder is available on this PC")


        elif 'wikipedia' in query:
            srch=input('enter yout search please... ')

            try:
                result=wikipedia.summary(srch,sentences=5)
                print('connecting...')
                print(result)
                speak(result)
            except Exception as e:
                print('Sorry, there were multiple results or no result. Please try a different keyword.')
                speak('Sorry, there were multiple results or no result. Please try a different keyword.')

           
        
        another_command=input(" What may I help you with the next ? ")

        if 'n' in another_command:
            break
        else:
            query= another_command
            continue
        
        if 'n' :
            break


wakeupsharon()



        

    

