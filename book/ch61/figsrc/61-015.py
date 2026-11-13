import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
u=10; cx,cy=24,33
line(ax,[(2,cy),(46,cy)],'fixe',lw=0.5); line(ax,[(cx,6),(cx,60)],'fixe',lw=0.5)
disc(ax,cx,cy,2*u,'sujet',fill=False,lw=1.2)
line(ax,[(cx-2.2*u,cy-1.2*u),(cx+1.6*u,cy+2.6*u)],'varie',lw=1.2)
s7=math.sqrt(7)
for x in ((-1+s7)/2,(-1-s7)/2):
    disc(ax,cx+x*u,cy+(x+1)*u,1.1,'resultat')
text(ax,24,9,'cercle','sujet','s'); text(ax,44,60,'droite','varie','s')
text(ax,38,47,'point P','resultat','s')
x0,w_=52,34
text(ax,69,61,'permis','resultat','s')
box(ax,x0,44,w_,14,'resultat',label='+  −  ×  ÷')
box(ax,x0,26,w_,14,'resultat',label='racine carrée\n$\\sqrt{28}$',size='s')
text(ax,69,23,'jamais','limite','s')
box(ax,x0,6,w_,14,'limite',label='racine cubique\n$\\sqrt[3]{2}$',size='s')
line(ax,[(x0+3,8),(x0+w_-3,18)],'limite',lw=1.4)
save(fig,'61-015')
