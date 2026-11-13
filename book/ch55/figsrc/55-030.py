import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 34, 58, 20, 11, 'sujet', label=r'$F$', size='xl')
text(ax, 60, 63.5, 'un corps quelconque', 'sujet', 'm', ha='left')
xs = [2, 31, 60]
for k, x in enumerate(xs):
    role = 'sujet' if k < 2 else 'autre'
    box(ax, x, 6, 26, 36, role)
    arrow(ax, (44, 57), (x + 13, 43.5), 'fixe')
c = [x + 13 for x in xs]
text(ax, c[0], 36, 'ℚ', 'sujet', 'xl'); text(ax, c[0], 30, 'fractions', 'sujet', 's')
for i in range(15):
    ax.add_patch(Circle((5 + i * 1.5, 22), 0.45, ec=COL['sujet'], fc=COL['sujet'], zorder=3))
text(ax, c[0], 11, 'infini', 'sujet', 's')
text(ax, c[1], 36, 'ℝ', 'sujet', 'xl'); text(ax, c[1], 30, 'droite graduée', 'sujet', 's')
line(ax, [(34, 22), (54, 22)], 'sujet', lw=2.2)
text(ax, c[1], 11, 'infini', 'sujet', 's')
text(ax, c[2], 36, 'ℤ/pℤ', 'autre', 'xl'); text(ax, c[2], 30, 'restes mod p', 'autre', 's')
for i in range(6):
    a = math.radians(90 - 60 * i)
    ax.add_patch(Circle((c[2] + 6 * math.cos(a), 21.5 + 6 * math.sin(a)), 0.9, ec=COL['autre'], fc=COL['autre'], zorder=3))
text(ax, c[2], 11, 'fini : p éléments', 'autre', 's')
save(fig, '55-030')
