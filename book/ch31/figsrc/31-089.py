import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
L = 60; x0 = 20
text(ax, 44, 61, r'$\cos^2 x = 1 - \sin^2 x$', 'sujet', 'l')
for y, lab in ((38, '60°'), (18, '120°')):
    text(ax, 10, y + 4, lab, 'encre', 'm', weight='bold')
    box(ax, x0, y, 0.75 * L, 8, 'varie', label=r'$\sin^2$ = 0,75' if y == 38 else None, size='s')
    box(ax, x0 + 0.75 * L, y, 0.25 * L, 8, 'sujet', label=r'$\cos^2$ 0,25' if y == 38 else None, size='s')
text(ax, x0 + 0.75 * L / 2, 22, r'$\sin^2$ = 0,75', 'varie', 's')
text(ax, x0 + 0.875 * L, 22, r'$\cos^2$ 0,25', 'sujet', 's')
brace(ax, x0 + 0.75 * L, x0 + L, 38, 'sujet', label=None, depth=-1.6) if False else None
brace(ax, x0, x0 + L, 50, 'fixe', label='total 1', down=False)
brace(ax, x0 + 0.75 * L, x0 + L, 12, 'resultat', label='1 − 0,75 = 0,25')
save(fig, '31-089')
