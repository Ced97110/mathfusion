import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
labs=['1',r'$x$',r'$x^2$',r'$x^3$',r'$x^4$']
for i,l in enumerate(labs): box(ax,9+i*14,66,12,10,'sujet',label=l)
brace(ax,9,9+4*14+12,66,'sujet',label='5 éléments',down=True)
box(ax,9,40,70,10,'fixe',label='espace de dimension 4')
text(ax,44,56,r'$5>4$','varie','m')
arrow(ax,(44,40),(44,31),'varie'); text(ax,62,35.5,'sont liés','varie','s')
box(ax,9,19,70,10,'resultat',label=r'$p(x)=0$, $p$ réel')
arrow(ax,(44,19),(44,10),'varie')
box(ax,9,0.5,70,9,'resultat',label=r'un facteur de degré $\leq 2$ : 0')
save(fig,'78-148')
