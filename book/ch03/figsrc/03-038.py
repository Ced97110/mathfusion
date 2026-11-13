import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
for x,t,r,w in [(20,'18','sujet','bold'),(29,'=','encre','normal'),(38,'6','autre','normal'),(46,'×','encre','normal'),(54,'3','resultat','normal')]:
    text(ax,x,80,t,r,'l',weight=w)
text(ax,20,73,'seul à gauche','sujet','s')
brace(ax,34,58,75,'fixe',label='facteurs, à droite')
for c in (14,26,38,50,62,74):
    for y in (50,54,58): disc(ax,c,y,1.2,'sujet')
    box(ax,c-4,47,8,14,'autre',fill=False,r=0.6)
brace(ax,10,78,45.5,'autre',label='6 parts')
box(ax,10,47,8,14,'resultat',fill=False,lw=2.0,r=0.6)
text(ax,14,64,'3 par part','resultat','s')
text(ax,4,34,'18 : partagé, connu','sujet','s',ha='left'); text(ax,4,27,'6 : partage, connu','autre','s',ha='left'); text(ax,4,20,'3 : cherché','resultat','s',ha='left')
text(ax,4,10,'0 ÷ 7 : le dividende 0 < 7','limite','s',ha='left')
save(fig,'03-038')
