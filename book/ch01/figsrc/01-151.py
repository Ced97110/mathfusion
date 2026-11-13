import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
full = [5, 7, 12, 40]
data = {58: [5, 7, 12, 40], 44: [7, 12, 40], 30: [40]}
for y, pts in data.items():
    f = numberline(ax, 6, 82, y, 0, 42, step=1, labels=(y == 30), every=10, arrow_right=False)
    for v in full:
        if v in pts: disc(ax, f(v), y, 1.2, 'sujet')
        else: ax.add_patch(Circle((f(v), y), 1.2, ec=COL['fixe'], fc='white', lw=0.6, ls='--', zorder=2.5))
    m = min(pts)
    disc(ax, f(m), y, 2.2, 'resultat', fill=False)
    text(ax, f(m), y + 3.5, str(m), 'resultat', 'm')
text(ax, 44, 68, 'toute collection non vide a un plus petit', 'resultat', 's')
box(ax, 40, 6, 44, 8, 'fixe', label="conséquence de l'axiome 3", size='s')
arrow(ax, (f(40), 14), (f(40), 24.5), 'fixe')
save(fig, '01-151')
