import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[(14,r'$4x$'),(30,r'$+\,1$'),(46,r'$-\,3x$'),(62,r'$=\,-8$')]
for x,s in xs: text(ax,x,52,s,'sujet' if 'x' in s else 'encre','l')
text(ax,14,58.5,'$x$ ici','sujet','s'); text(ax,46,58.5,'$x$ là','sujet','s')
arrow(ax,(18,49),(24,40),'varie',curve=0.0); arrow(ax,(46,49),(38,40),'varie')
box(ax,16,33,30,8,'varie',label=r'$4x-3x=x$')
text(ax,70,37,'regrouper','varie','s')
arrow(ax,(31,32),(31,24),'varie')
box(ax,12,10,52,13,'resultat',label=r'$x+1=-8$',size='l')
text(ax,67,16.5,'$x$ une fois','resultat','s',ha='left')
save(fig,'16-081')
