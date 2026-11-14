import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,2,47.5,'produit','autre','s',ha='left'); text(ax,2,23.5,'quotient','sujet','s',ha='left')
rows=[(34,'autre',[r'$3\times 2=6$',r'$6^2=36$',r'$9\times 4$']),(10,'sujet',[r'$\frac{3}{2}=1{,}5$',r'$1{,}5^2=2{,}25$',r'$\frac{9}{4}$'])]
for y,r,L in rows:
    for i,t in enumerate(L):
        box(ax,2+30*i,y,24,10,role=r,label=t,size='s')
        if i<2: arrow(ax,(26+30*i,y+5),(32+30*i,y+5),'varie')
text(ax,44,3.5,'même preuve : carré, puis égalité','resultat','s')
save(fig,'22-062')
