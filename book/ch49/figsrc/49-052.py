import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for i,(s,r) in enumerate([('x','sujet'),('y','varie'),(r'$y^{-1}$','varie'),('x','sujet')]): box(ax,24+10*i,44,9,9,r,label=s)
brace(ax,34,53,53,'varie',label=r'paire $y\,y^{-1}$',down=False)
text(ax,3,48.5,'départ','fixe','s',ha='left')
arrow(ax,(44,43),(44,33),'varie'); text(ax,48,38,'on efface la paire','varie','s',ha='left')
box(ax,34,22,9,9,'resultat',label='x'); box(ax,44,22,9,9,'resultat',label='x')
text(ax,3,26.5,'mot réduit','resultat','s',ha='left')
save(fig,'49-052')
