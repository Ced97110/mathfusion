import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$f=4x^2+6x+10$', 'fixe', 'm')
u = 5.0   # une unité = 5 mm ; un bloc = 2 unités
rows = [(46, 4, 2), (30, 6, 3), (14, 10, 5)]
for y, val, n in rows:
    text(ax, 14, y + 4, f'{val}', 'fixe', 'm', ha='right')
    for k in range(n):
        box(ax, 18 + k * 2 * u, y, 2 * u - 1, 8, 'sujet', r=0.5, label='2' if k == 0 else None)
brace(ax, 18, 18 + 2 * u - 1, 56, role='sujet', down=False, depth=1.4)
text(ax, 18 + u - 0.5, 61 - 3.5, '', 'sujet', 's')
text(ax, 18 + 2 * u + 10, 57.5, r'$c(f)=2$ : bloc commun', 'sujet', 's', ha='left')
text(ax, 44, 4, r'$4=2\times2$, $6=2\times3$, $10=2\times5$', 'encre', 's')
save(fig, '56-141')
