import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
def sac(x, y, objs, role, title=None, cap=None, ghost=False):
    box(ax, x, y, 36, 18, role, dash=ghost)
    for k, o in enumerate('abc'):
        if o in objs: disc(ax, x + 8 + k * 10, y + 9, 3.6, role, label=f'${o}$')
        else: disc(ax, x + 8 + k * 10, y + 9, 3.6, 'fixe', fill=False)
    if title: text(ax, x + 18, y + 22.5, title, role, 's', weight='bold')
    if cap: text(ax, x + 18, y - 3.5, cap, role, 's')
sac(2, 36, 'abc', 'sujet', 'ensemble de départ', r'$\{a,b,c\}$')
sac(50, 36, 'abc', 'resultat', 'sac plein', r'$\{a,b,c\}$')
text(ax, 44, 45, '=', 'varie', 'xl', weight='bold')
sac(26, 8, 'ab', 'fixe', None, '2 objets sur 3')
save(fig, '42-013')
