import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,s=26,33,15
poly(ax,[(cx-s,cy-s),(cx+s,cy-s),(cx+s,cy+s),(cx-s,cy+s)],'fixe',fill=False)
V={'A':(cx-s,cy-s),'B':(cx+s,cy-s),'C':(cx+s,cy+s),'D':(cx-s,cy+s)}
arrow(ax,(V['A'][0]+3,V['A'][1]-3),(V['B'][0]-3,V['B'][1]-3),'varie',curve=0.35)
arrow(ax,(V['A'][0]+2,V['A'][1]+2),(V['C'][0]-2,V['C'][1]-2),'varie')
arrow(ax,(V['A'][0]-3,V['A'][1]+3),(V['D'][0]-3,V['D'][1]-3),'varie',curve=-0.35)
for k,(x,y) in V.items():
    disc(ax,x,y,2.6,'sujet',label=k,size='s')
text(ax,cx,cy-9,r'$\frac{1}{2}$ tour','varie','s')
text(ax,cx,cy-s-9,r'$\frac{1}{4}$ de tour','varie','s')
text(ax,cx-s-3,cy,r'$\frac{3}{4}$','varie','s',ha='right')
box(ax,56,26,30,14,'resultat')
text(ax,71,35,'une seule orbite','resultat','s')
text(ax,71,30,r'$\{A,B,C,D\}$','resultat','s')
arrow(ax,(cx+s+5,cy),(55,33),'fixe')
save(fig,'47-034')
