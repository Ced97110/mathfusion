import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def dalle(y, n, role, lab):
    w = 60 / n
    for i in range(n): box(ax, 14 + i * w, y, w, 9, role if i == 0 else 'fixe', r=0.4)
    text(ax, 2, y + 4.5, lab, role, 's', ha='left')
text(ax, 44, 68, 'une dalle, une heure de travail', 'encre', 's')
dalle(48, 6, 'sujet', ''); text(ax, 80, 52.5, r'$\frac{1}{6}$', 'sujet', 'm')
dalle(30, 4, 'autre', ''); text(ax, 80, 34.5, r'$\frac{1}{4}$', 'autre', 'm')
text(ax, 7, 52.5, '1', 'sujet', 's'); text(ax, 7, 34.5, '2', 'autre', 's')
box(ax, 14, 8, 10, 9, 'sujet'); box(ax, 24, 8, 15, 9, 'autre'); box(ax, 14, 8, 60, 9, 'fixe', fill=False)
text(ax, 7, 12.5, '1 + 2', 'varie', 's')
brace(ax, 14, 39, 20, 'varie', down=False, label=r'$\frac{1}{6}+\frac{1}{4}$', size='m', depth=1.4)
save(fig, '21-007')
