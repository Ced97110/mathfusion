import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,53,r'gris : $\bar0$ ; vert : inversibles','encre','s')
for y,p in [(40,2),(26,7),(12,13)]:
    text(ax,10,y+3,f'p = {p}','sujet','s')
    for i in range(p): box(ax,20+i*4.2,y,3.6,6,'fixe' if i==0 else 'resultat',r=0.3,lw=0.6)
    text(ax,76,y+3,rf'$\varphi={p-1}$','resultat','s',ha='left')
brace(ax,24.2,20+13*4.2-0.6,11,'resultat',label=r'$p-1$ classes')
save(fig,'52-090')
