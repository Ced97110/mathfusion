import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# tower Q < Q(cbrt 2) < Q(cbrt 2, j) : degrees 3 then 2
box(ax, 4, 4, 46, 12, 'fixe', label='ℚ')
box(ax, 4, 31, 46, 12, 'sujet', label=r'ℚ($\sqrt[3]{2}$)')
box(ax, 4, 58, 46, 12, 'autre', label=r'ℚ($\sqrt[3]{2}$, $j$)')
arrow(ax, (27, 16.5), (27, 30.5), 'varie'); text(ax, 40, 23.5, '×3', 'varie', 'l', ha='left')
arrow(ax, (27, 43.5), (27, 57.5), 'varie'); text(ax, 40, 50.5, '×2', 'varie', 'l', ha='left')
arrow(ax, (66, 8), (66, 64), 'resultat')
text(ax, 76, 44, 'total', 'resultat', 's', ha='left')
text(ax, 76, 36, r'3 × 2', 'resultat', 'm', ha='left')
text(ax, 76, 28, r'$=6$', 'resultat', 'm', ha='left')
save(fig, '62-120')
