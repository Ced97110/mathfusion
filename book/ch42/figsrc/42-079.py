import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(80)
text(ax, 2, 76, 'implication', 'fixe', 's', ha='left')
box(ax, 2, 62, 60, 12, 'resultat', r'multiple de 4 $\Rightarrow$ pair', 'm'); text(ax, 75, 68, 'vrai', 'resultat', 'l')
text(ax, 2, 55, 'réciproque', 'fixe', 's', ha='left')
box(ax, 2, 40, 60, 12, 'limite', r'pair $\Rightarrow$ multiple de 4', 'm'); text(ax, 75, 46, 'faux', 'limite', 'l')
arrow(ax, (32, 40), (32, 17), 'limite')
box(ax, 2, 5, 60, 12, 'fixe', r'$6=4\times 1+2$ : reste 2', 'm'); text(ax, 75, 11, 'contre-exemple', 'limite', 's')
save(fig, '42-079')
