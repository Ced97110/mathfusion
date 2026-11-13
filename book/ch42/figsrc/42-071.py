import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(64)
rows = [(48, 'autre', False, 'seul $p$ vrai'), (28, 'autre', True, 'les deux vrais'), (8, 'sujet', True, r'si $p$, alors $q$')]
for y, role, has_q, lab in rows:
    box(ax, 2, y, 30, 10, role, 'multiple de 4', 's')
    if has_q:
        box(ax, 42, y, 16, 10, role, 'pair', 's')
        if role == 'sujet': arrow(ax, (33, y + 5), (41, y + 5), 'sujet')
        else: text(ax, 37, y + 5, 'et', 'autre', 's')
    text(ax, 61, y + 5, lab, role, 's', ha='left')
save(fig, '42-071')
