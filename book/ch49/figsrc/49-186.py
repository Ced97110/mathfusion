import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0, x1 = 8, 80; f = lambda v: x0 + v / 8 * (x1 - x0); y = 42
for a, b, role, lab in [(0, 2, 'resultat', r'$|C|$ = 2'), (2, 4, 'varie', '2'), (4, 6, 'varie', '2'), (6, 8, 'varie', '2')]:
    box(ax, f(a), y - 5, f(b) - f(a), 10, role, label=lab, size='m')
text(ax, f(4), y + 9, r'$|G|$ = 8 = 2 fois 2 fois 2', 'sujet', 'm')
numberline(ax, x0, x1, 22, 0, 8, step=2, arrow_right=False, size='m')
for v in (0, 2, 4, 6, 8): line(ax, [(f(v), y - 5), (f(v), 22)], 'fixe', lw=0.4, dash=True)
text(ax, f(0) + 0, 12, 'multiples de 2', 'fixe', 's', ha='left')
brace(ax, f(2), f(8), 9, 'varie', None, depth=2)
text(ax, f(5), 3, 'somme = 6, multiple de 2', 'varie', 's')
save(fig, '49-186')
