import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
x0, x1 = 12, 72
rows = [(70, -1, 1, 'cos 2A  (A = 30°)', 0.5, '0,5'), (46, 0, 2, '1 + cos 2A', 1.5, '1,5'), (22, 0, 1, '(1 + cos 2A) / 2', 0.75, '0,75')]
f = lambda v: x0 + (v + 1) / 3 * (x1 - x0)
ax.add_patch(Rectangle((f(0), 12), f(1) - f(0), 66, fc=FILL['resultat'], ec='none', zorder=0.5))
for y, a, b, name, v, vt in rows:
    numberline(ax, x0, x1, y, -1, 2, step=1, arrow_right=False, labels=(y == 22))
    text(ax, 4, y + 8, name, 'sujet' if y == 22 else 'encre', 's', ha='left')
    line(ax, [(f(a), y), (f(b), y)], 'resultat' if y == 22 else 'fixe', lw=3)
    ax.add_patch(Circle((f(v), y), 1.3, fc=COL['resultat'] if y == 22 else COL['sujet'], ec='none', zorder=4))
    text(ax, f(v), y + 4, vt, 'resultat' if y == 22 else 'sujet', 's')
for y0_, y1_, t in ((66, 52, '+ 1'), (42, 28, '÷ 2')):
    arrow(ax, (82, y0_), (82, y1_), 'varie'); text(ax, 80, (y0_ + y1_) / 2, t, 'varie', 's', ha='right')
text(ax, f(0.5), 4, 'toujours entre 0 et 1', 'resultat', 's')
save(fig, '34-108')
