import random
import scipy.constants
import math
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

beta=1
kBT=1/beta
J=1

def NeuesModell():
    Modell=np.ones((100,100),dtype=object)
    x=Modell.shape
    Ei=x[0]
    Ej=x[1]
    for i in range(Ei):
        for j in range(Ej):
            w=np.random.random_sample(2)
            w1=w[0]
            w2=w[1]
            Modell[i,j]=np.array([1,w1*2*np.pi,w2*np.pi])
    return Modell

b=[0.1,0,0] #b=beta*mu*B_null

def sumheisenberg(Modell):
    sh=Modell.shape
    summe=[0,0,0]
    for i in range(sh[0]):
        for j in range(sh[1]):
            summe=summe+to_cartesian(Modell[i,j])
    return summe

def deltahamiltonIsing(i,j,Modell,H1):
    """Berechnet den Unterschied der Energie bei Spinwechsel der ij-ten Komponente"""
    M1=np.array(Modell)
    M2=np.array(Modell)
    M2[i,j]=H1
    diff=2*np.sum(H1*naechsteNachbarn(M2,i,j))-np.sum(b*sumheisenberg(M2))-2*np.sum(M1[i,j]*naechsteNachbarn(M1,i,j))-np.sum(b*sumheisenberg(M1))
    return diff

def to_spherical(x):
    L = [x[0]]
    for xk in x[1:-1]:
        L.append(xk / abs(xk) * (xk ** 2 + L[-1] ** 2) ** 0.5)
        angles = [math.atan(Lk / xk1) for Lk, xk1 in zip(L, x[1:])]
        if x[-1] < 0:
            angles[-1] += math.pi
            radius = sum(xk ** 2 for xk in x) ** 0.5
    return [radius] + angles

def to_cartesian(spherical):
    r = spherical[0]
    angles = spherical[1:]
    pos = []
    for i, angle in enumerate(angles):
        x = r * math.cos(angle)
    for p in angles[i + 1:]:
        x *= math.sin(p)
        pos.append(x)
        first = r
    for p in angles:
        first *= math.sin(p)
        pos.insert(0, first)
    return np.array(pos)

def naechsteNachbarn(Modell,i,j):
    x=Modell.shape
    Ei=x[0]-1
    Ej=x[1]-1
    A=0
    F="Fehler"
    if 0<i<Ei:
        if 0<j<Ej:
            A=to_cartesian(Modell[i+1,j])+to_cartesian(Modell[i-1,j])+to_cartesian(Modell[i,j+1])+to_cartesian(Modell[i,j-1])
        elif j==0:
            A=to_cartesian(Modell[i+1,j])+to_cartesian(Modell[i-1,j])+to_cartesian(Modell[i,j+1])+to_cartesian(Modell[i,Ej])
        elif j==Ej:
            A=to_cartesian(Modell[i+1,j])+to_cartesian(Modell[i-1,j])+to_cartesian(Modell[i,j-1])+to_cartesian(Modell[i,0])
        else:
            print(F)
    elif i==0:
        if 0<j<Ej:
            A=to_cartesian(Modell[i+1,j])+to_cartesian(Modell[i,j+1])+to_cartesian(Modell[i,j-1])+to_cartesian(Modell[Ei,j])
        elif j==0:
            A=to_cartesian(Modell[i+1,j])+to_cartesian(Modell[i,j+1])+to_cartesian(Modell[i,Ej])+to_cartesian(Modell[Ei,j])
        elif j==Ej:
            A=to_cartesian(Modell[i+1,j])+to_cartesian(Modell[i,j-1])+to_cartesian(Modell[Ei,j])+to_cartesian(Modell[i,0])
        else:
            print(F)
    elif i==Ei:
        if 0<j<Ej:
            A=to_cartesian(Modell[i-1,j])+to_cartesian(Modell[i,j+1])+to_cartesian(Modell[i,j-1])+to_cartesian(Modell[0,j])
        elif j==0:
            A=to_cartesian(Modell[i-1,j])+to_cartesian(Modell[i,j+1])+to_cartesian(Modell[0,j])+to_cartesian(Modell[i,Ej])
        elif j==Ej:
            A=to_cartesian(Modell[i-1,j])+to_cartesian(Modell[i,j-1])+to_cartesian(Modell[0,j])+to_cartesian(Modell[i,0])
        else:
            print(F)
    else:
        print(F)
    return A

def simm(Modell):
    x=Modell.shape
    x1=x[0]
    x2=x[1]
    v=random.choice(np.random.random_sample(2))
    for k in range(10000):
        i = random.choice(range(x1))
        l = random.choice(range(x2))
        a = random.choice([-1,1,1,1])
        if a==1:
            w=np.random.random_sample(3)
            H1=to_spherical(2*w[0]*np.array(naechsteNachbarn(Modell,i,l)-to_cartesian(Modell[i,l])+to_cartesian(Modell[i,l])))
            H1[0]=1
            H1[1]=H1[1]%(2*np.pi)
            H1[2]=H1[2]%(np.pi)
            Modell[i,l]=H1
        else:
            w=np.random.random_sample(2)
            H1=(np.array([0,w[0]*2*np.pi,w[1]*np.pi])+Modell[i,l])
            H1[1]=H1[1]%(2*np.pi)
            H1[2]=H1[2]%(np.pi)
    if sum(to_cartesian(H1)*naechsteNachbarn(Modell,i,l))>sum(to_cartesian(Modell[i,l])*naechsteNachbarn(Modell,i,l)):
        Modell[i,l]=H1
    elif v+math.exp(-beta*deltahamiltonIsing(i,l,Modell,H1))> 1.0:
        Modell[i,l]=H1
    return Modell

betarange=np.linspace(0.01,1,num=100)

for beta in betarange:
    beta=beta
    for n in range(50):
        Modell=NeuesModell()
        vgl=np.sum(sumheisenberg(Modell))
        zahl2=0
        while zahl2<100:
            M=simm(Modell)
            vgl2=np.sum(sumheisenberg(M))
            if vgl2>=vgl:
                zahl2=zahl2+1
                vgl=vgl2
                p = np.append(p,M)
                zahl=zahl+1
                np.savetxt('Heisenbergversuch.txt', p)
