#Biblioteca utilizada para realizar o download do vídeo no Youtube
from pytube import YouTube

#Biblioteca utilizada para separar o áudios dos vídeos baixados
from moviepy.editor import *

#Bibliotecas utilizadas para reconhecer os diretórios 
#E também mover/remover os arquivos baixados
from os import remove, getcwd
import shutil


lista_Links = list() #Lista que receberá os links para um laço na função 2:
lista_Links.append("https://youtu.be/S9uPNppGsGo")
lista_Links.append("https://youtu.be/Mp0vhMDI7fA")
lista_Links.append("https://youtu.be/VuKvR1J2LQE")
lista_Links.append("https://youtu.be/31llNGKWDdo")
#Podendo acrescentar outros links:
#lista_Links.append()

def baixarVideo(link): #Esta função recebe um link somente de parâmetro, portanto download individual
    yt = YouTube(link).streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()
    print("Download realizado com sucesso.")

    #Neste momento iniciamos a separação do áudio do arquivo .mp4:
    mp4_file = yt.title()
    mp3_file = yt.title()+".mp3"
    VideoClip = VideoFileClip(mp4_file)
    AudioClip = VideoClip.audio
    AudioClip.write_audiofile(mp3_file)
    AudioClip.close()
    VideoClip.close() 
    
    #Como o .mp4 não será mais necessário, realizamos a exclusão:
    os.remove(yt.title())

    #E por fim, movo o arquivo .mp3 criado para uma pasta específica.
    pasta_rename = os.getcwd()+"\mp3"
    shutil.move(mp3_file, pasta_rename)


def baixarVideos(lista_Links): #Mesma função da anterior, porém recebendo uma lista, possibilitando vários downloads
    for item in lista_Links:
        yt = YouTube(item).streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()
        print("Download realizado com sucesso.")
        mp4_file = yt.title()
        mp3_file = yt.title()+".mp3"
        VideoClip = VideoFileClip(mp4_file)
        AudioClip = VideoClip.audio
        AudioClip.write_audiofile(mp3_file)
        AudioClip.close()
        VideoClip.close() 
        os.remove(yt.title())
        pasta_rename = os.getcwd()+"\mp3"
        shutil.move(mp3_file, pasta_rename)

#baixarVideo(https://youtu.be/S9uPNppGsGo)
#baixarVideos(lista_Links)