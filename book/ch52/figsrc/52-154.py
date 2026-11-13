import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 86, r'$\eta$ injective ⇔ ker $\eta$ = {0}', 'sujet', 'm', weight='bold')
cols = [(2, 'resultat', r'ker $\eta$ = {0}', ['même image :\ndifférence 0', 'les deux sont égaux', 'injective']),
        (47, 'autre', r'ker $\eta$ ≠ {0}', ['1 et 5 : même image', r'5 − 1 = 4 ∈ ker $\eta$', '4 ≠ 0 : pas injective'])]
for x, role, head, steps in cols:
    box(ax, x, 62, 39, 12, role, label=head, size='m', weight='bold')
    ys = [44, 26, 8]
    for i, (y, s) in enumerate(zip(ys, steps)):
        last = i == 2
        box(ax, x, y, 39, 12, role if last else 'fixe', label=s, size='s', weight='bold' if last else 'normal')
    arrow(ax, (x + 19.5, 62), (x + 19.5, 56), 'fixe'); arrow(ax, (x + 19.5, 44), (x + 19.5, 38), 'fixe'); arrow(ax, (x + 19.5, 26), (x + 19.5, 20), 'fixe')
save(fig, '52-154')
