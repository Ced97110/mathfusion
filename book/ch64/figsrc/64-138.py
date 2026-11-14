import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
bh = 8
# colonne de gauche : S4, 24 -> 12 -> 4 -> 2 -> 1
lx, lw_ = 4, 28
sizes = [r'$S_4$ : 24', '12', '4', '2', '1']
ys = [62 - 12 * k for k in range(5)]
text(ax, lx + lw_ / 2, 77, r'$n=4$ : résoluble', 'resultat', 'm')
for k, (s, y) in enumerate(zip(sizes, ys)):
    box(ax, lx, y, lw_, bh, 'resultat', label=s)
    if k < 4:
        arrow(ax, (lx + lw_ / 2, y - 0.3), (lx + lw_ / 2, ys[k + 1] + bh + 0.3), 'resultat')
# colonne de droite : S5, 120 -> 60, puis rien
rx, rw = 56, 28
text(ax, rx + rw / 2, 77, r'$n=5$ : pas résoluble', 'limite', 'm')
box(ax, rx, ys[0], rw, bh, 'sujet', label=r'$S_5$ : 120')
box(ax, rx, ys[2], rw, bh, 'limite', label=r'$A_5$ : 60')
box(ax, rx, ys[4], rw, bh, 'fixe', fill=False, dash=True, label='1')
arrow(ax, (rx + rw / 2, ys[0] - 0.3), (rx + rw / 2, ys[2] + bh + 0.3), 'sujet')
line(ax, [(rx + rw / 2, ys[2] - 0.3), (rx + rw / 2, ys[4] + bh + 0.3)], 'limite', dash=True)
text(ax, rx + rw / 2, (ys[2] + ys[4] + bh) / 2, r'$\times$', 'limite', 'xl')
text(ax, rx + rw / 2 - 3, (ys[2] + ys[4] + bh) / 2, 'aucun pas', 'limite', 's', ha='right')
save(fig, '64-138')
