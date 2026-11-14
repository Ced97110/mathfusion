import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# deux sacs types : e1 = (1, 0) riz seul, e2 = (0, 1) lentilles seules
def sac(x, title, role, riz, len_):
    box(ax, x, 8, 40, 36, role, lw=1.0)
    text(ax, x + 20, 51, title, role, 'l', weight='bold')
    for y, name, q, r in [(34, 'riz', riz, 'sujet'), (17, 'lentilles', len_, 'autre')]:
        text(ax, x + 3, y + 3, f'{name} : {q} kg', r, 's', ha='left')
        if q:
            box(ax, x + 29, y - 0.5, 7, 7, r, r=0.5)
        else:
            box(ax, x + 29, y - 0.5, 7, 7, 'fixe', fill=False, dash=True, r=0.5)
sac(2, r'$e_1 = (1,\ 0)$', 'sujet', 1, 0)
sac(46, r'$e_2 = (0,\ 1)$', 'autre', 0, 1)
save(fig, '58-007')
