import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(52)
x0, k = 38, 80
rows = [(34, 'tan 10°', 0.1763, 'sujet', False), (22, '2 × 0,1763 (faux)', 0.3526, 'limite', True), (10, 'tan 20° (table)', 0.3640, 'resultat', False)]
for y, lab, v, role, dash in rows:
    text(ax, x0 - 2, y + 3, lab, role, 's', ha='right')
    box(ax, x0, y, v * k, 6, role, fill=not dash, dash=dash, r=0.6)
    text(ax, x0 + v * k + 2.5, y + 3, f'{v:.4f}'.replace('.', ','), role, 's', ha='left')
text(ax, 56, 17, '≠', 'limite', 'l', weight='bold')
text(ax, 44, 46, r'$\tan A\ \neq\ \tan \times A$', 'encre', 'l')
save(fig, '25-074')
