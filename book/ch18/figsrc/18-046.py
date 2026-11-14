import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(72)
u = 3.2
def rect(x, y, w, h, role, fill=True, dash=False):
    poly(ax, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], role, fill=fill)
    if dash: ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc='none', lw=0.8, ls='--', zorder=3))
x0, y0 = 4, 26
rect(x0, y0, 5 * u, 2 * u, 'sujet'); rect(x0, y0 + 2 * u, 2 * u, 3 * u, 'varie')
rect(x0 + 2 * u, y0 + 2 * u, 3 * u, 3 * u, 'limite', fill=False, dash=True)
text(ax, x0 + 3.5 * u, y0 + 3.5 * u, r'$b^2=9$', 'limite', 's')
x1 = 46
rect(x1, y0, 5 * u, 2 * u, 'sujet'); rect(x1 + 5 * u, y0, 3 * u, 2 * u, 'varie')
arrow(ax, (x0 + 5 * u + 3, y0 + 3), (x1 - 3, y0 + 3), 'varie')
text(ax, 20, 53, r'$a^2-b^2$', 'sujet', 'm'); text(ax, 58, 53, r'$(a+b)(a-b)$', 'sujet', 'm')
text(ax, x0 + 2.5 * u, y0 - 4, r'$25-9=16$', 'resultat', 's'); text(ax, x1 + 4 * u, y0 - 4, r'$8\times2=16$', 'resultat', 's')
text(ax, x1 + 8 * u + 1.5, y0 + u, r'$a-b=2$', 'varie', 's', ha='left')
brace(ax, x1, x1 + 8 * u, y0 + 2 * u + 1, 'fixe', r'$a+b=8$', down=False)
text(ax, 44, 8, r'$10$ et $1$ : $100-1=11\times9=99$', 'fixe', 's')
save(fig, '18-046')
