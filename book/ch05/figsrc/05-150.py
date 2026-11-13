import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,2,60,'Quel est le PGCD ?','sujet','m',ha='left')
box(ax,2,44,14,10,'resultat',label='6',size='l')
text(ax,20,49,'une seule réponse','resultat','m',ha='left')
text(ax,2,34,r'Quels coefficients $(u, v)$ ?','varie','m',ha='left')
for i,c in enumerate(['(−1, 1)','(2, −1)','(5, −3)']):
    box(ax,2+25*i,14,22,12,'varie',label=c)
box(ax,77,14,9,12,'varie',fill=False,dash=True,label='…')
text(ax,2,8,'une infinité de réponses','varie','m',ha='left')
save(fig,'05-150')
