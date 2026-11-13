import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,62,'3 × 3 × 3 = 27 termes','encre','l')
s=7
for k in range(3):
    px=4.5+k*29
    text(ax,px+10.5,55,f'$k={k+1}$','autre','m')
    for i in range(3):
        for j in range(3):
            ok=len({i,j,k})==3
            box(ax,px+j*s,40-(i+1)*s+11,s,s,'resultat' if ok else 'fixe',r=0.4)
box(ax,6,20,6,6,'resultat',r=0.4); text(ax,15,23,'6 : numéros différents','resultat','m',ha='left')
box(ax,6,10,6,6,'fixe',r=0.4); text(ax,15,13,'21 : un numéro répété','fixe','m',ha='left')
save(fig,'76-092')
