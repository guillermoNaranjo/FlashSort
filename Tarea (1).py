# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:58:04 2020

@author: memon, sdulongs
"""
import math
import random 
import time
import matplotlib.pyplot as plt

def arregloOrden(n):
    arr=[]
    for i in range(n):
        arr.append(i)
    return arr

def arregloInverso(n):
    arr=[]
    k=n
    for i in range(n):
        arr.append(k)
        k-=1
    return arr

def arregloRandom(n):
    arr=[]
    for i in range(n):
        k=random.randint(0,999)
        arr.append(k)
    return arr

def flash_sort(arr):
    min=arr[0]
    max=0
    n=len(arr)
    c=0.43
    if n<5:
        c=0.51
    m=math.floor(c*n)
    l=[]

    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
        if arr[max]<arr[i]:
            max=i
    if arr[max]==min:
        return arr

    c1=(m-1)/(arr[max]-min)
    
    for i in range(0,m):
        l.append(0)
        
    for i in range(0,n):
        k=math.floor(c1*(arr[i]-min))
        l[k]+=1
        
    for i in range(1,m):
        l[i]+=l[i-1]
        
    arr[max],arr[0]=arr[0],arr[max]
    
    #Permutacion 
    move=0
    j=0
    k=m-1
    while (n-1) > move:
        while j>l[k]-1:
            j+=1
            k=math.floor(c1*(arr[j]-min))
        while j!=l[k]:
            k=math.floor(c1*(arr[j]-min))
            l[k]-=1
            arr[j], arr[l[k]] = arr[l[k]], arr[j]
            move+=1

    #Insercion directa
    for i in range(1,n):
        hold=arr[i]
        hueco=i-1
        while hueco>=0 and hold<arr[hueco]:
            arr[hueco+1]=arr[hueco]
            hueco-=1
        arr[hueco+1]=hold   
    return arr

def ordenamiento_por_seleccion_directa(lista_valores):    
    i=0    
    while i<len(lista_valores):        
        min=i        
        indices=list(range(i+1,len(lista_valores)))        
        for indice in indices:            
            if lista_valores[indice]<lista_valores[min]:                
                min=indice        
        #Intercambio de los valores de lista_valores[min] y lista_valores[i]:        
        lista_valores[min],lista_valores[i]=lista_valores[i],lista_valores[min]        
        i=i+1

def ordenamiento_por_insercion_directa(lista_valores):
    i=1
    while i<len(lista_valores):
        sig=lista_valores[i]
        hueco=i
        while hueco>0 and sig<lista_valores[hueco-1]:
            lista_valores[hueco]=lista_valores[hueco-1]
            hueco=hueco-1
        lista_valores[hueco]=sig
        i=i+1

def merge_sort(lista_valores):
    merge_sort_r(lista_valores,0,len(lista_valores)-1)

def merge_sort_r(lista_valores,lim_inf,lim_sup):    
    if lim_inf<lim_sup:        
        indice_intermedio=lim_inf+(lim_sup-lim_inf)//2        
        merge_sort_r(lista_valores,lim_inf,indice_intermedio)        
        merge_sort_r(lista_valores,indice_intermedio+1,lim_sup)        
        merge(lista_valores,lim_inf,indice_intermedio,lim_sup)
        
def merge(lista_valores,lim_inf,indice_intermedio,lim_sup):    
    aux=list(lista_valores)    
    i=lim_inf    
    j=indice_intermedio+1    
    k=lim_inf    
    while i<=indice_intermedio and j<=lim_sup:        
        if aux[i]<=aux[j]:            
            lista_valores[k]=aux[i]            
            i=i+1        
        else:            
            lista_valores[k]=aux[j]            
            j=j+1
        k=k+1    
    while i<=indice_intermedio:        
        lista_valores[k]=aux[i]        
        k=k+1        
        i=i+1    
    while j<=lim_sup:        
        lista_valores[k]=aux[j]        
        k=k+1        
        j=j+1
                
def test():
    valores_x=[]
    valores_y_Flash_Sort_orden=[]
    valores_y_Flash_Sort_inverso=[]
    valores_y_Flash_Sort_random=[]
    tamano=5
    incremento=5
    tamano_final=1000
    while tamano<=tamano_final:
        valores_x=valores_x+[tamano]
        lista_ordenada=arregloOrden(tamano)
        lista_inversa=arregloInverso(tamano)
        lista_randon=arregloRandom(tamano)
        for lista in [lista_ordenada, lista_inversa, lista_randon]:
            time_before=time.perf_counter()
            flash_sort(lista)
            time_after=time.perf_counter()
            diff=time_after - time_before
            if lista==lista_ordenada:
                valores_y_Flash_Sort_orden=valores_y_Flash_Sort_orden+[diff]
            elif lista==lista_inversa:
                valores_y_Flash_Sort_inverso=valores_y_Flash_Sort_inverso+[diff]
            elif lista==lista_randon:
                valores_y_Flash_Sort_random=valores_y_Flash_Sort_random+[diff]
        tamano+=incremento
    plt.xlabel("# de Datos")
    plt.ylabel("unidades de Tiempo")
    plt.plot(valores_x, valores_y_Flash_Sort_inverso, label="Arreglo inverso")
    plt.plot(valores_x, valores_y_Flash_Sort_orden, label="Arreglo orden")
    plt.plot(valores_x, valores_y_Flash_Sort_random, label="Arreglo random")
    plt.legend(loc="upper left")



def test_promedio():
    valores_x=[]
    valores_y_Flash_Sort_orden=[]
    valores_y_Flash_Sort_inverso=[]
    valores_y_Flash_Sort_random=[]
    tamano=5
    incremento=5
    tamano_final=1000
    while tamano<=tamano_final:
        valores_x=valores_x+[tamano]
        lista_ordenada=arregloOrden(tamano)
        lista_inversa=arregloInverso(tamano)
        lista_randon=arregloRandom(tamano)
        for lista in [lista_ordenada, lista_inversa, lista_randon]:
            prom=0
            for i in range(0,10):
                copia=list(lista)
                time_before=time.perf_counter()
                flash_sort(copia)
                time_after=time.perf_counter()
                diff=time_after-time_before
                prom+=diff
            prom=prom/10
            if lista==lista_ordenada:
                valores_y_Flash_Sort_orden=valores_y_Flash_Sort_orden+[prom]
            elif lista==lista_inversa:
                valores_y_Flash_Sort_inverso=valores_y_Flash_Sort_inverso+[prom]
            elif lista==lista_randon:
                valores_y_Flash_Sort_random=valores_y_Flash_Sort_random+[prom]
        tamano+=incremento
    plt.xlabel("# de Datos")
    plt.ylabel("unidades de Tiempo")
    plt.plot(valores_x, valores_y_Flash_Sort_inverso, label="Arreglo inverso")
    plt.plot(valores_x, valores_y_Flash_Sort_orden, label="Arreglo orden")
    plt.plot(valores_x, valores_y_Flash_Sort_random, label="Arreglo random")
    plt.legend(loc="upper left")

def test_completo():
    valores_x=[]
    valores_y_Flash_Sort_inverso=[]
    valores_y_Flash_Sort_orden=[]
    valores_y_Flash_Sort_random=[]
    valores_y_insercion_directa_inverso=[]
    valores_y_insercion_directa_orden=[]
    valores_y_insercion_directa_random=[]
    valores_y_seleccion_directa_inverso=[]
    valores_y_seleccion_directa_orden=[]
    valores_y_seleccion_directa_random=[]
    valores_y_merge_sort_inverso=[]
    valores_y_merge_sort_orden=[]
    valores_y_merge_sort_random=[]
    tamano=5
    incremento=5
    tamano_final=1000
    while tamano<tamano_final:
        valores_x+=[tamano]
        lista_ordenada=arregloOrden(tamano)
        lista_inversa=arregloInverso(tamano)
        lista_random=arregloRandom(tamano)
        lista_metodos=[flash_sort, ordenamiento_por_seleccion_directa, ordenamiento_por_insercion_directa, merge_sort]
        listas=[lista_ordenada, lista_inversa, lista_random]
        for metodo in lista_metodos:
            for lista in listas:
                copia=list(lista)
                time_before=time.perf_counter()
                metodo(copia)
                time_after=time.perf_counter()
                diff=time_after - time_before
                if metodo is flash_sort:
                    if lista is lista_inversa:
                        valores_y_Flash_Sort_inverso+=[diff]
                    elif lista is lista_ordenada:
                        valores_y_Flash_Sort_orden+=[diff]
                    elif lista is lista_random:
                        valores_y_Flash_Sort_random+=[diff]
                elif metodo is merge_sort:
                    if lista is lista_inversa:
                        valores_y_merge_sort_inverso+=[diff]
                    elif lista is lista_ordenada:
                        valores_y_merge_sort_orden+=[diff]
                    elif lista is lista_random:
                        valores_y_merge_sort_random+=[diff]
                elif metodo is ordenamiento_por_insercion_directa:
                    if lista is lista_inversa:
                        valores_y_insercion_directa_inverso+=[diff]
                    elif lista is lista_ordenada:
                        valores_y_insercion_directa_orden+=[diff]
                    elif lista is lista_random:
                        valores_y_insercion_directa_random+=[diff]
                elif metodo is ordenamiento_por_seleccion_directa:
                    if lista is lista_inversa:
                        valores_y_seleccion_directa_inverso+=[diff]
                    elif lista is lista_ordenada:
                        valores_y_seleccion_directa_orden+=[diff]
                    elif lista is lista_random:
                        valores_y_seleccion_directa_random+=[diff]
        tamano+=incremento
    plt.figure("Arreglo Inverso")
    plt.xlabel("Número de Datos")
    plt.ylabel("Unidades de tiempo")
    plt.plot(valores_x, valores_y_Flash_Sort_inverso, label="Flash Sort inverso")
    plt.plot(valores_x, valores_y_insercion_directa_inverso, label="Insercion Directa inverso")
    plt.plot(valores_x, valores_y_merge_sort_inverso, label="Merge Sort inverso")
    plt.plot(valores_x, valores_y_seleccion_directa_inverso, label="Selección Directa inverso")
    plt.legend(loc="upper left")
    plt.figure("Arreglo Orden")
    plt.xlabel("Número de Datos")
    plt.ylabel("Unidades de Tiempo")
    plt.plot(valores_x, valores_y_Flash_Sort_orden, label="Flash Sort orden")
    plt.plot(valores_x, valores_y_insercion_directa_orden, label="Insercion Directa orden")
    plt.plot(valores_x, valores_y_merge_sort_orden, label="Merge Sort orden")
    plt.plot(valores_x, valores_y_seleccion_directa_orden, label="Selección Directa orden")
    plt.legend(loc="upper left")
    plt.figure("Arreglo Random")
    plt.xlabel("Número de Datos")
    plt.ylabel("Unidades de Tiempo")
    plt.plot(valores_x, valores_y_Flash_Sort_random, label="Flash Sort random")
    plt.plot(valores_x, valores_y_insercion_directa_random, label="Insercion Directa random")
    plt.plot(valores_x, valores_y_merge_sort_random, label="Merge Sort random")
    plt.plot(valores_x, valores_y_seleccion_directa_random, label="Selección Directa random")
    plt.legend(loc="upper left")
    
arr=arregloRandom(7)
print(arr)
print(flash_sort(arr))

test_completo()
                    
                    
                        
                
        
    
    





          
            
            
            
            
            
        
        
        
            