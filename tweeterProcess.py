#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import regex
import json
from pattern.es import parsetree
from textblob import TextBlob 

class TweeterProcess:

    def __init__(self):
        self.p_vacias = self.getPalabrasVacias()
        self._lemmas = self.getLemmasList()
        self.sdal = self.getSDAL()

    # procesamiento de tweets

    # carga de palabras vacias, lemmas, y SDAL

    #carga de Tweets

    # graba archivo de entranemiento en arff
    def saveToArff(self):
        fp = open('./Tweets/tweets.txt', 'r')
        line = fp.readline()

         #abrir training json file
        tfp = open('./Listas/entrenamiento.arff', 'w')
        tfp.write('@RELATION type_of_sentence\n')
        tfp.write('\n')
        tfp.write('@ATTRIBUTE freq_positive_adj         NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_negative_adj         NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_positive_verb        NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_negative_verb        NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_positive_noun        NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_negative_noun        NUMERIC\n')
        tfp.write('@ATTRIBUTE class                     {pos, neg, neu}\n')
        tfp.write('\n')
        tfp.write('@DATA\n')

        while line:
            prTweet = self.processTweet(line)
            tfp.write(
                str(prTweet[1][1]) + ',' +
                str(prTweet[1][2]) + ',' +
                str(prTweet[1][3]) + ',' +
                str(prTweet[1][4]) + ',' +
                str(prTweet[1][5]) + ',' +
                str(prTweet[1][6]) + ',' +
                str(prTweet[2]) + '\n'
            )
            line = fp.readline()

        tfp.close()
        fp.close()

    def saveTestToArff(self):
        fp = open('./Tweets/tweets.txt', 'r')
        line = fp.readline()

         #abrir training json file
        tfp = open('./Listas/entrenamiento.arff', 'w')
        tfp.write('@RELATION type_of_sentence\n')
        tfp.write('\n')
        tfp.write('@ATTRIBUTE freq_positive_adj         NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_negative_adj         NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_positive_verb        NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_negative_verb        NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_positive_noun        NUMERIC\n')
        tfp.write('@ATTRIBUTE freq_negative_noun        NUMERIC\n')
        tfp.write('@ATTRIBUTE class                     {pos, neg, neu}\n')
        tfp.write('\n')
        tfp.write('@DATA\n')

        while line:
            prTweet = self.processTweet(line)
            tfp.write(
                str(prTweet[1][1]) + ',' +
                str(prTweet[1][2]) + ',' +
                str(prTweet[1][3]) + ',' +
                str(prTweet[1][4]) + ',' +
                str(prTweet[1][5]) + ',' +
                str(prTweet[1][6]) + ',' +
                str(prTweet[2]) + '\n'
            )
            line = fp.readline()

        tfp.close()
        fp.close()

    # procesa con el algoritmo un string
    def processTweet(self, tweet):
        carac = self.getCaracteristicas(tweet)
        cal = self.getEvaluacionTweet(carac)
        print(cal)
        return (carac, cal, self.getLabelFromCal(cal[0]))
    
    # devuelve una lista con las palabras clave del tweet
    def getCaracteristicas(self, tweet):
        wordList = self.getListaAsUtf(tweet.split())
        lemmas = self.getLemmas(wordList)
        lemmas.extend(regex.findall(r'\X',tweet))
        unigramas = self.getUnigramas(lemmas)
        return unigramas

    #retorna una tupla con la calificacion numerica y el vector de caracteristicas (cantidad de adjetivos, verbos y sustantivos) 
    def getEvaluacionTweet(self, caracteristicas):
        calificacion = self.getEvaluationUnigrama(caracteristicas)
        return calificacion

    #grabar json con el formato para textblob
    def saveToTrainJson(self):
        fp = open('./Tweets/tweets.txt', 'r')
        line = fp.readline()

         #abrir training json file
        tfp = open('./Listas/Train.json', 'w')
        tfp.write('[\n')

        while line:
            prTweet = self.processTweet(line)
            self.writeTweetEvalToJson(self.listAsString(prTweet[0]), prTweet[2], prTweet[1],  tfp)
            line = fp.readline()

        tfp.write(']')
        tfp.close()
        fp.close()

    # devuelve una lista de palabra como una lista de palabras en utf8
    def getListaAsUtf(self, wordList):
        utf = []
        for word in wordList:
            if isinstance(word, str):
                utf.append(word.decode('utf-8'))
            else:
                utf.append(word)
        return utf

    # funcion que carga la lista de lemmas para el idioma espanol
    def getLemmasList(self):
        auxDict = {}
        fp = open('./Listas/lemmatization-es.txt', 'r')
        lemmasList = fp.readlines()
        for lemma in lemmasList:
            wordList = lemma.split()
            for word in wordList:
                word = word.decode('utf-8')
            auxDict[wordList[1]]=wordList[0]
        return auxDict

    # carga la lista de palabra vacias -- Falta revisar: muchas palabras si tienen significado en esta lista
    def getPalabrasVacias(self, ):
        _p_vacias = []
        # agregar URL, u otras que palabras quemadas
        fp = open('./Listas/Vacias.txt', 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            _p_vacias.append(word.decode('utf-8'))
            line = fp.readline()
        fp.close()
        return _p_vacias

    # Funcion que filtra las palabras vacias y devuelve solo la lista de palabras con significado
    def getUnigramas(self, words):
        v_caracteristicas = []
        for word in words:
            if word in self.p_vacias:
                continue
            else:
                v_caracteristicas.append(word.lower())
        return v_caracteristicas

    # Funcion para lemmatizar con la libreria parse
    def getLemmas(self, words):
        lemmas = []
        for word in words:
            lemmas.append(parsetree(word, lemmata=True)[0].lemma[0])
        return lemmas

    # getEvaluationUnigrama
    # obtiene la evaluacion de la lista de caracteristicas con el diccionario SDAL
    # Agrega todos las avaluaciones de las palabras y divide por el numero de palabras evaluadas
    # Paara los verbos y los adjetivos se les dio un mayor peso en la calificaion 
    def getEvaluationUnigrama(self, caracteristicas):
        score = 0
        count = 0
        freq_adj_pos = 0
        freq_adj_neg = 0
        freq_ver_pos = 0
        freq_ver_neg = 0
        freq_sus_pos = 0
        freq_sus_neg = 0
        if len(caracteristicas) == 0:
            return (0, freq_adj_pos, freq_adj_neg, freq_ver_pos, freq_ver_neg, freq_sus_pos, freq_sus_neg) 
        for word in caracteristicas:
            if word in self.sdal:
                pleasantness = float(self.sdal[word]['pleasantness'])
                if(pleasantness < 0):
                    pleasantness = pleasantness * 2
                if self.sdal[word]['obj'] == u'N' or self.sdal[word]['obj'] == u'R':
                    score += pleasantness
                    if pleasantness < 0:
                        freq_sus_neg += 1
                    else:
                        freq_sus_pos += 1
                elif self.sdal[word]['obj'] == u'V':
                    score += pleasantness * 1.1
                    if pleasantness < 0:
                        freq_ver_neg += 1
                    else:
                        freq_ver_pos += 1
                elif self.sdal[word]['obj'] == u'A':
                    score += pleasantness * 1.2
                    if pleasantness < 0:
                        freq_adj_neg += 1
                    else:
                        freq_adj_pos += 1
                else:
                    score += pleasantness
                count += 1
        if count == 0:
            return (0, freq_adj_pos, freq_adj_neg, freq_ver_pos, freq_ver_neg, freq_sus_pos, freq_sus_neg) 
        return (score / count, freq_adj_pos, freq_adj_neg, freq_ver_pos, freq_ver_neg, freq_sus_pos, freq_sus_neg) 

    #Evaluacion por digramas - no implementado todavia, ni lo hare
    def getEvaluationDigram(self, caracteristicas):
        if len(caracteristicas) == 0:
            return 0
        digram_calification = []
        for i,k in zip(caracteristicas,caracteristicas[1:]):
            print self.sdal[i]['pleasantness'] + self.sdal[k]['pleasantness']
            if i in self.sdal and k in self.sdal:
                first = float(self.sdal[i]['pleasantness'])
                second = float(self.sdal[k]['pleasantness'])
                print first * second


    # abrir el archivo con el diccionario de palabras y sus calificaciones
    def getSDAL(self, ):
        with open('./Listas/sdal.json') as data_file:
            _sdal = json.load(data_file)
        return _sdal
    # end
        
    # obtener el label de pos, neg, neu dado una calificaion
    def getLabelFromCal(self, cal):
        if cal < -0.1:
            return 'neg'
        elif cal >= -0.1 and cal < 0.1:
            return 'neu'
        elif cal >= 0.1:
            return 'pos'

    # formato json para textblob
    def writeTweetEvalToJson(self, tweet, label, cal , tfp):
        tfp.write('{"text":"' + tweet.encode('utf-8').rstrip('\n') + '","label":"' + label + '","cal":' +  str(cal) + '},\n')

    # retornar la lista de caracteristicas como un string
    def listAsString(self, caracteristicas):
        string = ''
        for word in caracteristicas:
            string = string + word + ' '
        return string[:-1]