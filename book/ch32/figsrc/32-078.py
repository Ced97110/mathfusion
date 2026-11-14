import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pp(cx, cy, R, deg): return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
def uc(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.9)
def dot(ax, p, role, r=1.3): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(82)
steps = ['1. isoler le sinus', '2. regarder k', '3. angle principal', '4. second angle', '5. ajouter des tours', '6. garder l’intervalle']
vals = [(r'$\sin(30t)=0{,}5$', 'm'), ('oui : −1 ≤ 0,5 ≤ 1', 's'), ('30°', 'm'), ('150°', 'm'), (r'$+\,360^\circ n$', 'm'), ('0 à 24 heures', 's')]
ys = [3 + (5 - i) * 13 for i in range(6)]
for i, (s, (v, sz)) in enumerate(zip(steps, vals)):
    box(ax, 3, ys[i], 44, 9, 'sujet', label=s)
    box(ax, 52, ys[i], 33, 9, 'resultat', label=v, size=sz)
    arrow(ax, (47.8, ys[i] + 4.5), (51.2, ys[i] + 4.5), 'varie')
    if i < 5: arrow(ax, (25, ys[i] - 0.2), (25, ys[i + 1] + 9.2), 'varie')
save(fig, '32-078')
