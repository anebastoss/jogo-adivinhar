from tkinter import *
from tkinter import ttk
import random
import pygame

#cores
preto = '#444466'
branco = '#ffffff'
azul = '#00008b'
verm = '#ff4500'
roxo = '#8a2be2'
#8a2be2
verde = '#28a745'
f = '#141414'

#musica
pygame.init()
pygame.mixer.music.load('chacapella.mp3')

#janela
janela=Tk()
janela.geometry('480x360')
janela.title('Adivinhe o numero')
janela.configure(bg=f)

#frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280,)
frame_top=Frame(janela, width=480, height=40, bg=f, pady=0, padx=0, relief='flat',)
frame_top.grid(row=1, column=0, sticky=NW)
frame_corpo=Frame(janela, width=360, height=480, bg=f, pady=0, padx=0, relief='flat')
frame_corpo.grid(row=2, column=0, sticky=N)
style=ttk.Style(janela)
style.theme_use("clam")

tentativas=5
pontuaçao=0

#programa principal
def iniciar():
    pygame.mixer.music.play(-1)
    regra1['text']=''
    regra2['text']=''
    regra3['text']=''
    num=random.sample(range(1,9),8)

    #define o valor certo
    def valor(v):
        num=random.sample(range(1,9),8)
        resp=[random.choice(num)]

        global tentativas
        global pontuaçao

        for i in resp:
            #verifica se o valor escolhido é o certo
            if v==i:
                tentativas+=2
                pontuaçao+=10
                i_tentativas['text']='Tentativas: '+str(tentativas)
                i_pontos['text']='Pontuação: '+str(pontuaçao)

            else:
                tentativas-=1
                i_tentativas['text']='Tentativas: '+str(tentativas)

                #verifica se as tentativas acabaram
                if tentativas<=0:
                    b1['state']='disable'
                    b2['state']='disable'
                    b3['state']='disable'
                    b4['state']='disable'
                    b5['state']='disable'
                    b6['state']='disable'
                    b7['state']='disable'
                    b8['state']='disable'

                    b1['text']=''
                    b2['text']=''
                    b3['text']=''
                    b4['text']=''
                    b5['text']=''
                    b6['text']=''
                    b7['text']=''
                    b8['text']=''

                    b1['bg']=f
                    b2['bg']=f
                    b3['bg']=f
                    b4['bg']=f
                    b5['bg']=f
                    b6['bg']=f
                    b7['bg']=f
                    b8['bg']=f

                    gameover()

                else:
                    pass

    b1=Button(frame_corpo, command=lambda:valor(num[0]), text=num[0], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b1.place(x=0, y=90)
    b2=Button(frame_corpo, command=lambda:valor(num[1]), text=num[1], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b2.place(x=85, y=90)
    b3=Button(frame_corpo, command=lambda:valor(num[2]), text=num[2], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b3.place(x=170, y=90)
    b4=Button(frame_corpo, command=lambda:valor(num[3]), text=num[3], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b4.place(x=255, y=90)
    b5=Button(frame_corpo, command=lambda:valor(num[4]), text=num[4], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b5.place(x=0, y=179)
    b6=Button(frame_corpo, command=lambda:valor(num[5]), text=num[5], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b6.place(x=85, y=179)
    b7=Button(frame_corpo, command=lambda:valor(num[6]), text=num[6], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b7.place(x=170, y=179)
    b8=Button(frame_corpo, command=lambda:valor(num[7]), text=num[7], width=6, height=3, font=('Ivy 16 bold'), bg=f, fg=branco, relief=RAISED, overrelief=RIDGE)
    b8.place(x=255, y=179)
    botao['text']=''
    botao['width']=0

#função gameover
def gameover():
    global tentativas
    global pontuaçao

    pygame.mixer.music.pause()

    go=Label(frame_corpo, text='GAME OVER', relief='raised', anchor='center', font=("Ivy 23 bold"), bg=branco, fg=verm)
    go.place(x=77, y=110)

    t_pontos=Label(frame_corpo, text='Você fez: '+str(pontuaçao)+' pontos', relief='raised', anchor='center', font=("Ivy 16 bold"), bg=branco, fg=azul)
    t_pontos.place(x=76, y=170)

    botao3=Button(frame_corpo, command=iniciar, width=33, text='Jogar novamente', relief=RAISED, anchor='center', font=("Ivy 13 bold"), bg=verde, fg=branco, overrelief=RIDGE)
    botao3.place(x=2, y=230)

    tentativas=5
    pontuaçao=0

    i_tentativas['text']='Tentativas: '+str(tentativas)
    i_pontos['text']='Pontuação: '+str(pontuaçao)

#Frame top
nome=Label(frame_top, text='Adivinhe o número', anchor='center', font=("Ivy 22 bold"), bg=f, fg=roxo)
nome.place(x=122, y=0)

#Frame corpo
i_pontos=Label(frame_corpo, text='Pontuação: 0', anchor='center', font=("Ivy 12 bold"), bg=f, fg=branco)
i_pontos.place(x=0, y=30)

i_tentativas=Label(frame_corpo, text='Tentativas: 5', anchor='center', font=("Ivy 12 bold"), bg=f, fg=branco)
i_tentativas.place(x=239, y=30)

linha=Label(frame_corpo, text='', width=112, anchor='center', font=("Ivy 4"), bg=azul, fg=branco)
linha.place(x=0, y=67)

regra1=Label(frame_corpo, text='Adivinhe o número para pontuar', anchor='center', font=("Ivy 9 bold"), bg=f, fg=branco)
regra1.place(x=0, y=110)

regra2=Label(frame_corpo, text='Se acertar, ganha mais 2 pontos', anchor='center', font=("Ivy 9 bold"), bg=f, fg=branco)
regra2.place(x=0, y=150)

regra3=Label(frame_corpo, text='Se errar, perde uma chance', anchor='center', font=("Ivy 9 bold"), bg=f, fg=branco)
regra3.place(x=0, y=190)

botao=Button(frame_corpo, command=iniciar, text='Jogar', width=37, relief=RAISED, anchor='center', font=("Ivy 11 bold"), bg=verde, fg=branco, overrelief=RIDGE)
botao.place(x=0, y=237)

pygame.event.wait()
janela.mainloop()



    



                    
