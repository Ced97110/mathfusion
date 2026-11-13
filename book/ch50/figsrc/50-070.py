import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'$n_p = [G:N(P)] = |G|\ /\ |N(P)|$', 'sujet', 'm', weight='bold')
cx = [14, 36, 58, 78]
heads = ['1 choisir\n$P$', '2 chercher\n$N(P)$', '3 compter\nses éléments', '4 diviser\n$|G|$']
for x, h in zip(cx, heads):
    text(ax, x, 62, h, 'varie', 's')
for i in range(3):
    arrow(ax, (cx[i] + 8, 62), (cx[i + 1] - 8.5, 62), 'varie', lw=0.9)
def dots(x, y, n, role, per_row=3):
    for k in range(n):
        disc(ax, x - (min(n, per_row) - 1) * 2.2 + (k % per_row) * 4.4, y - (k // per_row) * 4.4, 1.5, role)
rows = [(40, 'p = 2', 2, 2, '$6\\ /\\ 2 = 3$'), (12, 'p = 3', 3, 6, '$6\\ /\\ 6 = 1$')]
for y, lab, nP, nN, res in rows:
    text(ax, 3, y + 8, '$' + lab + '$', 'encre', 's', ha='left', weight='bold')
    dots(cx[0], y + 2, nP, 'sujet')
    dots(cx[1], y + 2, nN, 'autre' if nN == 2 else 'autre')
    text(ax, cx[2], y + 2, str(nN), 'autre', 'l', weight='bold')
    text(ax, cx[3] - 2, y + 2, res, 'resultat', 'm', weight='bold')
    line(ax, [(2, y - 8), (86, y - 8)], 'fixe', lw=0.5)
save(fig, '50-070')
