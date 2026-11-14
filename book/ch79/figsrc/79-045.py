import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(100)
w,h=18,8
N={'b':(44,14),'A':(16,44),'B':(72,44),'U':(44,74)}
lab={'b':'{b}','A':'{r, b}','B':'{b, v}','U':'{r, b, v}'}
rl={'b':'resultat','A':'sujet','B':'autre','U':'resultat'}
for lo,up in (('b','A'),('b','B'),('A','U'),('B','U')):
    line(ax,[(N[lo][0],N[lo][1]+h/2),(N[up][0],N[up][1]-h/2)],'fixe',0.9)
for k,(cx,cy) in N.items(): box(ax,cx-w/2,cy-h/2,w,h,rl[k],label=lab[k])
text(ax,72,74,'A ∪ B','resultat','l'); text(ax,72,14,'A ∩ B','resultat','l')
text(ax,16,74,'contient A et B','resultat','s'); text(ax,16,14,'dans A et dans B','resultat','s')
text(ax,44,92,'r : rouge  b : bleu  v : vert','fixe','s')
save(fig,'79-045')
