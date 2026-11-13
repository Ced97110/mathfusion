import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'chaque pair se range en tas de 2', 'encre', 's')
sp, r, x0 = 6.0, 2.2, 14.0
rows = [2, 4, 6, 8, 10]
for k, n in enumerate(rows):
    y = 48 - k * 9.6
    text(ax, 5, y, str(n), 'sujet', 'l', ha='center')
    for p in range(n // 2):
        role = 'resultat' if n == 2 else 'varie'
        cx = x0 + p * 2 * sp
        box(ax, cx - 3.4, y - 3.6, 2 * sp - 0.6, 7.2, role, fill=True, r=1.0)
        for j in range(2):
            disc(ax, cx + j * sp, y, r, 'sujet')
    if n == 2:
        text(ax, 80, y, 'rien en trop', 'resultat', 's')
    else:
        text(ax, 80, y, '2 en trop', 'varie', 's')
text(ax, 44, 1.8, r'le tas de 2 est $\neq$ 1 et $\neq$ au nombre', 'encre', 's')
save(fig, '05-050')
