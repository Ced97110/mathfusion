import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy = 8, 46
X = lambda x: ox + 14 * x
line(ax, [(ox - 2, oy), (X(3.6), oy)], 'fixe', lw=0.7)
line(ax, [(X(t / 20), oy + 2.0 * (3 * (t / 20) ** 2 - 10 * (t / 20) + 11)) for t in range(0, 65)], 'sujet', lw=1.4)
text(ax, X(0.35), oy + 20, r'$k$', 'sujet', 'm')
box(ax, 58, 52, 28, 9, 'sujet', label=r'$100-132=-32$', size='s')
box(ax, 58, 38, 28, 11, 'resultat', label='$k$ : aucune\nracine réelle', size='s')
arrow(ax, (72, 52), (72, 49), 'varie', lw=0.9)
f = numberline(ax, ox, ox + 56, 22, 0, 4, 1, arrow_right=False)
for v in (1, 2, 3):
    disc(ax, f(v), 22, 1.4, 'resultat')
text(ax, 72, 22, 'Sturm\ncompte 3', 'varie', 's')
text(ax, 8, 8, r'racines de $h$ : $1$, $2$, $3$', 'resultat', 's', ha='left')
text(ax, 48, 8, r'plus proche : $P=(1,\ 0)$', 'sujet', 's', ha='left')
save(fig, '70-143')
