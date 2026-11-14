import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(56)
text(ax, 22, 51, 'côté gauche', 'sujet', 's'); text(ax, 66, 51, 'côté droit', 'autre', 's')
lbox(ax, 4, 30, 36, 16, 'sujet', r'$\frac{2-1{,}1547}{2+1{,}1547}$', size='l')
lbox(ax, 48, 30, 36, 16, 'autre', r'$\frac{1{,}7321-1}{1{,}7321+1}$', size='l')
arrow(ax, (22, 29), (38, 19), 'sujet'); arrow(ax, (66, 29), (50, 19), 'autre')
lbox(ax, 26, 5, 36, 13, 'resultat', r'$\approx 0{,}2679$', size='l'); text(ax, 44, 23.5, 'même nombre', 'resultat', 's')
save(fig, '31-136')
