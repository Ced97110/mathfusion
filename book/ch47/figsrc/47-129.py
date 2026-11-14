import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$g$ = un retournement', 'encre', 'l')
x0, cw, gap = 7.0, 8.5, 0.8
def xs(i): return x0 + i * (cw + gap)
for row, (y, role, lab) in enumerate([(36, 'sujet', r'$gN$'), (14, 'autre', r'$Ng$')]):
    text(ax, x0, y + 12.5, lab, role, 'l', ha='left')
    for i in range(8):
        r = role if i >= 4 else 'fixe'
        box(ax, xs(i), y, cw, 8, r)
for i in range(4, 8):
    arrow(ax, (xs(i) + cw / 2, 36), (xs(i) + cw / 2, 22), 'resultat', lw=0.8, both=True)
text(ax, 44, 29, '=', 'resultat', 'l', weight='bold')
brace(ax, xs(0), xs(3) + cw, 12, 'fixe', 'rotations N')
brace(ax, xs(4), xs(7) + cw, 12, 'fixe', 'retournements')
text(ax, 44, 3.5, 'mêmes éléments des deux côtés', 'resultat', 's')
save(fig, '47-129')
