import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(44)
f = numberline(ax, 20, 80, 10, 0, 360, 90, arrow_right=False)
text(ax, 50, 2.5, 'angle en degrés', 'fixe', 's')
for y, role, nm in ((34, 'sujet', 'gauche'), (22, 'autre', 'droite')):
    text(ax, 2, y, nm, role, 's', ha='left'); line(ax, [(20, y), (80, y)], role)
disc(ax, f(90), 34, 1.6, 'limite'); disc(ax, f(90), 22, 1.6, 'limite'); disc(ax, f(270), 22, 1.6, 'limite')
disc(ax, f(270), 34, 1.6, 'resultat'); text(ax, f(270), 39, 'vaut 0', 'resultat', 's')
text(ax, f(90), 39, 'sans sens', 'limite', 's'); text(ax, f(270), 27, 'sans sens', 'limite', 's')
save(fig, '31-131')
