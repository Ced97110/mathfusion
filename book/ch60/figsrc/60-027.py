import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def tree(cx, role, kids, widths, note, res):
    box(ax, cx - 8, 50, 16, 10, 'sujet', label='12', size='l')
    xs = [cx - 11, cx + 11]
    for x, k, w in zip(xs, kids, widths):
        box(ax, x - w / 2, 26, w, 10, role, label=k, size='m')
        arrow(ax, (cx + (-4 if x < cx else 4), 50), (x, 36.5), 'fixe')
    text(ax, cx, 31, '×', role, 'l')
    text(ax, cx, 20, note, role, 's')
    text(ax, cx, 8, res, role, 'm', weight='bold')
tree(22, 'resultat', ['4 = 2²', '3'], [18, 12], 'sans facteur commun', 'ℤ/12 ≅ ℤ/2² ⊕ ℤ/3')
tree(66, 'limite', ['2', '6'], [12, 12], 'facteur commun 2', 'ℤ/12 ≠ ℤ/2 ⊕ ℤ/6')
save(fig, '60-027')
