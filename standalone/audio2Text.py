import speech_recognition as sr
import pyautogui as aut
import os

def exibirMicrofones():
    mics = sr.Microphone.list_microphone_names()
    for i in range(len(mics)):
        print(f'Microfone {i}: {mics[i]}')
    
def reconhecer_fala():    
    microfone = sr.Recognizer() #Habilita o microfone
    with sr.Microphone() as source:        
        #microfone.adjust_for_ambient_noise(source)#Reducao de ruido disponivel na speech_recognition        
        print("Diga alguma coisa: ")        
        audio = microfone.listen(source) #guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes
        try:
            frase = microfone.recognize_google(audio,language='pt-BR') #audio sera interpretado na lingua portuguesa            
            if 'cacatua' in frase:
                print('Palavra chave para reiniciar o reconhecimento de fala foi encontrado. Ativando novamente o reconhecimento de fala.')
                reconhecer_fala()

            else:
                print("Você disse: " + frase)
                # verificaFrase(frase.lower())
                aut.write(frase)
                aut.press('enter')
                
        except Exception as e:
            print(f'Houve o seguinte problema: {e}')
        return frase

def reconhecer_audio(arquivo):
    r = sr.Recognizer()
    print('Adquirindo o arquivo de áudio...')
    arquivo = sr.AudioFile(arquivo)
    with arquivo as source:
        audio = r.record(source)
    print('Tentando realizar a conversão do áudio para o texto:')
    try:
        frase = r.recognize_google(audio, language='pt-BR')
        print(frase)
    except:
        print("Não entendi o que você disse!")

def verificaFrase(frase):
    if ('abrir' or 'abra' or 'abre') and 'steam' in frase:
        print('\nTentando abrir a steam\n')
        os.startfile('F:/Steam/steam.exe')
    if 'modlog' in frase:
        #os.startfile('C:/Users/Cacatua/AppData/Local/Discord/app-1.0.9002/Discord.exe')
        if 'conspiração' in frase:
            aut.write('&ml ')
            aut.hotkey('ctrl', 'v')
            aut.write(' g conspiracao c')
            

def main():
    #reconhecer_audio(r'C:/Users/Cacatua/Desktop/teste.wav')
    reconhecer_fala()

if __name__ == '__main__':
    main()