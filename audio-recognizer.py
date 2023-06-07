import speech_recognition as sr
import pyttsx3 
import os
from time import sleep

robo = pyttsx3.init()
recon = sr.Recognizer()



#Introdução ao aplicativo
def bem_vindo():
    
    with sr.Microphone() as source:
        robo.say("Bem-vindo a Alimentéqui. Queremos te ajudar a sair da situação em que você se encontra.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()

 #Função que apenas interpreta a voz do usuário para preencher o nome              
def cadastro_nome():
    
    with sr.Microphone() as source:
       
        robo.say("Diga seu nome.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()  
        audio = recon.listen(source)
        print("==================================")
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))  
        print("==================================")

#Função que apenas interpreta a voz do usuário para preencher o e-mail        
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
        print("==================================")
      

#Função que apenas interpreta a voz do usuário para preencher a senha       
def cadastro_senha():
    with sr.Microphone() as source:
      
        robo.say("Diga sua senha.")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()    
        audio = recon.listen(source)
        print("==================================")
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))     
        print("==================================")
       
#Função que apenas interpreta a voz do usuário para preencher o login        
def entrar():
    
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
        print("==================================")
        

#Tamanho da área que o usuário tem disponível para plantio        
def area_plantio():
    
    with sr.Microphone() as source:
        
        robo.say("Ok. Nos conte qual o tamanho da área do seu plantio?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("==================================")
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))
        print("==================================")
        
#Região onde o usuário reside     
def regiao():
    
    with sr.Microphone() as source:
        
        robo.say("Nos diga em que região do Brasil você mora?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("==================================")
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))
        print("==================================")



#Dinheiro disponível para comprar o necessário do plantio      
def investir():
    
    with sr.Microphone() as source:
        
        robo.say("Ok. Quantos reais você teria disponível para investir no plantio?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("==================================")
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))
        print("==================================")


#Referente ao tempo que o usuário teria disponível para esperar os frutos
def tempo():
    
    with sr.Microphone() as source:
        
        robo.say("Considerando sua situação, quanto tempo você acha que consegueria esperar os frutos do plantio?")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait()
        audio = recon.listen(source)
        print("==================================")
        print("Ouvindo...")
        sleep(1)
        print(recon.recognize_google(audio, language='pt'))
        print("==================================")
        robo.say("Ok. Aguarde ")
        robo.setProperty('voice', b'brasil')
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 0.7)
        robo.runAndWait() 

#Aqui seria a resposta da API do GPT.       
#def resposta():
   #robo.say("")
   #robo.setProperty('voice', b'brasil')
   #robo.setProperty('rate', 140)
   #robo.setProperty('volume', 0.7)
   #robo.runAndWait()
    


def formulario():
    area_plantio()
    regiao()
    investir()
    tempo()

def login():
    cadastro_nome()
    cadastro_email()
    cadastro_senha()    
    entrar()
    
    
def main():
    bem_vindo()
    login()
    formulario()
    
    
    
main()

