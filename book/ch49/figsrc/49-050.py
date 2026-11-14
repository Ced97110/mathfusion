import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
L=[('x','sujet'),('y','varie'),(r'$y^{-1}$','varie'),('x','sujet')]
for i,(s,r) in enumerate(L): box(ax,3+9*i,22,8,8,r,label=s)
R=['x','x']
for i,s in enumerate(R): box(ax,60+9*i,22,8,8,'resultat',label=s)
text(ax,20.5,36,'mot non réduit','fixe','s'); text(ax,68.5,36,'mot réduit','resultat','s')
arrow(ax,(40,26),(57,26),'varie',lw=1.3); text(ax,48.5,30.5,'effacer','varie','s')
brace(ax,12,29,21,'varie',label='paire à effacer')
brace(ax,60,77,21,'resultat',label='aucune paire')
save(fig,'49-050')
