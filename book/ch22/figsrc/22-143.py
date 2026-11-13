import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
labs=[r'$\sqrt{4x-5}=-6$',r'$4x-5=36$',r'$4x=41$',r'$x=41/4=10{,}25$',r'$\sqrt{36}=6$, et $6\neq-6$']
roles=['sujet','sujet','sujet','sujet','limite']
acts=['élever au carré','ajouter 5','diviser par 4','vérifier']
ys=[4+(4-i)*15 for i in range(5)]
for i in range(5):
    box(ax,4,ys[i],44 if i<4 else 62,9,roles[i],label=labs[i])
for i in range(4):
    arrow(ax,(26,ys[i]),(26,ys[i+1]+9),'varie'); text(ax,30,ys[i]-3,acts[i],'varie','s',ha='left')
save(fig,'22-143')
