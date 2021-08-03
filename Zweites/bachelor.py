import random
import scipy.constants
import math
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

def NeuesModell():
    Modell=np.ones((50,50),dtype=int)
    x=Modell.shape
    Ei=x[0]
    Ej=x[1]
    for i in range(Ei):
        for j in range(Ej):
            Modell[i,j]=random.choice([-1,1])
    return np.array(Modell)

def korrelationpl(r,Modell):
    x=Modell.shape
    Ei=x[0]-1
    Ej=x[1]-1
    A=0
    for i in range(Ei):
        for j in range(Ej):
            if i<=Ei-r:
                if j<=Ej-r:
                    A1=Modell[i,j]*Modell[i+r,j]+Modell[i,j]*Modell[i,j+r]
                    A=A+A1
                elif j>Ej-r:
                    A1=Modell[i,j]*Modell[i+r,j]+Modell[i,j]*Modell[i,r-(Ej-j)-1]
                    A=A+A1
                else:
                    print(F)
            elif i>Ei-r:
                if j<=Ej-r:
                    A1=Modell[i,j]*Modell[r-(Ei-i)-1,j]+Modell[i,j]*Modell[i,j+r]
                    A=A+A1
                elif j>Ej-r:
                    A1=Modell[i,j]*Modell[r-(Ei-i)-1,j]+Modell[i,j]*Modell[i,r-(Ej-j)-1]
                    A=A+A1
                else:
                    print(F)
                    A=A/(2*Ei*Ej)
    return A

def naechsteNachbarn(Modell,i,j):
    x=Modell.shape
    Ei=x[0]-1
    Ej=x[1]-1
    A=0
    F="Fehler"
    if 0<i<Ei:
        if 0<j<Ej:
            A=Modell[i,j]*Modell[i+1,j]+Modell[i,j]*Modell[i-1,j]+Modell[i,j]*Modell[i,j+1]+Modell[i,j]*Modell[i,j-1]
        elif j==0:
            A=Modell[i,j]*Modell[i+1,j]+Modell[i,j]*Modell[i-1,j]+Modell[i,j]*Modell[i,j+1]+Modell[i,j]*Modell[i,Ej]
        elif j==Ej:
            A=Modell[i,j]*Modell[i+1,j]+Modell[i,j]*Modell[i-1,j]+Modell[i,j]*Modell[i,j-1]+Modell[i,j]*Modell[i,0]
        else:
            print(F)
    elif i==0:
        if 0<j<Ej:
            A=Modell[i,j]*Modell[i+1,j]+Modell[i,j]*Modell[i,j+1]+Modell[i,j]*Modell[i,j-1]+Modell[i,j]*Modell[Ei,j]
        elif j==0:
            A=Modell[i,j]*Modell[i+1,j]+Modell[i,j]*Modell[i,j+1]+Modell[i,j]*Modell[i,Ej]+Modell[i,j]*Modell[Ei,j]
        elif j==Ej:
            A=Modell[i,j]*Modell[i+1,j]+Modell[i,j]*Modell[i,j-1]+Modell[i,j]*Modell[Ei,j]+Modell[i,j]*Modell[i,0]
        else:
            print(F)
    elif i==Ei:
        if 0<j<Ej:
            A=Modell[i,j]*Modell[i-1,j]+Modell[i,j]*Modell[i,j+1]+Modell[i,j]*Modell[i,j-1]+Modell[i,j]*Modell[0,j]
        elif j==0:
            A=Modell[i,j]*Modell[i-1,j]+Modell[i,j]*Modell[i,j+1]+Modell[i,j]*Modell[0,j]+Modell[i,j]*Modell[i,Ej]
        elif j==Ej:
            A=Modell[i,j]*Modell[i-1,j]+Modell[i,j]*Modell[i,j-1]+Modell[i,j]*Modell[0,j]+Modell[i,j]*Modell[i,0]
        else:
            print(F)
    else:
        print(F)
        A=-A
    return A

def deltahamiltonIsing(i,j,Modell):
    M1=np.array(Modell)
    M2=np.array(Modell)
    M2[i,j]=-M2[i,j]
    diff=(naechsteNachbarn(M2,i,j)-b*np.sum(M2))-(naechsteNachbarn(M1,i,j)-b*np.sum(M1))
    return diff

def sim(Modell):
    Modell=NeuesModell()
    Mod=[Modell]
    x=Modell.shape
    x1=x[0]
    x2=x[1]
    mag1=np.sum(Modell)
    for k in range(1000):
        if sum(sum(Modell))==x1*x2:
            break
        i = random.choice(range(x1))
        l = random.choice(range(x2))
        w=random.choice(np.random.random_sample(2))
        if deltahamiltonIsing(i,l,Modell)<0:
            Modell[i,l]=-Modell[i,l]
        elif w+math.exp(-beta*deltahamiltonIsing(i,l,Modell))> 1.0:
            Modell[i,l]=-Modell[i,l]
            mag2=np.sum(Modell)
            Mod=np.append(Mod,[Modell],axis=0)
            h=1
            zahl=0
    while zahl<100:
        if mag1==mag2:
            zahl=zahl+1
            Modell=Mod[h]
            mag1=np.sum(Mod[h])
            for k in range(1000):
                if np.sum(Modell)==x1*x2:
                    break
                i = random.choice(range(x1))
                l = random.choice(range(x2))
                w=random.choice(np.random.random_sample(2))
                if deltahamiltonIsing(i,l,Modell)<0:
                    Modell[i,l]=-Modell[i,l]
                elif w<math.exp(-beta*deltahamiltonIsing(i,l,Modell)):
                    Modell[i,l]=-Modell[i,l]
                    Mod=np.append(Mod,[Modell],axis=0)
                    h=h+1
                    mag2=np.sum(Mod[h])
    return np.array(Modell)

betarange=np.linspace(0.01,1,num=100)
o= np.loadtxt("Durchlauf.txt")
m=np.reshape(o,(-1,50,50))
b=0
zahl=0
p=[]
for beta in betarange:
    beta=beta
for n in range(50):
    Modell=NeuesModell()
    vgl=np.sum(Modell)
    zahl2=0
while zahl2<1000:
    M=sim(Modell)
    vgl2=np.sum(M)
    if vgl2>=vgl:
        zahl2=zahl2+1
        vgl=vgl2
        p = np.append(p,M)
        zahl=zahl+1
np.savetxt('Durchlauf.txt',o)
