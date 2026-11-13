import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(62)
box(ax, 4, 46, 24, 12, 'fixe', label='SOH', size='l', weight='bold')
box(ax, 32, 46, 24, 12, 'fixe', label='CAH', size='l', weight='bold')
box(ax, 60, 46, 24, 12, 'sujet', label='TOA', size='l', weight='bold')
for y, lab, role in [(37, 'T = tangente', 'resultat'), (28, 'O = opposé', 'varie'), (19, 'A = adjacent', 'sujet')]:
    text(ax, 62, y, lab, role, 'm', ha='left')
line(ax, [(61, 45), (61, 17)], 'sujet', lw=1.0)
s = 5.0
C = (8, 16); A = (C[0] + 4 * s, C[1]); B = (C[0], C[1] + 3 * s)
poly(ax, [C, A, B], 'fixe')
line(ax, [C, A], 'sujet', lw=2.2); line(ax, [C, B], 'varie', lw=2.2); line(ax, [A, B], 'fixe', lw=1.2)
text(ax, C[0] + 2 * s, C[1] - 3.2, 'A', 'sujet', 'm', weight='bold'); text(ax, C[0] - 3, C[1] + 1.5 * s, 'O', 'varie', 'm', weight='bold')
arc(ax, A, 5, 143.13, 180)
text(ax, 18, 5, r'$\mathrm{T} = \mathrm{O}\,/\,\mathrm{A}$', 'resultat', 'm', weight='bold')
save(fig, '25-075')
