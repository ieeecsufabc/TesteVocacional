from tkinter import *

root = Tk()
root.title("Teste Vocacional - IEEE Computer Society UFABC")

count1 = IntVar()
count2 = IntVar()
count3 = IntVar()
count4 = IntVar()
count5 = IntVar()
result = IntVar()

#Função para trocar entre os frames
def raise_frame(frame):
    frame.tkraise()

#Função para aumentar os contadores
def setCount(count):
	if count == 1:
		count1.set(count1.get() + 1)
	elif count == 2:
		count2.set(count2.get() + 1)
	elif count == 3:
		count3.set(count3.get() + 1)
	elif count == 4:
		count4.set(count4.get() + 1)
	elif count == 5:
		count5.set(count5.get() + 1)

#Função para calcular o resultado
def show_result():
	result.set(count1.get())
	if count1.get() < count2.get():
		result.set(count2.get())
	if result.get() < count3.get():
		result.set(count3.get())
	if result.get() < count4.get():
		result.set(count4.get())
	if result.get() < count5.get():
		result.set(count5.get())

	if result.get() == count1.get():
		resultText.config(text="Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia Ambiental e Urbana - BC&T"+'\n'+"Bacharelado em Ciências Biológicas - BC&T"+'\n'+"Bacharelado em Matemática - BC&T"+'\n'+"Licenciatura em Filosofia - BC&H"+'\n'+"Licenciatura em Ciências Biológicas - BC&T"+'\n'+"Licenciatura em Matemática - BC&T")
	elif result.get() == count2.get():
		resultText.config(text="Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia Aeroespacial - BC&T"+'\n'+"Engenharia Biomédica - BC&T"+'\n'+"Engenharia de Energia - BC&T"+'\n'+"Engenharia de Instrumentação, Automação e Robótica - BC&T"+'\n'+"Bacharelado em Neurociência - BC&T"+'\n'+"Bacharelado em Relações Internacionais - BC&H")
	elif result.get() == count3.get():
		resultText.config(text="Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia de Gestão - BC&T"+'\n'+"Engenharia de Informação - BC&T"+'\n'+"Engenharia de Instrumentação, Automação e Robótica - BC&T"+'\n'+"Bacharelado em Ciências da Computação - BC&T"+'\n'+"Bacharelado em Física - BC&T"+"Bacharelado em Quiímica - BC&T"+'\n'+"Licenciatura em Física - BC&T"+'\n'+"Licenciatura em Química - BC&T")
	elif result.get() == count4.get():
		resultText.config(text="Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia de Gestão - BC&T"+'\n'+"Engenharia da Informação - BC&T"+'\n'+"Engenharia de Instrumentação, Automação e Robótica - BC&T"+'\n'+"Bacharelado em Ciências Econômicas - BC&H")
	elif result.get() == count5.get():
		resultText.config(text="Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Bacharelado em Filosofia - BC&H"+'\n'+"Bacharelado em Planejamento Territorial - BC&H"+'\n'+"Bacharelado em Física - BC&T"+'\n'+"Bacharelado em Quimíca - BC&T")

#Função para resetar o teste.
def reset():
	for count in (count1, count2, count3, count4, count5):
		count.set(0)

#Declaração dos frames
startFrame = Frame(root)
q1 = Frame(root)
q2 = Frame(root)
q3 = Frame(root)
q4 = Frame(root)
q5 = Frame(root)
q6 = Frame(root)
q7 = Frame(root)
q8 = Frame(root)
q9 = Frame(root)
q10 = Frame(root)
q11 = Frame(root)
finalFrame = Frame(root)
for frame in (startFrame, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, finalFrame):
    frame.grid(row=0, column=0, sticky='news')

#Página inicial
Label(startFrame, text="Olá! Seja bem vindo ao teste Vocacional desenvolvido pelo IEEE Computer Society UFABC").pack()
Button(startFrame, text="Começar!", command=lambda:raise_frame(q1)).pack()

#Estrutura da questão
#Label(frame da questão, text="Número da questão").pack()
#Button(frame da questão, text="Resposta 1", command=lambda:[raise_frame(frame da próxima questão), setCount(1)]).pack()
#Button(frame da questão, text="Resposta 2", command=lambda:[raise_frame(frame da próxima questão), setCount(2)]).pack()
#Button(frame da questão, text="Resposta 3", command=lambda:[raise_frame(frame da próxima questão), setCount(3)]).pack()
#Button(frame da questão, text="Resposta 4", command=lambda:[raise_frame(frame da próxima questão), setCount(4)]).pack()
#Button(frame da questão, text="Resposta 5", command=lambda:[raise_frame(frame da próxima questão), setCount(5)]).pack()

#Questão 1
Label(q1, text='Questão 1 - Você se considera uma pessoa:').pack()
Button(q1, text='Exigente, gosta das coisas organizadas', command=lambda:[raise_frame(q2), setCount(1)]).pack()
Button(q1, text='Ambiciosa, que corre atrás dos próprios sonhos', command=lambda:[raise_frame(q2), setCount(2)]).pack()
Button(q1, text='Conservadora, que analisa os riscos antes de agir', command=lambda:[raise_frame(q2), setCount(3)]).pack()
Button(q1, text='Controladora, busca ter um alto padrão de vida', command=lambda:[raise_frame(q2), setCount(4)]).pack()
Button(q1, text='Solidário, que busca ajudar o próximo', command=lambda:[raise_frame(q2), setCount(5)]).pack()

#Questão 2
Label(q2, text='Questão 2 - Em qual dos seguintes ambientes você se sente mais confortável:').pack()
Button(q2, text='Hospital', command=lambda:[raise_frame(q3), setCount(1)]).pack()
Button(q2, text='Clubes esportivos', command=lambda:[raise_frame(q3), setCount(2)]).pack()
Button(q2, text='Parques ecológicos', command=lambda:[raise_frame(q3), setCount(3)]).pack()
Button(q2, text='Shopping Center', command=lambda:[raise_frame(q3), setCount(4)]).pack()
Button(q2, text='Lugares tranquilos e isolados', command=lambda:[raise_frame(q3), setCount(5)]).pack()

#Questão 3
Label(q3, text='Questão 3 - Qual das seguintes personalidades você mais admira:').pack()
Button(q3, text='Albert Einsten', command=lambda:[raise_frame(q4), setCount(1)]).pack()
Button(q3, text='Silvio Santos', command=lambda:[raise_frame(q4), setCount(2)]).pack()
Button(q3, text='Neymar', command=lambda:[raise_frame(q4), setCount(3)]).pack()
Button(q3, text='Gisele Bündchen', command=lambda:[raise_frame(q4), setCount(4)]).pack()
Button(q3, text='Mahatma Gandhe', command=lambda:[raise_frame(q4), setCount(5)]).pack()

#Questão 4
Label(q4, text='Questão 4 - Com qual modalidade esportiva você mais se indentifica:').pack()
Button(q4, text='Futebol', command=lambda:[raise_frame(q5), setCount(1)]).pack()
Button(q4, text='Judô', command=lambda:[raise_frame(q5), setCount(2)]).pack()
Button(q4, text='Vela', command=lambda:[raise_frame(q5), setCount(3)]).pack()
Button(q4, text='Tênis', command=lambda:[raise_frame(q5), setCount(4)]).pack()
Button(q4, text='Não me indentifico com esportes', command=lambda:[raise_frame(q5), setCount(5)]).pack()

#Questão 5
Label(q5, text='Questão 5 - Costuma fazer amizades com pessoas:').pack()
Button(q5, text='Importantes e influentes', command=lambda:[raise_frame(q6), setCount(1)]).pack()
Button(q5, text='Que compactuam com os mesmos objetivos e interesses que eu', command=lambda:[raise_frame(q6), setCount(2)]).pack()
Button(q5, text='Que pensam igual a mim', command=lambda:[raise_frame(q6), setCount(3)]).pack()
Button(q5, text='Que possam acrescentar novos conhecimentos', command=lambda:[raise_frame(q6), setCount(4)]).pack()
Button(q5, text='Quaisquer, não me apego muito as características', command=lambda:[raise_frame(q6), setCount(5)]).pack()

#Questão 6
Label(q6, text='Questão 6 - Para onde você mais gostaria de viajar:').pack()
Button(q6, text='Para a Grécia, querendo conhecer esculturas e contruções antigas', command=lambda:[raise_frame(q7), setCount(1)]).pack()
Button(q6, text='Para a Austrália, visando aventuras radicais', command=lambda:[raise_frame(q7), setCount(2)]).pack()
Button(q6, text='Para os Estados Unidos, para aproveitar o conforto e fazer compras', command=lambda:[raise_frame(q7), setCount(3)]).pack()
Button(q6, text='Para o Japão, conhecer novas culturas', command=lambda:[raise_frame(q7), setCount(4)]).pack()
Button(q6, text='Para o Caribe, aproveitar com a família', command=lambda:[raise_frame(q7), setCount(5)]).pack()

#Questão 7
Label(q7, text='Questão 7 - Quando você vai a um lugar em que você não conhece as pessoas:').pack()
Button(q7, text='Fica em um canto sozinho', command=lambda:[raise_frame(q8), setCount(1)]).pack()
Button(q7, text='Conversa com alguém que possa lhe apresentar os demais', command=lambda:[raise_frame(q8), setCount(2)]).pack()
Button(q7, text='Se diverte e fica bem sozinho', command=lambda:[raise_frame(q8), setCount(3)]).pack()
Button(q7, text='Tenta socializar e fazer amigos', command=lambda:[raise_frame(q8), setCount(4)]).pack()
Button(q7, text='Sente-se incomodado e vai embora', command=lambda:[raise_frame(q8), setCount(5)]).pack()

#Questão 8
Label(q8, text='Questão 8 - A pessoa em que você se espelha:').pack()
Button(q8, text='Situa-se numa posição de destaque no mercado, devido a muito estudo', command=lambda:[raise_frame(q9), setCount(1)]).pack()
Button(q8, text='Viaja bastante e gosta de se aventurar', command=lambda:[raise_frame(q9), setCount(2)]).pack()
Button(q8, text='Aproveita a vida e descobre novas experiências', command=lambda:[raise_frame(q9), setCount(3)]).pack()
Button(q8, text='É bem criativa e apresenta sempre novidades', command=lambda:[raise_frame(q9), setCount(4)]).pack()
Button(q8, text='Dedica-se a trabalhos solidários', command=lambda:[raise_frame(q9), setCount(5)]).pack()

#Questão 9
Label(q9, text='Questão 9 - O mais importante para você numa profissão é:').pack()
Button(q9, text='Ser bem sucedido e conseguir um bom retorno financeiro', command=lambda:[raise_frame(q10), setCount(1)]).pack()
Button(q9, text='O destaque no mercado de trabalho', command=lambda:[raise_frame(q10), setCount(2)]).pack()
Button(q9, text='Realizar algo que goste, independente do retorno financeiro', command=lambda:[raise_frame(q10), setCount(3)]).pack()
Button(q9, text='Ter um grande retorno financeiro', command=lambda:[raise_frame(q10), setCount(4)]).pack()
Button(q9, text='Poder ajudar as pessoas em sua volta', command=lambda:[raise_frame(q10), setCount(5)]).pack()

#Questão 10
Label(q10, text='Questão 10 - Para você, qual seria a pior coisa:').pack()
Button(q10, text='Não ser reconhecido pelos meus feito e empenho', command=lambda:[raise_frame(q11), setCount(1)]).pack()
Button(q10, text='Ficar distante da família e amigos', command=lambda:[raise_frame(q11), setCount(2)]).pack()
Button(q10, text='Realizar ativiades contra os seus princípios', command=lambda:[raise_frame(q11), setCount(3)]).pack()
Button(q10, text='Deixar de fazer alguma atividade por falta de dinheiro', command=lambda:[raise_frame(q11), setCount(4)]).pack()
Button(q10, text='Ser obrigado a fazer o que não gosta', command=lambda:[raise_frame(q11), setCount(5)]).pack()

#Questão 11
Label(q11, text='Questão 11 - Gosta que lembrem de você por:').pack()
Button(q11, text='Suas conquistas', command=lambda:[show_result(), raise_frame(finalFrame), setCount(1)]).pack()
Button(q11, text='Seu jeito de ser', command=lambda:[show_result(), raise_frame(finalFrame), setCount(2)]).pack()
Button(q11, text='Suas raízes familiares', command=lambda:[show_result(), raise_frame(finalFrame), setCount(3)]).pack()
Button(q11, text='Sua popularidade', command=lambda:[show_result(), raise_frame(finalFrame), setCount(4)]).pack()
Button(q11, text='Sempre fornecer ajuda aos outros', command=lambda:[show_result(), raise_frame(finalFrame), setCount(5)]).pack()


#Página final
resultText = Label(finalFrame, text="")
resultText.pack()
Button(finalFrame, text="Recomeçar", command=lambda:[reset(), raise_frame(startFrame)]).pack()

raise_frame(startFrame)
root.mainloop()
