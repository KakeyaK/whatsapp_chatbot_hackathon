from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

#possiveis escritas erradas

info = ['*1.* Coronavírus é uma família de vírus que causam infecções respiratórias. O novo agente do coronavírus foi descoberto em 31/12/19 após casos registrados na China. Provoca a doença chamada de COVID-19.', '*2.* Os sintomas da COVID-19 são semelhantes aos de uma gripe. Entre eles estão a febre, a tosse, dificuldades respiratórias e, em alguns casos, cansaço, dores no corpo, dor de garganta e corrimento nasal. Os sintomas se agravam de forma gradual, e muitas vezes são leves. Em certos casos, principalmente quando o infectado pertence a um grupo de risco, pode ser mais grave, levando inclusive à morte.', '*3.* Realize nosso teste (baseado em testes oficiais do Ministério da Saúde) para saber sua situação e o que deve ser feito. Para contato direto com autoridades da saúde, disque 136 para receber informações do Ministério da Saúde. Em caso de suspeita, FIQUE EM CASA. O isolamento social protege você e as outras pessoas.', '*4.* Período de incubação é o tempo que leva para os primeiros sintomasaparecerem desde a infecção por coronavírus, que pode ser de 2 a 14 dias.' ,'*5.* Através do contato com pessoas infectadas, podendo ser transmitido via apertos de mão, gotículas de saliva expelidas com a fala, espirros, tosse, catarro e objetos e superfícies contaminados. Não há dados que comprovem a transmissão via animais de estimação e importação de produtos vindos da China ou de qualquer outro país contaminado.', '*6.* As diferenças entre o novo coronavírus e outras síndromes gripais são bem sutis. A principal delas é que a COVID-19 causa falta de ar e demais problemas respiratórios com maior frequência que um resfriado ou uma gripe. Para maisinformações, acesse o site https://coronavirus.saude.gov.br/sobre-a-doenca, do Ministério da Saúde, e veja a sessão “Comparativo de doenças”.', '*7.* No momento, ainda não há remédio ou vacina para a COVID-19. Para se prevenir, são recomendados o isolamento social e as medidas básicas de higienização. Aos infectados, é recomendado fazer tratamento dos sintomas e permanecer em repouso e isolamento social, em casos leves. Pacientes com sintomas mais intensos devem ser hospitalizados.', '*8.* As pessoas mais vulneráveis à COVID-19 pertencem ao chamado grupo de risco. Entre elas estão idosos (mais de 60 anos), pessoas com imunidade baixa (quem está se recuperando de uma cirurgia ou alguém com aids, por exemplo), diabéticos, pessoas com problemas respiratórios, hipertensos e pessoas com problemas crônicos renais.', '*9.* Não através do contato físico. Existe, sim, a possibilidade da contaminação através da carne, mas basta cozinhar bem a carne para se prevenir. Não é preciso se preocupar com animais de estimação', '*10.* No momento, a medida mais importante de prevenção ao coronavírus é o isolamento social. Ficar em casa ajuda muito a diminuir a propagação. Dentro de casa, as medidas de prevenção são simples: não compartilhar objetos pessoais, lavar frequentemente as mãos com sabão, higienizar objetos pessoais, cobrir o rosto como braço ou com um lenço ao espirrar ou tossir. O melhor jeito e lavar a mão é conforme a imagem a seguir:\n Caso seja extremamente necessário sair de casa, mantenha uma distância mínima de 1,5m em relação a qualquer pessoa e evite aglomerações. Ao chegar em casa, higienize as mãos e troque de roupa. Até o momento, o uso de máscaras é recomendado apenas para quem pertence ao grupo de risco (idosos, diabéticos, hipertensos, pessoas que sofrem de alguma doença crônica ou que prejudique o sistema imunológico). Máscaras caseiras podem ser feitas e utilizadas, embora na maioria dos casos seu uso não previna o contágio, apenasa transmissão.']

apresentar =[]

oi = []

menorque5 = ["0","1","2","3","4","5",]


informacoes = ["informações",
               "INFORMAÇÕES",
               "INFORMACÕES",
               "Informaçoes",
               "Informações",
               "informaçoes",
               "informacoes",
               "Informacoes",
               "Informacões",
               "informacões"]

teste = ["teste",
         "Teste",
         "TESTE",
         "tete",
         "TEST"]


casos = ["Caos",
         "casos",
         "CASOS",
         "Casos",
         "Casps"]

confirmar = ["Confirmar",
             "Confirmar",
             "CONFIRMAR",
             "confirm"]
sim = ["sim",
       "ss",
       "s",
       "SIM",
       "Sim",
       "Siim"]

nao = ["não",
       "nao",
       "n",
       "NAO",
       "NÃo",
       "NÃO",
       "Nao"]

#texto acompanha o andamento da conversa
#legenda dos números de texto

#0 = Nenhuma interação relevante feita com o bot
#1 = bot já se apresentou e mostrou seus comandos,, quando pedido o teste, já gera a primeira pergunta
#2 = dentro do teste, segunda pergunta, sobre sintomas leves
#3 = terceira pergunta, sobre idade
#4 = quarta pergunta, sobre sintomas pesados
#5 = quinta pergunta, sobre doenças de risco, primeira da série
#6 = sexta pergunta, sobre doencas de risco, segunda da série
#7 = sétima doença, sobre doencas de risco, terceira da série
#8 = Termina
    
presentar = 'Digite "informações" para saber informações conhecidas até agora sobre o COVID-19.\n Digite "teste" para fazer um teste semelhante ao aplicado no site do ministério da saúde para avaliar a possibilidade de você estar infectado.\n Digite "Casos" e o seu município para saber o número de casos em seu município.\n Por último, se você deseja confirmar alguma afirmação que te fizeram sobre o COVID-19, digite "Confirmar" e envie, então mande outra mensagem com a afirmação que você deseja confirmar, como "o COVID-19 se espalha pelo ar" e te direi se posso confirmar essa afirmação ou ela não é conhecida e verificada por mim'

texto = 0

#utilizar para teste
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])

#Funções para facilitar o teste

def sms_reply():

    global texto
    global sim
    global nao


    
    
    # msg recebe a mensagem
    msg = request.values.get('Body', '').lower()

    # resp responde a mensagem
    resp = MessagingResponse()

    if msg in informacoes:
        resp.message("Tenho informações para responder às seguintes perguntas, digite o número da pergunta para eu te dar a resposta:\n\n*1.* O que é o corona vírus?/O que é a covid-19? /O que é o novo corona vírus?\n\n*2.* Quais são os sintomas?/ Quais são os sintomas do coronavírus?/ Sintomas?/ Corona vírus mata\n\n*3.* Acho que tenho COVID-19, o que faço?/ O que fazer em caso de suspeita de contaminação?\n\n*4.* Qual é o tempo de incubação do vírus?/ Quanto tempo demora para que os sintomas de manifestem?\n\n*5.* Como o COVID-19 é transmitido?\n\n*6.* Qual é a diferença entre a gripe e a COVID-19?\n\n*7.* Existe vacina para a COVID-19?\n\n*8.* Qual é o grupo de risco?/ Sou do grupo de risco? Idosos/crianças/diabéticos são mais vulneráveis?\n\n*9.* Animais podem transmitir coronavírus?\n\n*10.* Como posso me proteger?/ Quais são as medidas de proteção?/ Isolamento social é necessário?")
        texto = 1.1
    elif msg in str(list(range(1,11))) and texto == 1.1:
        resp.message(info[int(msg)-1])
        texto = 1
        
    #elif msg in faq:
     #   respon.message("Você selecionou a opção mais informações")
     #  texto = 1
     
    elif msg in apresentar:
        resp.message(presentar)

    elif msg in confirmar:
        resp.message("Você selecionou confirmar")
        texto = 1

    elif msg in casos:
        resp.message("Você selecionou casos")
        texto = 1
        
    #elif msg in oi and texto != 0:
    #   resp.message(random.choice(oi))

    #elif msg in palavrao:
   #     resp.message("poxa, desculpe se te incomodei, me envie a palavra sugestão e depois me mande sugestão para eu poder melhorar ;)")

    #elif msg in sugestão:
     #   resp.message("obrigado pela sugestão!!")

#apresentação inici
    elif texto == 0:
        resp.message(presentar)
        texto = 1



#====TESTE COMEÇA====


    elif msg in teste:
        resp.message("Você selecionou o teste")
        resp.message("Lembre: Está é uma ferramenta de auxílio que não substitui um diagnóstico médico profissional.")
        resp.message("Você apresentou mais de 37,8° de febre?")
        texto = 2

    #ponta fechada
    elif msg in nao and texto == 2:
        resp.message("Pelas informações que você nos passou, neste momento NÃO há uma situação de emergência/risco para o novo coronavírus (COVID-19)")
        texto = 1

    elif msg in sim and texto == 2:
        resp.message("Você apresenta tum ou mais desses sintomas: Tosse; dor de garganta; dificuldade para respirar?")
        texto = 3

    #ponta fechada
    elif msg in nao and texto == 3:
        resp.message("Pelas informações que você nos passou, neste momento NÃO há uma situação de emergência/risco para o novo coronavírus (COVID-19)")
        texto = 1

    elif msg in sim and texto == 3:
        resp.message("Qual sua idade?")
        texto = 4
        
    #ponta fechada
    elif msg in menorque5 and texto == 4:
        texto = 1
        resp.message("Para crianças com 5 anos ou menos, independente dos sintomas, recomendamos buscar uma Unidade Básica de Saúde (UBS) o mais rápido possível. Veja no link a seguir a unidade mais próxima de você:\n http://w.tnh.health/l/ubs")

    elif msg in str(list(range(5,201))) and texto == 4:
        texto = 5
        resp.message("Entre os seguintes sintomas: dificuldade para respirar ao realizar pequenos esforços; sensação de cansaço itenso; sensação de desmaio. Você sente algum deles?")
        
    #ponta fechada
    elif msg in sim and texto == 5:
        resp.message("Pelas informações que você nos deu, a melhor opção é buscar um atendimento em uma Emergência Hospitalar ou um Pronto Atendimento de Urgêcia! Faça isso o mais rápido possível.")
        texto = 1
        
    elif msg in nao and texto == 5:
        resp.message("Vou perguntar agora sobre algumas das suas condições de saúde. Se você se encaixar em uma ou mais das situações abaixo, responda SIM")
        resp.message("Doenças cardíacas: hipertensão arterial (pressão alta), coronariopatias (doença dos vasos do coração), valvulopatias (doença de válvulas do coração), IAM prévio (infarto anterior)?\n Doenças respiratórias: asma e outras pneumopatias (doenças no pulmão) ou está com tuberculose ativa?\n Doenças neurológicas: disfunção congênita, lesões musculares, epilepsia, paralisia cerebral, síndrome de Down, derrame (AVC/AVE) ou doenças neuromusculares?")
        texto = 6
        
    #ponta fecha
    elif msg in sim and texto == 6:
        resp.message('Pelas informações que você nos deu, recomendamos, o mais rápido ´posível, que busque uma Unidade Básica de Saúde (UBS) (veja no link a seguir a unidade mais próxima de você: http://w.tnh.health/l/ubs) ou ligar para 08005918800. A ligação é gratuita')
        texto = 1

    elif msg in nao and texto == 6:
        resp.message('E alguma destas? Câncer, diabetes, doenças nos rins, doença nos fígados, problemas de saúde que causam baixa imunidade (aids, transplantes e outros)')
        texto = 7

    #ponta fecha
    elif msg in sim and texto == 7:
        resp.message('Pelas informações que você nos deu, recomendamos, o mais rápido ´posível, que busque uma Unidade Básica de Saúde (UBS) (veja no link a seguir a unidade mais próxima de você: http://w.tnh.health/l/ubs) ou ligar para 08005918800. A ligação é gratuita')
        texto = 1

    elif msg in nao and texto == 7:
        resp.message("Você é gestante ou está na fase de puerpério até duas semanas após o parto ou teve aborto neste período? Tem obesidade grave (Índice de Massa Corporal - IMC maior que 40)?")
        texto = 8
        
    #ponta fecha
    elif msg in sim and texto == 8:
        resp.message('Pelas informações que você nos deu, recomendamos, o mais rápido ´posível, que busque uma Unidade Básica de Saúde (UBS) (veja no link a seguir a unidade mais próxima de você: http://w.tnh.health/l/ubs) ou ligar para 08005918800. A ligação é gratuita')
        texto = 1
        
    #ponta fecha
    elif msg in nao and texto == 8:
        resp.message("Pelas informações que você nos deu, os sintomas indicam que você pode estar com uma infecção respiratória, ou seja, sem sinais de gravidade para o novo coronavírus. O melhor a se fazer neste caso é praticar o isolamento domiciliar por 14 dias")
        texto = 1

#====FIM DO TESTE====


    elif texto >= 2:
        ("Desculpe, não consegui entender, responda de novo a pergunta por favor")
        
    else:
        resp.message("Desculpe, acho que não entendi o que você falou, infelizmente meu vocabulário ainda é raso ;-/")
        texto = 0
    
    
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
