
cont1 = 0  
cont2 = 0   
cont3 = 0   
cont4 = 0   
cont5 = 0
print("Olá, seja bem-vindo ao teste vocacional desenvolvido pelo IEEE Computer Society UFABC")
print('\n'+"Siga as instruções para realizar o teste:")
print('\n'+"Existe 11 perguntas objetivas, selecione a que você mais se indentifica e aperte ENTER")
print('\n'+"Q1) Você se considera uma pessoa:"+'\n'+"1) Exigente, gosta das coisas organizadas"+'\n'+"2) Ambiciosa,que corre atrás dos próprios sonhos"+'\n'+"3) Conservadora, que analisa os riscos antes de agir"+'\n'+"4) Controladora,busca ter um alto padrão de vida"+'\n'+"5) Solidária, que busca ajudar o próximo")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print("")
print('\n'+"Q2) Em qual dos seguintes ambientes você se sente confortável:"+'\n'+"1) Hospital"+'\n'+"2) Clubes esportivos"+'\n'+"3) Parques ecológico"+'\n'+"4) Shopping center"+'\n'+"5) Lugares tranquilos e isolados")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q3) Qual das seguintes personalidades você mais adimira:"+'\n'+"1) Albert Einstein"+'\n'+"2) Silvio Santos"+'\n'+"3) Neymar"+'\n'+"4) Gisele Bünche"+'\n'+"5) Mahatma Gandhi")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q4) Com qual modalidade esportiva você mais se identifica:"+'\n'+"1) Futebol"+'\n'+"2) Judô"+'\n'+"3) Vela"+'\n'+"4) Tênis"+'\n'+"5) Não se identifica com esportes")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+ "Q5) Costuma fazer amizades com pessoas:"+'\n'+"1) Importantes e influentes"+'\n'+"2) Que compactuam com os mesmos objetivos e interesses"+'\n'+"3) Que pensam igual a mim"+'\n'+"4) Que possam acrescentar novos conhecimentos"+'\n'+"5) Quaisquer, não se apega muito a características")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q6) Para onde você mais gostaria de viajar:"+'\n'+"1) Para Grécia, querendo conhecer esculturas e construções antigas"+'\n'+"2) Para a Austrália, visando aventuras radicais"+'\n'+"3) Para os Estados Unidos, para aproveitar do conforto e fazer compras"+'\n'+"4) Para o Japão, conhecer novos culturas"+'\n'+"5) Para o Caribe, aproveitar com a família")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q7) Quando você vai a um lugar em que você não conhece as pessoas:"+'\n'+"1) Fica em um canto sozinho"+'\n'+"2) Conversa com alguém que possa lhe apresentar aos demais"+'\n'+"3) Se diverte e fica bem sozinho"+'\n'+"4) Tenta socializar e fazer amigos"+'\n'+"5) Sente-se incomodado e vai embora")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q8) A pessoa em que você se espelha:"+'\n'+"1) Situa-se em uma posição de destaque no mercado devido a muito estudo"+'\n'+"2) Viaja bastante e gosta de se aventurar"+'\n'+"3) aproveita a vida e descobre novas experiências"+'\n'+"4) É bem criativa e apresenta sempre novidades"+'\n'+"5) Dedica-se a trabalhos solidários")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q9) Mais importante para você em uma profissão é:"+'\n'+"1) Ser bem sucedido e conseguir um bom retorno financeiro"+'\n'+"2) A evidência no mercado de trabalho"+'\n'+"3) Realizar algo que goste, independente do retorno financeiro"+'\n'+"4) Ter um grande retorno financeiro"+'\n'+"5) Poder ajudar as pessoas a sua volta")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q10) Para você, qual seria a pior coisa?"+'\n'+"1) Não ser reconhecido pelos meus feitos e empenho"+'\n'+"2) Ficar distante da família e amigos"+'\n'+"3) Realizar atividades contra o seus princípios"+'\n'+"4) Deixar de fazer alguma atividade por falta de dinheiro"+'\n'+"5) Ser obrigado a fazer o que não gosta")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print('\n'+"Q11) Gosta que lembrem de você por:"+'\n'+"1) Suas conquistas"+'\n'+"2) Seu jeito de ser"+'\n'+"3) Suas raízes familiares"+'\n'+"4) Sua popularidade"+'\n'+"5) Sempre fornecer ajuda aos outros")
n = int(input())
if (n<1 or n>5):
  print("não existe essa resposta, digite novamente")
  n = int(input()) 
elif n == 1:
  cont1 += 1
elif n == 2:
  cont2 += 1 
elif n == 3:
  cont3 += 1 
elif n == 4:
  cont4 += 1 
elif n == 5:
  cont5 += 1 
print("")
if(cont1<cont2):
  resultado == cont2
elif(cont1<cont3):
  resultado == cont3
elif(cont1<cont4):
  resultado == cont4
elif(cont1<cont5):
  resultado == cont5
else:
  resultado == cont1
if (resultado == cont1):
  print("Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia Ambiental e Urbana - BC&T"+'\n'+"Bacharelado em Ciências Biológicas - BC&T"+'\n'+"Bacharelado em Matemática - BC&T"+'\n'+"Licenciatura em Filosofia - BC&H"+'\n'+"Licenciatura em Ciências Biológicas - BC&T"+'\n'+"Licenciatura em Matemática - BC&T")
elif (resultado == cont2):
 print("Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia Aeroespacial - BC&T"+'\n'+"Engenharia Biomédica - BC&T"+'\n'+"Engenharia de Energia - BC&T"+'\n'+"Engenharia de Instrumentação, Automação e Robótica - BC&T"+'\n'+"Bacharelado em Neurociência - BC&T"+'\n'+"Bacharelado em Relações Internacionais - BC&H")
elif (resultado == cont3):
  print("Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia de Gestão - BC&T"+'\n'+"Engenharia de Informação - BC&T"+'\n'+"Engenharia de Instrumentação, Automação e Robótica - BC&T"+'\n'+"Bacharelado em Ciências da Computação - BC&T"+'\n'+"Bacharelado em Física - BC&T"+"Bacharelado em Quiímica - BC&T"+'\n'+"Licenciatura em Física - BC&T"+'\n'+"Licenciatura em Química - BC&T")
elif (resultado == cont4):
  print("Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Engenharia de Gestão - BC&T"+'\n'+"Engenharia da Informação - BC&T"+'\n'+"Engenharia de Instrumentação, Automação e Robótica - BC&T"+'\n'+"Bacharelado em Ciências Econômicas - BC&H")
elif (resultado == cont5):
  print("Os cursos da UFABC disponíveis, que mais se assemelham ao seu perfil são:"+'\n'+"Bacharelado em Filosofia - BC&H"+'\n'+"Bacharelado em Planejamento Territorial - BC&H"+'\n'+"Bacharelado em Física - BC&T"+'\n'+"Bacharelado em Quimíca - BC&T")
