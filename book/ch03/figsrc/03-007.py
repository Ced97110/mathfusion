import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,3,64,'groupes de 4 carreaux','resultat','s',ha='left')
for gx in (4,14,24):
    box(ax,gx,48,8,8,'resultat',fill=False,r=0.5)
    for i in range(2):
        for j in range(2): box(ax,gx+1+3*i,49+3*j,3,3,'sujet',r=0.3,lw=0.5)
text(ax,36,52,'reste 0','resultat','m',ha='left')
text(ax,3,38,'groupes de 0 carreau','limite','s',ha='left',weight='bold')
for bx in (4,38,72):
    for i in range(4):
        for j in range(3): box(ax,bx+3*i,14+3*j,3,3,'sujet',r=0.3,lw=0.5)
    text(ax,bx+6,10,'reste 12','sujet','s')
arrow(ax,(17,18.5),(37,18.5),'limite'); arrow(ax,(51,18.5),(71,18.5),'limite')
text(ax,27,25.5,'10 groupes vides','limite','s'); text(ax,61,25.5,"jusqu'à 1 000 groupes",'limite','s')
for x in (20,24,28,32,54,58,62,66): box(ax,x,29,3,3,'limite',fill=False,dash=True,r=0.3,lw=0.6)
save(fig,'03-007')
