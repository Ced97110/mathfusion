import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
text(ax,24,86,'preuve','sujet','s'); text(ax,66,86,'avec 4 et 7','autre','s')
rows=[('1. départ','sujet',r"$\eta(h)\,x'$",'h = 4, x’ = 7'),
      ('2. clé : η surjective','varie',r"$x'=\eta(x)$",'x = 7'),
      ('3. arrivée','resultat',r"$\eta(hx)\in\eta(I)$",'4 × 7 = 28, reste 4')]
for i,(cap,role,sym,num) in enumerate(rows):
    y=58-i*28
    text(ax,12,y+15.5,cap,role,'s',ha='left',weight='bold' if i==1 else 'normal')
    lw=1.8 if i==1 else 0.8
    box(ax,3,y,40,12,role,label=sym,size='m',lw=lw); box(ax,47,y,38,12,role,label=num,size='s',lw=lw)
    if i<2:
        arrow(ax,(8,y),(8,y-15.5),'fixe'); arrow(ax,(66,y),(66,y-15.5),'fixe')
save(fig,'52-166')
