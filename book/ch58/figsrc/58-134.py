import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
n = lambda v: str(v).replace('-', '−')
# coefficients des degrés 0 à 4
p = [1, 0, 3, 0, -1]
q = [2, 0, -1, 0, 0]
s = [x + y for x, y in zip(p, q)]
assert s == [3, 0, 2, 0, -1]
x0, dx, w = 22, 14, 12
# bandes des degrés impairs (1 et 3), derrière les trois lignes
for d in (1, 3):
    ax.add_patch(Rectangle((x0 + d * dx - w / 2 - 1, 8), w + 2, 52, fc=FILL['varie'], ec='none', zorder=1))
text(ax, 44, 65, 'coefficient de chaque degré', 'fixe', 's')
for d in range(5):
    role = 'varie' if d % 2 == 1 else 'fixe'
    text(ax, x0 + d * dx, 54, rf'$x^{d}$' if d > 1 else ('1' if d == 0 else r'$x$'), role, 'm', weight='bold' if d % 2 else 'normal')
rows = [('p', p, 'sujet', 38), ('q', q, 'autre', 26), (r'$p+q$', s, 'resultat', 10)]
for lab, c, role, y in rows:
    text(ax, 6, y + 5, lab, role, 'm')
    for d, v in enumerate(c):
        if d % 2 == 1:
            box(ax, x0 + d * dx - w / 2, y, w, 10, 'varie', label=n(v), weight='bold')
        else:
            box(ax, x0 + d * dx - w / 2, y, w, 10, role, label=n(v))
line(ax, [(2, 22.5), (86, 22.5)], 'encre', lw=0.8)
text(ax, 44, 3.5, 'degrés impairs : 0 dans p, q et p + q', 'varie', 's', weight='bold')
save(fig, '58-134')
