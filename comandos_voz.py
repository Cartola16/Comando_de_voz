import os
import speech_recognition as sr
import sys 
import pyttsx3 as voz
import re




def fala_cartola(mensagem):
    cartola_voz=voz.init()
    cartola_voz.say(mensagem)
    cartola_voz.runAndWait()

def ouvindo():

    rec=sr.Recognizer()# método junto com o Microphone para o input da voz

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)#retira todo o barulho do ambiente

        while True:

            try:
                entrada_audio=rec.listen(s)#aqui é onde reconhece a voz, o input de audio
                comando_voz=rec.recognize_google(entrada_audio,language="pt")#aqui é onde reconhecemos o idioma
                
                return comando_voz
            
            except sr.UnknownValueError:#caso aconteça algum erro
                fala_cartola("Não entendi, repita por favor")

def verifica_comando(comando_mensagem):

    comandos=re.split(" ",comando_mensagem)
    
    comando=""
    for i in comandos:
        print(i)


    for comando_cortado in comandos:

        if comando_cortado=="desligar" or comando_cortado=="Desligar" or comando_cortado=="DESLIGAR" or comando_cortado=="desliga" or comando_cortado=="Desliga" or comando_cortado=="DESLIGA" or comando_cortado=="desligue" or comando_cortado=="Desligue":
            comando="desligar"
        
        elif comando_cortado=="reiniciar" or comando_cortado=="REINICIAR" or comando_cortado=="REINICIA" or comando_cortado=="reinicia" or comando_cortado=="Reinicia" or comando_cortado=="Reiniciar":
            comando="reiniciar"
        
        elif comando_cortado=="descansar" or comando_cortado=="descansa" or comando_cortado=="DESCANSAR" or comando_cortado=="DESCANSA" or comando_cortado=="Descansa" or comando_cortado=="Descansar":
            comando="suspender"
            
        
        elif comando_cortado=="suspender" or comando_cortado=="suspenda" or comando_cortado=="suspende" or comando_cortado=="Suspender" or comando_cortado=="Suspende" or comando_cortado=="Suspenda":
            comando="suspender"
        
        elif comando_cortado=="fechar":
            for i in comandos:
                if i=="Cartola" or i=="cartola":
                    comando="fechar cartola"
            
       
            
        
    return comando

def executa_comando(comando):


        if comando=="desligar":
            fala_cartola("Desligando")
            os.system("shutdown /s")

        elif comando=="reiniciar":
            fala_cartola("Reiniciando")
            os.system("shutdown /r /t 1")

        elif comando=="suspender":
            fala_cartola("Suspendendo")
            os.system("shutdown /h")

        elif comando=="fechar cartola":
            fala_cartola("Bye Bye")
            sys.exit()

        
fala_cartola("Estou te ouvindo")

while True:
    comando=ouvindo()
    print(comando)
    comando=verifica_comando(comando)
    print(comando)
    executa_comando(comando)





