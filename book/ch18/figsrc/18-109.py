import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def tok(x,y,t,role): box(ax,x,y,16,9,role,label=t,size='s')
text(ax,2,56,r'$x^2-9$','fixe','m',ha='left'); tok(24,52,r'$x+3$','varie'); tok(42,52,r'$x-3$','sujet')
text(ax,2,40,r'$x^2+5x+6$','fixe','m',ha='left'); tok(24,36,r'$x+2$','autre'); tok(42,36,r'$x+3$','varie')
text(ax,2,17,'PPCM','resultat','m',ha='left',weight='bold'); tok(24,13,r'$x+2$','autre'); tok(42,13,r'$x+3$','varie'); tok(60,13,r'$x-3$','sujet')
text(ax,70,45,'facteur commun','varie','s'); text(ax,70,40,'une seule fois','varie','s')
text(ax,44,4,r'comme $4$, $6$ : $2\times2\times3=12$','fixe','s')
save(fig,'18-109')
