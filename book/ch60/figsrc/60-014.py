import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def tree(cx, role, head, top, kids):
    text(ax, cx, 60, head, role, 'm', weight='bold')
    box(ax, cx - 12, 44, 24, 10, role, label=top, size='l')
    wk = 18
    for s, k in zip((-1, 1), kids):
        bx = cx + s * 11
        box(ax, bx - wk / 2, 14, wk, 10, role, label=k, size='m')
        arrow(ax, (cx + s * 6, 44), (bx, 24.5), role)
    text(ax, cx, 19, '×', role, 'l')
tree(22, 'sujet', 'dans ℤ', '12', ['4', '3'])
tree(66, 'autre', 'dans F[λ]', 'λ² − 1', ['λ − 1', 'λ + 1'])
text(ax, 44, 5, 'même découpage en facteurs', 'encre', 's')
save(fig, '60-014')
