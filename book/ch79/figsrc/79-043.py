import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(80)
rows=[(62,'12 ∨ 20','« 12 joint 20 »','60 : un élément','sujet','resultat'),
      (38,'12 ∧ 20','« 12 rencontre 20 »','4 : un élément','sujet','resultat'),
      (14,'12 ≤ 20','« 12 en dessous de 20 »','affirmation : vrai ou faux','autre','autre')]
for y,s,c,rt,r1,r2 in rows:
    box(ax,2,y,34,10,r1,label=s,size='l')
    text(ax,19,y-4,c,r1,'s')
    arrow(ax,(36,y+5),(46,y+5),'varie')
    box(ax,46,y,40,10,r2,label=rt,size='s')
save(fig,'79-043')
