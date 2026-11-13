import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
rows=[(56,'sujet',r"$n=d\times q$   et   $m=d\times q'$",r'$6=3\times 2$  et  $9=3\times 3$'),
      (30,'varie',r"$n\times x+m\times y=d\times(q\times x+q'\times y)$",r'$6\times 4+9\times 5=3\times(2\times 4+3\times 5)$'),
      (4,'resultat',r'$d\times$ (un entier)',r'$3\times 23=69$')]
for y,role,g,nm in rows:
    box(ax,2,y,60,16,role)
    text(ax,32,y+11,g,role,'m'); text(ax,32,y+4.5,nm,'encre','s')
arrow(ax,(32,56),(32,46),'varie'); arrow(ax,(32,30),(32,20),'varie')
text(ax,75,64,'Départ','sujet','m'); text(ax,75,38,'distributivité :\nd en facteur','varie','s'); text(ax,75,12,'Arrivée','resultat','m')
save(fig,'05-019')
