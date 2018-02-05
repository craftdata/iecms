#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importação de módulos:
import nltk, re
from nltk.etree.ElementTree import ElementTree

#Padrões: expressões regulares a serem utilizadas pelo tagger
padroes1=[
    # Padrões negativos
        (r'.*(fuck|hell|shit|kinky).*','IW'), #Improper Words e composições
        (r'^ass$','IW'), #Improper Words sozinhas
        (r'.*(stupid|ridiculous|loser|unethical|fool).*','PA'), #Personal Attacks
        (r'^(my|mine|myself)$','NC'), #Narcisism
        (r'.*(this is the way it is|it is a fact that).*','SI'), #Speak Impersonal
        (r'<.{1,3}>.*</.{1,3}>', 'HF'), #HTML Formatting
        (r'a{3,}|b{3,}|c{3,}|d{3,}|e{3,}|f{3,}|g{3,}|h{3,}|i{3,}|j{3,}|k{3,}|l{3,}|m{3,}|n{3,}|o{3,}|p{3,}|q{3,}|r{3,}|s{3,}|t{3,}|u{3,}|v{3,}|w{3,}|x{3,}|y{3,}|z', 'RL'), #Repeated letters
        (r'\?{2,}', 'IP'), #Improper Punctuation
        (r'[\*]+.+[\*]+', 'ET'), (r'[\(\{]{2,}.+[\)\}]{2,}', 'ET'), #Enclosed terms
        (r'.*[$#@%!#]{2,}.*>', 'CS'), #Character sequences
        (r'.*[8|:\;][-]*[\(|\)]{2,}.*', 'EM'), #Emoticons
    # Padrões positivos
        (r'.*(please|thanks|thank you|i would be grateful).*', 'EP'), #Expressions of politeness and gratitude
    # Para aplicar em todos: (r'','')
]
# Definição do tagger
re_tagger1=nltk.RegexpTagger(padroes1)
# Definindo classes:
# Classe Palavras: gera os tokens a serem analisados para se detectar os padrões
class Frase():
        def __init__(self, frase, problemas):
                self.texto=frase

                self.problemas=[]
                # Adiciona tags relativas a sintaxe html
                for caso in re.findall(r'<h\d>.+</h\d>',self.texto):
                        self.problemas.append((caso[4:-5],'HE'))
                for caso in re.findall(r'<sub>.+</sub>',self.texto):
                        self.problemas.append((caso[5:-6],'SB'))
                for caso in re.findall(r'<sup>.+</sup>',self.texto):
                        self.problemas.append((caso[5:-6],'SP'))
                for caso in re.findall(r'<span>.+</span>',self.texto):
                        self.problemas.append((caso[6:-7],'SP'))
                for caso in re.findall(r'<small>.+</small>',self.texto):
                        self.problemas.append((caso[7:-8],'SM'))
                for caso in re.findall(r'<b>.+</b>',self.texto):
                        self.problemas.append((caso[3:-4],'BO'))
                for caso in re.findall(r'<i>.+</i>',self.texto):
                        self.problemas.append((caso[3:-4],'IT'))

                # Remove sintaxes html, wiki e outras desnecessárias
                self.texto=remove_html(self.texto)
                self.texto=remove_wiki(self.texto)
                self.texto=remove_obsoletos(self.texto)

                # Separação dos tokens
                self.palavras = [palavra for palavra in re.split(u'"|\?|\.*\s+"*',frase[:-1]) if palavra!='']
                self.palavraslower = [palavra.lower() for palavra in self.palavras]

                # Detecta sequências de palavras maiúsculas (Case Words)
                n=0
                while n<(len(self.palavras)-1):
                        if re.search(r'^[A-Z]{2,}$',self.palavras[n]):
                                self.casewords=self.palavras[n]
                                n=n+1
                                while n<(len(self.palavras)-1) and re.search(r'^[A-Z]{2,}$',self.palavras[n]):
                                        self.casewords=self.casewords+" "+self.palavras[n]
                                        n=n+1
                                self.problemas.append((self.casewords,'CW'))
                        n=n+1

                # Problemas com apenas 1 palavra
                for problema in re_tagger1.tag(self.palavraslower):
                        if problema[1]!=None:
                                self.problemas.append(problema)
                # Problemas com 2  ou mais palavras
                # Caso do you + 2 palavras
                for n in range(len(self.palavraslower)-1):
                        if re.search(r'[yY]ou.*$',self.palavras[n]):
                                if n==len(self.palavraslower)-1:
                                        self.problemas.append((self.palavras[n],'Y1'))
                                elif n==len(self.palavraslower)-2:
                                        self.problemas.append((self.palavras[n]+' '+self.palavras[n+1],'Y2'))
                                else:
                                        self.problemas.append((self.palavras[n]+' '+self.palavras[n+1]+' '+self.palavras[n+2],'YO'))
                # Caso do you com adjetivo agressivo
                for n in range(len(self.palavraslower)-2):
                        if re.search(r'^i$|^(you|he|she|it|we|they|my|your|his|her|its|our|their).*$',self.palavras[n]):
                                if re.search(r'.*(you|your|stupid|ridiculous|loser|unethical|fool).*',self.palavras[n+1]):
                                        self.problemas.append((self.palavras[n]+' '+self.palavras[n+1],'PA'))
                # Caso com verbo to be entre o you e o adjetivo
                for n in range(len(self.palavraslower)-3):
                        if re.search(r'^i$|^(you|he|she|it|we|they|my|your|his|her|its|our|their)$',self.palavraslower[n]):
                                if re.search(r'.*(is|are).*',self.palavras[n+1]):
                                        if re.search(r'.*(stupid|ridiculous|loser|unethical|fool).*',self.palavras[n+2]):
                                                self.problemas.append((self.palavras[n]+' '+self.palavras[n+1],'PA'))
                # Passagem de problemas para a classe comentários:
                problemas.append(self.problemas)

# Classe Data: armazena a data do comentário
# variáveis: hora, minuto, dia, mês e ano
class Data():
    # A linha abaixo já instancia a classe recebendo valores do usuário
    def __init__(self, datacompleta):
        self.completa=datacompleta
        self.tokens=re.split(r':|, | ',self.completa)
        self.hora=self.tokens[0]
        self.minuto=self.tokens[1]
        self.dia=self.tokens[2]
        self.mes=self.tokens[3]
        self.ano=self.tokens[4]
        self.tipo=self.tokens[5]

# Classe Commentário: comentário com posicionamento, texto recebido,
# número de caracteres que compõem o comentário
# variáveis: posicionamento, texto, numCaractere, frases[], usuario, data
#            respostas[], numFrase
class Comentario():
    def __init__(self, texto, datacompleta, num):
        self.numComentario=num
        self.posicionamento=' '
        if re.search("^:* *'''.*''' *", texto):
            # Remove caracteres irrelevantes: separa o texto em um vetor de strings (tokens) removendo o trecho "   --'''abcd'''   "
            self.tokens=re.split(r" *-*''' *",texto)
            if self.tokens[0]!='':
                self.nivel=len(re.findall(':',self.tokens[0]))
            else:
                    self.nivel=0
            self.posicionamento=self.tokens[1]
            self.texto=' '.join(self.tokens[2:])

        else:
            self.texto=texto
            self.nivel=len(re.findall('^:+\w',self.texto))-1

        self.frases=[]

        # Remove caracteres irrelevantes: ':' e '\n' ao início de um comentário
        if (self.texto[0]==':')|(self.texto[0]=='\n'):
                m=1
                while (self.texto[m]==':')|(self.texto[m]=='\n'):
                        m=m+1
                self.texto=self.texto[m:]

        # o u'' indica o tipo de caractere: unicode, r: raw (literal)
        if re.search('\[\[User:[\w.\xfc]+',self.texto):
            # Problema com unicode \xfc de Türinger, pesquisar modo de representar caracteres acentuados em unicode
            self.usuario=re.split('(\[\[User:[\w.\xfc]+)',self.texto)[1][7:]
            self.texto=re.split('(\[\[User:[\w.\xfc]+)',self.texto)[0]
        elif re.search('\(\[\[User talk:[\w.\xfc]+',self.texto):
            self.usuario=re.split('(\(\[\[User talk:[\w.\xfc]+)',self.texto)[1][13:]
            self.texto=re.split('(\(\[\[User talk:[\w.\xfc]+)',self.texto)[0]
        else: self.usuario=' '

        # Armazenamento da Data
        self.data=Data(datacompleta)
        # Contagem dos caracteres
        self.numCaracteres=len(self.texto)
        # Divisão do texto
        self.tokens=re.split(r"\. \s*",self.texto)

        # Declaração de variáveis
        self.problemas=[]
        self.problemas2=[]

        for i in range(len(self.tokens)):
            # se a string(elemento do vetor de tokens) não for vazia
            if self.tokens[i] != '':
                # adiciona um elemento no vetor de tokens
                self.frases.append(Frase(self.tokens[i]+'.',self.problemas))
        # Contagem do número de frases
        self.numFrase=len(self.frases)
        self.numPadroes=0
        # Contagem do número de padrões identificados
        for frase in self.frases:
                self.numPadroes=self.numPadroes+len(frase.problemas)

        # Remoção de sintaxes irrelevantes após processamento
        self.texto=remove_html(self.texto)
        self.texto=remove_wiki(self.texto)
        self.texto=remove_obsoletos(self.texto)

# Classe Discussion: discussão
# variáveis: assunto, texto, comentarios[]
class Discussao():
    def __init__(self, assunto, texto, num):
        self.numDiscussao=num
        self.assunto=link_assunto(assunto)
        self.texto=texto
     # Processamento do texto:
        self.tokens=re.split(r'\s*(\d\d:\d\d, \d{1,2} [a-zA-Z]{3,10} \d{4} \([A-Z]{3}\))\w*\s*',self.texto)
        self.comentarios=[]
        self.numComentarios=len(self.tokens)/2
        for n in range(self.numComentarios):
            if self.tokens[n]!='':
                if re.search('^<[\w =]*>\s*(<[\w =]*>\s*)*',self.tokens[n]):
                    string=re.split('^<[\w =]*>\s*(<[\w =]*>\s*)*',self.tokens[n])[2]
                self.comentarios.append(Comentario(self.tokens[2*n], self.tokens[2*n+1], n+1))

        self.pessoas=[]
        self.numPadroes=0
        for comentario in self.comentarios:
                self.pessoas.append(comentario.usuario)
                self.numPadroes=self.numPadroes+comentario.numPadroes
        set(self.pessoas)
        self.numPessoas=len(self.pessoas)

# Classe XML: armazena os dados do arquivo .xml
# variáveis: sitename, title, articleid, timestamp, username, userid, texto, discussoes[]
class Xml():
    def __init__(self,arq): #inicializa a instância com a função
      # monta uma árvore a partir dos campos do arquivo do XML:
        arq_xml = ElementTree().parse(arq)
        # coleta direta da árvore do ElementTree (função do módulo NLTK para processamento de XML)
        self.sitename=arq_xml[0][0].text
        self.title=arq_xml[1][0].text
        self.alticleid=arq_xml[1][1].text
        self.timestamp=arq_xml[1][2][1].text
        self.username=arq_xml[1][2][2][0].text
        self.userid=arq_xml[1][2][2][1].text
        self.texto=arq_xml[1][2][4].text
      # Processamento do texto:
        # Separa o texto em trechos com ' == '
        # Extração de tokens de dentro da variável da classe
        self.tokens=re.split(r'\s*==\s*',self.texto)
        self.discussoes=[]
        for n in range(len(self.tokens)/2):
                self.discussoes.append(Discussao(self.tokens[2*n+1],self.tokens[2*n+2],n+1))

# Funções para processamento de texto wiki:
# função recebe um texto, checa se é link na sintaxe de wiki e retorna apenas o que apareceno título sem o link
def link_assunto(texto):
    # verifica se se encaixa na sintaxe de link de wiki
    if re.search('^\[\[.{2,200}\|.{2,200}\]\]$', texto):
        # retorna o que aparece na tela como título,
        return re.findall(r'\|.{2,400}\]\]$', texto)[0][1:-2]
    elif re.search('^\[\[.{2,400}\]\]$', texto):
        return re.findall(r'^\[\[.{2,400}\]\]$', texto)[0][2:-2]
    else: return texto
# remove trechos de código html do tipo <...> e espaços em volta
def remove_html(string):
   return re.sub(r'\s*<(\w|\\|\/|!|-|=|"|;|:| )+>\s*',' ',string)
# remove trecho de código wiki do tipo [...] e espaços em volta
def remove_wiki(string):
    aux=re.sub(r'\s*\[\[\w+:[\w| |.|\|\\|\/|\#]+\]\]\s*',' ',string)
    return re.sub(r'\[\[|\]\] *','',aux)
    # extra: descobrir o que é [WP:EL]], [WP:SPAM]], [[WP:NOT#LINK]]
# remove caracteres obsoletos ao final do texto, ex : e -- ao final dos textos
def remove_obsoletos(string):
    return re.sub(r'[,|\s|\-]*$',' ',string)

#PROBLEMA: para o arquivo 'Wikipedia_talk:AutoWikiBrowser.xml', ele chama a discussão de uma forma diferente: =Discussion=
arquivo=Xml('Talk:Ethics.xml')

# Escrevendo resultados desejados em arquivos de saída:
# DadosComentario.txt
string=''
dadoscomentario = open('DadosComentario.txt','w')
for discussao in arquivo.discussoes:
        for comentario in discussao.comentarios:
                string=str(discussao.numDiscussao)+' '+str(comentario.numComentario)+' '+str(comentario.numCaracteres)+' '+str(comentario.numPadroes)+'\n'
                dadoscomentario.write(string)
dadoscomentario.close()

#DadosDiscussao.txt
dadosdiscussao = open('DadosDiscussao.txt', 'w')
for discussao in arquivo.discussoes:
        string=str(discussao.numDiscussao)+' '+str(discussao.numComentarios)+' '+str(discussao.numPadroes)+'\n'
        dadosdiscussao.write(string)
dadosdiscussao.close()

# Problemas Encontrados para serem exibidos na tela
i=1
for discussao in arquivo.discussoes:
    j=1
    print '-----------------------\n\n\n', 'Discussao ',i,' - ', discussao.assunto,'\n'
    for comentario in discussao.comentarios:
        if comentario.numPadroes != 0 :
                print 'Comentario ',j,'nivel%s - %s - %s - %s'%(comentario.nivel,comentario.usuario,comentario.data.completa,comentario.posicionamento),'\n',comentario.texto,'\n'
                print 'Comentario ',j,'nivel%s - %s - %s - %s'%(comentario.nivel,comentario.usuario,comentario.data.completa,comentario.posicionamento),'\n'
                for frase in comentario.frases:
                        print frase.texto
                print "\nProblemas: "
                for frase in comentario.frases:
                        if frase.problemas != []:
                                print str(frase.problemas)
        j=j+1
    i=i+1
