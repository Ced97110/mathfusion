import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'quelles U vérifient UA = AU ?', 'encre', 'm')
def grid(x0, free_all):
    ytop, cw, ch = 54, 13, 11
    ent = [['a', 'b'], ['c', 'd']]
    for r in range(2):
        for c in range(2):
            free = free_all or r == c
            box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, 'varie' if free else 'fixe',
                label=ent[r][c] if free else '0', size='m')
    for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 2 * cw + 1.5)):
        line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 2 * ch - 0.5), (xx - sgn * 1.5, ytop - 2 * ch - 0.5)], 'encre', lw=0.9)
text(ax, 21, 61, 'A = 2·I', 'sujet', 'm', weight='bold')
text(ax, 65, 61, 'A = diag(2, 3)', 'autre', 'm', weight='bold')
grid(8, True); grid(52, False)
text(ax, 21, 26, '4 cases libres', 'varie', 's')
text(ax, 65, 26, '2 cases libres', 'varie', 's')
text(ax, 44, 12, 'A plus variée → moins de U', 'encre', 's')
save(fig, '60-191')
