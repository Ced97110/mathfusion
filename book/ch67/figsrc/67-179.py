import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 64, 70, 'nombre d’éléments', 'fixe', 's')
levels = [(54, 4, 16, 'autre', r'$\mathbb{F}_{16}$'),
          (32, 2, 4, 'sujet', r'$\mathbb{F}_4$'),
          (10, 1, 2, 'fixe', r'$\mathbb{F}_2$')]
for y, d, n, role, lab in levels:
    box(ax, 24, y, 22, 10, role, label=lab)
    text(ax, 3, y + 5, f'diviseur {d}', role, 's', ha='left')
    for j in range(n):
        row, col = divmod(j, 8) if n > 8 else (0, j)
        yy = y + 5 + (1.7 if n > 8 else 0) - (3.4 if (n > 8 and row == 1) else 0)
        disc(ax, 54 + col * 3.0, yy, 1.1, role)
line(ax, [(35, 20), (35, 32)], 'fixe')
line(ax, [(35, 42), (35, 54)], 'fixe')
save(fig, '67-179')
