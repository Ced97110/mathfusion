import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for cx, ttl in [(24, 'identité'), (64, 'demi-tour')]:
    line(ax, [(cx - 12, 26), (cx + 12, 26)], 'fixe'); line(ax, [(cx, 14), (cx, 38)], 'fixe')
    text(ax, cx, 48, ttl, 'sujet', 'm')
disc(ax, 30, 32, 1.4, 'sujet'); disc(ax, 30, 32, 3.4, 'resultat', fill=False); text(ax, 34, 35, r'$v$', 'sujet', 's'); text(ax, 24, 9, 'même point', 'resultat', 's')
disc(ax, 70, 32, 1.4, 'sujet'); disc(ax, 58, 20, 1.4, 'resultat'); arrow(ax, (69, 31), (59, 21), 'varie')
text(ax, 74, 35, r'$v$', 'sujet', 's'); text(ax, 54, 17, r'$-v$', 'resultat', 's'); text(ax, 64, 9, 'point opposé', 'resultat', 's')
text(ax, 44, 3, r'$C$ : ces deux matrices de $SL_2$', 'encre', 's')
save(fig, '73-125')
