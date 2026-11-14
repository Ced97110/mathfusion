import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, u = 30, 36, 13.5
line(ax, [(cx - 29, cy), (cx + 29, cy)], 'fixe', lw=0.4)
line(ax, [(cx, cy - 14), (cx, cy + 14)], 'fixe', lw=0.4)
arrow(ax, (cx, cy), (cx + 2 * u, cy + 0.8 * u), 'sujet', lw=1.6)
arrow(ax, (cx, cy), (cx - 2 * u, cy - 0.8 * u), 'autre', lw=1.6)
disc(ax, cx, cy, 1.4, 'resultat')
text(ax, 44, 58, '$x^2+1$ agit : $T^2v+v$ = 0', 'resultat', 'm')
text(ax, 50, 51, '$v$ = (2 ; 0,8)', 'sujet', 's')
text(ax, 14, 18, '$T^2v$ = (−2 ; −0,8)', 'autre', 's')
text(ax, 38, 29, '(0 ; 0)', 'resultat', 's')
box(ax, 2, 2, 84, 11, 'resultat', label='1er nombre : −2 + 2 = 0\n2e nombre : −0,8 + 0,8 = 0', size='s')
save(fig, '57-102')
