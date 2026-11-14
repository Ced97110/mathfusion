import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
s=14; gx=42; gy=14
H=[1,3];K=[1,5]
for j,k in enumerate(K):
    box(ax,gx+j*s,gy+2*s,s,8,'autre',label=str(k))
for i,h in enumerate(H):
    box(ax,gx-s,gy+(1-i)*s,s,s,'sujet',label=str(h))
    for j,k in enumerate(K):
        p=(h*k)%8
        box(ax,gx+j*s,gy+(1-i)*s,s,s,'resultat',label=str(p),size='l')
text(ax,gx-s/2,gy+2*s+4,'×','encre','s')
text(ax,gx+s,gy+2*s+13,'K = {1, 5}','autre','m')
text(ax,gx-s-2,gy+s,'H = {1, 3}','sujet','m',ha='right')
text(ax,gx+s,gy-5,'produits mod 8 : 1, 5, 3, 7','resultat','s')
save(fig,'45-243')
