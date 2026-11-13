import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
X0, CW, CH, Y = 8.0, 6.0, 7.0, 54.0
groups = [(1, 'fixe', 'ordre 1'), (3, 'sujet', 'ordre 2'), (8, 'autre', 'ordre 3')]
text(ax, 44, 79, r'$A_4$ : 12 éléments', 'encre', 'm')
i = 0
for n, role, lab in groups:
    for _ in range(n):
        box(ax, X0 + i * CW, Y, CW - 0.6, CH, role, r=0.4, lw=0.7); i += 1
    x0 = X0 + (i - n) * CW; x1 = X0 + i * CW - 0.6
    brace(ax, x0, x1, Y + CH + 0.5, role, label=str(n), down=False, size='s')
    brace(ax, x0, x1, Y - 0.5, role, label=lab, down=True, size='s')
assert i == 12
box(ax, 8, 28, 72, 8, 'resultat', label="2 premier : ordre 2 présent", size='s')
box(ax, 8, 18, 72, 8, 'resultat', label="3 premier : ordre 3 présent", size='s')
box(ax, 8, 8, 72, 8, 'limite', label="4 non premier : sans ordre 4", size='s')
save(fig, '50-053')
