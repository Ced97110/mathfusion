import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(56, 1, 'fixe', r'ordre 1 : $e$'), (40, 3, 'varie', r'ordre 2 : $(1\ 2)(3\ 4)$'), (24, 8, 'sujet', r'ordre 3 : $(1\ 2\ 3)$')]
for y, n, r, lab in rows:
    text(ax, 8, y + 6.5, lab, r, 's', ha='left')
    for i in range(n): disc(ax, 11 + i * 7.5, y, 2.7, r)
text(ax, 44, 8, r'$1 + 3 + 8 = 12$ éléments de $A_4$', 'encre', 'm', weight='bold')
save(fig, '50-151')
