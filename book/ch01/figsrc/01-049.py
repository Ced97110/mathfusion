import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
line(ax,[(3,20),(85,20)],'fixe',lw=0.9)
for i in range(6):
    x=4+9*i; h=3+4*i
    box(ax,x,20,7,h,'fixe' if i==0 else 'sujet',r=0.3)
    text(ax,x+3.5,16,str(i),'encre','s')
text(ax,14,74,'départ : marche 0','fixe','s')
arrow(ax,(8,72),(7.5,24.5),'fixe',lw=0.7)
tops=[(7.5+9*i,24+4*i) for i in range(6)]
for a,b in zip(tops[:-1],tops[1:]): arrow(ax,a,b,'varie',curve=0.3)
text(ax,24,50,'chaque pas : +20 cm','varie','m')
# axiome 3 : une chaîne ininterrompue qui part de 0 et arrive à 1 000 000
disc(ax,7.5,11,1.2,'fixe')
for i in range(5):
    arrow(ax,(9.2+9*i if i==0 else 8.5+9*i,11),(15.5+9*i,11),'fixe',lw=1.0)
line(ax,[(54,11),(75,11)],'fixe',lw=1.0,dash=True); arrow(ax,(75,11),(77.4,11),'fixe',lw=1.0)
disc(ax,79,11,1.2,'resultat')
text(ax,44,5,'axiome 3 : chaque marche est atteinte depuis 0','fixe','s')
line(ax,[(58,20),(72,20)],'fixe',dash=True)
line(ax,[(49,43),(56,43)],'resultat',lw=1.6)
text(ax,30,60,'marche 5 : une seule valeur','resultat','s')
line(ax,[(40,58.5),(51,44)],'resultat',lw=0.7)
line(ax,[(48,48),(57,48)],'limite',dash=True)
line(ax,[(51.5,47),(53.5,49)],'limite'); line(ax,[(51.5,49),(53.5,47)],'limite')
text(ax,62,54,'pas de 2e valeur','limite','s')
box(ax,74,20,10,26,'sujet',r=0.3); box(ax,74,50,10,12,'sujet',r=0.3)
box(ax,74,50,10,12,'resultat',fill=False,lw=1.4,r=0.3)
line(ax,[(73,45),(85,47)],'fixe'); line(ax,[(73,49),(85,51)],'fixe')
text(ax,79,16,'1 000 000','encre','s')
text(ax,76,68,'hauteur définie','resultat','s')
save(fig,'01-049')
