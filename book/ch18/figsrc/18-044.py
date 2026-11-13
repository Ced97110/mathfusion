import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(80)
def row(y, n, lab, lone=False, brace_label=None):
    text(ax, 3, y + 12, lab, 'fixe', 's', ha='left')
    ng = n // 2; x = 3
    for g in range(ng):
        box(ax, x, y - 1, 17, 10, 'resultat', fill=False, dash=True)
        box(ax, x + 1, y, 7.5, 8, 'sujet', r=0.3); box(ax, x + 9, y, 7.5, 8, 'sujet', r=0.3); x += 20
    if lone: box(ax, x, y, 7.5, 8, 'limite', r=0.3, label='seul', size='s')
    if brace_label: brace(ax, 3, 3 + 20 * ng - 3, y - 1, 'fixe', brace_label)
row(58, 4, '4 termes : 2 groupes de 2', brace_label='aucun facteur commun à tous'); row(35, 6, '6 termes : 3 groupes de 2')
row(12, 2, '3 termes : un terme reste seul', lone=True)
save(fig, '18-044')
