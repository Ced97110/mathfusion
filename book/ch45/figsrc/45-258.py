import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
rows=[(42,[1,1,0],'sujet'),(28,[0,1,1],'autre'),(10,[1,0,1],'resultat')]
for y,v,r in rows:
    for j,x in enumerate(v): box(ax,34+j*13,y,11,10,r,label=str(x),size='l')
text(ax,28,47,'110','sujet','s',ha='right'); text(ax,28,33,'011','autre','s',ha='right'); text(ax,28,15,'101','resultat','s',ha='right')
text(ax,24,37,'+','varie','xl')
line(ax,[(34,26),(72,26)],'varie',lw=0.8)
text(ax,44,57,'case par case, modulo 2','varie','s')
text(ax,44,3,'n = 3 : 8 mots possibles','fixe','s')
save(fig,'45-258')
