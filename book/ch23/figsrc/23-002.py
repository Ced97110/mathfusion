import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 5; x0 = 22; bh = 5.5
text(ax, 2, 55.5 + 2.75 + 0.0, 'largeur', 'encre', 's', ha='left'); text(ax, 2, 48 + 2.75, 'longueur', 'encre', 's', ha='left')
def group(y, wn, wl, tot):
    w = wn * u
    box(ax, x0, y + 7.5, w, bh, 'sujet', True, label=wl, r=0.3)
    box(ax, x0, y, w, bh, 'sujet', True, label=wl, r=0.3)
    box(ax, x0 + w, y, 4 * u, bh, 'fixe', True, label='4', r=0.3)
    text(ax, x0 + w + 4 * u + 2.5, y + bh / 2, tot, 'encre', 'm', ha='left')
group(48, 4, 'x', r'$x+4$')
group(26, 3, '3', '7')
group(4, 5, '5', '9')
save(fig, '23-002')
