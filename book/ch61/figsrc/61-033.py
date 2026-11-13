import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,6,52,34,10,'sujet',label='$E$ (haut)')
box(ax,6,30,34,10,'fixe',label='$K$ (milieu)')
box(ax,6,8,34,10,'fixe',label='$F$ (fractions)')
arrow(ax,(23,18),(23,30),'varie'); text(ax,28,24,'2','varie','l')
arrow(ax,(23,40),(23,52),'varie'); text(ax,28,46,'2','varie','l')
line(ax,[(40,13),(46,13)],'fixe',dash=True); line(ax,[(40,57),(46,57)],'fixe',dash=True)
arrow(ax,(46,13),(46,57),'resultat'); text(ax,51,35,'4','resultat','l')
for i in range(2):
    for j in range(2): disc(ax,63+i*10,32+j*10,3.5,'resultat')
text(ax,68,24,'4 briques','resultat','s')
text(ax,44,68,'4 = 2 × 2','sujet','l')
save(fig,'61-033')
