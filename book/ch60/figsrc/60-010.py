import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
w, h = 5.6, 7
def bar(x, y, n, role):
    for k in range(n):
        box(ax, x + k * w + 0.3, y, w - 0.6, h, role, r=0.5)
    return x + n * w
text(ax, 10, 52, 'ℤ/12 : 1 morceau', 'sujet', 'm', ha='left')
bar(10, 38, 12, 'sujet'); text(ax, 10 + 6 * w, 33, '12 positions', 'sujet', 's')
text(ax, 10, 25, 'ℤ/4 ⊕ ℤ/3 : 2 morceaux', 'encre', 'm', ha='left')
e = bar(10, 11, 4, 'sujet'); text(ax, 10 + 2 * w, 6, '4', 'sujet', 's')
text(ax, e + 4, 11 + h / 2, '⊕', 'varie', 'l')
e2 = bar(e + 8, 11, 3, 'autre'); text(ax, e + 8 + 1.5 * w, 6, '3', 'autre', 's')
text(ax, 77, 26, 'même\ngroupe ?', 'varie', 's')
save(fig, '60-010')
