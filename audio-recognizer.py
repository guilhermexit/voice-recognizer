import speech_recognition as sr
import pyttsx3 
import os
from time import sleep

robo = pyttsx3.init()
recon = sr.Recognizer()
resposta = ""


def bem_vindo():
    
    with sr.Microphone() as source:
        robo.say("Bem-vindo a Alimentéqui. Queremos te ajudar a sair da situação em que você se encontra.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        
def cadastro_nome():
    
    with sr.Microphone() as source:
       
        robo.say("Diga seu nome.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()  
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))  
    
def cadastro_email():
    with sr.Microphone() as source:
      
        robo.say("Diga seu email.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()    
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))  
        
        
def cadastro_senha():
    with sr.Microphone() as source:
      
        robo.say("Diga sua senha.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()    
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))     
        
        
def login():
    
    with sr.Microphone() as source:
      
        robo.say("Faça seu login. Digite seu email.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()    
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))     
        robo.say("Ótimo. Agora digite sua senha.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()    
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))   
        
        
def area_plantio():
    
    with sr.Microphone() as source:
        
        robo.say("Ok. Nos conte qual o tamanho da área do seu plantio?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))
        
def regiao():
    
    with sr.Microphone() as source:
        
        robo.say("Nos diga em que região do Brasil você mora?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))
        
def investir():
    
    with sr.Microphone() as source:
        
        robo.say("Ok. Quantos reais você teria disponível para investir no plantio?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))

def tempo():
    
    with sr.Microphone() as source:
        
        robo.say("Considerando sua situação, quanto tempo você acha que consegueria esperar os frutos do plantio?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))
        

        
def main():
    bem_vindo()
    cadastro_nome()
    cadastro_email()
    cadastro_senha()    
    login()
    area_plantio()
    regiao()
    investir()
    tempo()
    
    
main()

