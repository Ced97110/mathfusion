import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
s=13; gx=34; gy=12
H=[0,2,4];K=[0,3]
for j,k in enumerate(K):
    box(ax,gx+j*s,gy+3*s,s,8,'autre',label=str(k))
for i,h in enumerate(H):
    box(ax,gx-s,gy+(2-i)*s,s,s,'sujet',label=str(h))
    for j,k in enumerate(K):
        box(ax,gx+j*s,gy+(2-i)*s,s,s,'resultat',label=str((h+k)%6),size='l')
text(ax,gx+s,gy+3*s+13,'K = {0, 3}','autre','m')
text(ax,gx-s-2,gy+1.5*s,'H = {0, 2, 4}','sujet','m',ha='right')
text(ax,gx+s,gy-5,'6 sommes : 0 à 5, toutes','resultat','s')
save(fig,'45-244')
