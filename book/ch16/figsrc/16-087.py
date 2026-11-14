import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
def balance(yb,show):
    line(ax,[(14,yb),(74,yb)],'fixe',lw=1.4); poly(ax,[(44,yb),(40,yb-9),(48,yb-9)],'fixe')
    for cx in (24,64):
        line(ax,[(cx-10,yb-1),(cx+10,yb-1)],'fixe',lw=1.1)
        for dx in (-5,5):
            if show: box(ax,cx+dx-4,yb+0.5,8,8,'sujet',label='$x$')
            else: box(ax,cx+dx-4,yb+0.5,8,8,'fixe',fill=False,dash=True)
balance(60,True)
for cx in (24,64): brace(ax,cx-9,cx+9,70,'sujet',label='$2x$',down=False)
arrow(ax,(44,47),(44,37),'varie'); text(ax,49,42,r'retirer $2x$ des deux côtés','varie','s',ha='left')
balance(24,False)
for cx in (24,64): text(ax,cx,17,'reste : rien','fixe','s')
text(ax,44,6,'toujours en équilibre','resultat','m')
text(ax,44,80,'$2x$ est un nombre','sujet','m')
save(fig,'16-087')
