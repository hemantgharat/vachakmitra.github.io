import speech_recognition as sr
import time
import colorama as cl
cl.init(autoreset=True)
result=[]
para="Life is good and beautiful"
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('Read the below text...\n')
        time.sleep(1)
        print(para)
        voice = listener.listen(source,timeout=5,phrase_time_limit=5)
        print(type(voice))
        command = listener.recognize_google(voice,language='en-US')
        print("\nYour Comment- ",command)
        text1=para.lower()
        text2=command.lower()
        text=text1.split()
        voice=text2.split()
        for i,j in zip(voice,text):
            if i == j:
                result.append(cl.Fore.GREEN+j)
            else:
                result.append(cl.Fore.RED+j)
                continue
        print(" ".join(result))
        cl.Fore.autoreset=True
except:
    print("Something went wrong")
        
