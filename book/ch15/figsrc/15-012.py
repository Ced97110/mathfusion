import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$3x+2y$ avec $x=2$, $y=5$', 'encre', 'm')
for i, p in enumerate((2, 2, 2, 5, 5)):
    box(ax, 15 + 12 * i, 36, 10, 10, 'sujet' if i < 3 else 'autre', label=str(p), weight='bold')
brace(ax, 15, 49, 35, 'sujet', '3 × 2 = 6'); brace(ax, 51, 73, 35, 'autre', '2 × 5 = 10')
text(ax, 44, 22, 'total : 6 + 10 = 16', 'resultat', 'm', weight='bold')
text(ax, 24, 8, r'$5x$ = 10 ≠ 16', 'limite', 's'); text(ax, 64, 8, r'$5y$ = 25 ≠ 16', 'limite', 's')
save(fig, '15-012')
