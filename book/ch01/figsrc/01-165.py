import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
X = lambda v: 10 + 6 * (v - 2)
ys = (84, 62, 38)
fs = [numberline(ax, 10, 82, y, 2, 14, labels=False, arrow_right=False) for y in ys]
text(ax, 10, 79.5, '2', 'fixe', 's')
text(ax, 10, 92, '1. supposer des cas faux', 'encre', 's', ha='left')
for v in (8, 11, 13):
    disc(ax, X(v), 84, 1.5, 'limite', fill=False); ax.patches[-1].set_zorder(4)
text(ax, 10, 70, '2. prendre le plus petit', 'encre', 's', ha='left')
for v in (11, 13):
    disc(ax, X(v), 62, 1.5, 'fixe', fill=False); ax.patches[-1].set_zorder(4)
disc(ax, X(8), 62, 1.8, 'limite'); ax.patches[-1].set_zorder(4)
text(ax, X(8), 56, 'le plus petit', 'limite', 's')
text(ax, 10, 48, "3. il n'est pas faux", 'encre', 's', ha='left')
for v, lab in ((4, 'a'), (5, 'b')):
    disc(ax, X(v), 38, 1.4, 'resultat'); ax.patches[-1].set_zorder(4)
    text(ax, X(v), 33, lab, 'resultat', 's')
disc(ax, X(8), 38, 1.8, 'resultat'); ax.patches[-1].set_zorder(4)
disc(ax, X(8), 38, 2.8, 'limite', fill=False); ax.patches[-1].set_zorder(4)
for v in (4, 5):
    arrow(ax, (X(v), 40), (X(8), 40), 'varie', curve=-0.4)
text(ax, 64, 44, 'a et b : plus petits, vrais', 'resultat', 's')
text(ax, 62, 31, 'ou insécable : vrai aussi', 'fixe', 's')
text(ax, 10, 18, '4. contradiction : arrêt', 'limite', 's', ha='left')
text(ax, 44, 7, "aucun cas faux n'existe", 'resultat', 'm')
save(fig, '01-165')
