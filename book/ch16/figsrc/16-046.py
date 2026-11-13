import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,4,50,34,12,'sujet',label=r'$x+7=11$',size='l')
text(ax,42,56,'7 encore attaché à x','varie','s',ha='left')
arrow(ax,(21,50),(21,31),'varie'); text(ax,25,40.5,'retirer 7 des deux membres','varie','s',ha='left')
box(ax,4,18,34,12,'resultat',label=r'$x=4$',size='l')
text(ax,42,24,'x est seule : on s\'arrête','resultat','s',ha='left')
text(ax,21,12,'solution lue','resultat','s')
save(fig,'16-046')
