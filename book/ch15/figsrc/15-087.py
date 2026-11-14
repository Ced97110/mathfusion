import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r"$a = 1$ : l'opposé de 10 vaut $-10$", 'encre', 'm')
text(ax, 2, 52, 'tous les signes changent', 'resultat', 's', ha='left')
text(ax, 2, 30, 'dernier signe oublié', 'limite', 's', ha='left')
for y, last, role, val in ((36, r'$+18$', 'resultat', r'$= -10$'), (14, r'$-18$', 'limite', r'$= -46$')):
    for i, t in enumerate((r'$-21a^2$', r'$-7a$')):
        box(ax, 2 + i * 22, y, 20, 12, 'resultat' if y == 36 else 'fixe', label=t)
    box(ax, 46, y, 20, 12, role, label=last)
    text(ax, 77, y + 6, val, role, 'm')
save(fig, '15-087')
