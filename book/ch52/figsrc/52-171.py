import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,50,57,'reste par 3','varie','s')
text(ax,5,28,'reste par 2','sujet','s',rot=90)
cw,ch=22,13; ox,oy=14,12
for c in range(3): text(ax,ox+c*cw+cw/2,oy+2*ch+3.5,str(c),'varie','m')
for r in range(2): text(ax,ox-3.5,oy+r*ch+ch/2,str(1-r) if False else str(1-r),'sujet','m')
for n in range(6):
    r=n%2; c=n%3
    box(ax,ox+c*cw+0.8,oy+(1-r)*ch+0.8,cw-1.6,ch-1.6,'resultat',label=str(n),size='l')
text(ax,50,5,'6 classes dans 6 cases','resultat','s')
save(fig,'52-171')
