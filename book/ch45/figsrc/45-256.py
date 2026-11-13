import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
rows=[(50,[1,2],'sujet'),(34,[1,1],'autre'),(12,[0,0],'resultat')]
for y,v,r in rows:
    for j,x in enumerate(v): box(ax,26+j*14,y,12,10,r,label=str(x),size='l')
text(ax,18,55,'(1, 2)','sujet','m',ha='right'); text(ax,18,39,'(1, 1)','autre','m',ha='right'); text(ax,18,17,'(0, 0)','resultat','m',ha='right')
text(ax,32,62,'mod 2','fixe','s'); text(ax,46,62,'mod 3','fixe','s')
text(ax,24,29,'+','varie','xl')
line(ax,[(26,30),(52,30)],'varie',lw=0.8)
text(ax,70,48,'1 + 1 = 0','fixe','s'); text(ax,70,40,'2 + 1 = 0','fixe','s')
text(ax,70,26,'G ⊕ H = G × H','resultat','s')
save(fig,'45-256')
