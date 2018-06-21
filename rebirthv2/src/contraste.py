#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Organisme de référence …… : Télécom ParisTech (https://www.telecom-paristech.fr/)
Contexte du projet ……………… : Projet PAF (https://paf.telecom-paristech.fr/)
Sujet ………………………………………………… : Contraste et catégorisation (http://teaching.dessalles.fr/Projects/P18051801.html)
Auteurs …………………………………………… : Bastien Vagne, Louis Penet de Monterno, Benoît Malézieux,Clément Bonet, Aurélien Blicq, Antoine Bellami
Date …………………………………………………… : 19/06/2018
Description du fichier …… : Cartouche
"""

import numpy as np
import pandas as pd

import gmm
import clusterisation

class Contraste:
    
    def __init__(self,clustersList,critere=0.5,numberCluster=3):
        self.clustersList=clustersList
        self.critere=critere
        self.numberCluster=numberCluster
        
    def difference(self,cluster):
        """ return the difference between a dataframe and its center """
        dataframe = cluster.getDataFrame()
        del dataframe['category']
        center = cluster.getCenter()
        diff = abs(dataframe-center)/self.variance(dataframe)
        return diff
             
    def variance(self,dataFrame):
        return dataFrame.var(axis=0)
        
        
    def sharpening(self,diff):
        """ sharps the dataframe in function a critere"""
        
        maxiListe = diff.max(axis=0)
        
        for k in diff.iterrows():
            for j in range(len(k)):
                if(k[1][j]<self.critere*maxiListe[j]):
                    k[1][j]=0  
                
        return diff
        
    def contrast(self):
        """ reapply kmean on each sharpens cluster """

        for cluster in self.clustersList:
            diff = self.difference(cluster)
            sharp = self.sharpening(diff)
            #concaténer
            
        #gmmsur tout 
        newGmm = gmm.GMM(sharp,self.numberCluster)
        newDataFrame, centers = newGmm.result()
            
        print(newDataFrame)
        
            #print(diff)
            
            
    def result(self):
        """ return the dataframe centré réduit sharpené """
        self.contrast()
        return self.clustersList