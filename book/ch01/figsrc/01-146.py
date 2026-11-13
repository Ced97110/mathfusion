import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 73, r'$10^{n+1} + 3 \times 10^{n} + 5$', 'sujet', 'l')
ok = ['135 = 9 × 15', '1 305 = 9 × 145', '13 005 = 9 × 1 445']
for i, (y, n) in enumerate(zip([56.5, 46.5, 36.5], [1, 2, 3])):
    box(ax, 4, y, 18, 7, 'fixe', label=rf'$n$ = {n}')
    text(ax, 55, y + 3.5, ok[i], 'resultat', 'm')
line(ax, [(4, 34), (84, 34)], 'fixe', dash=True)
for y, lab in zip([24.5, 14.5], [r'$n$ = 4', r'$n$ = 1000']):
    box(ax, 4, y, 18, 7, 'limite', fill=False, dash=True, label=lab)
    text(ax, 55, y + 3.5, '?', 'limite', 'l')
text(ax, 44, 7, 'conjecture : reste à prouver', 'limite', 's')
save(fig, '01-146')
