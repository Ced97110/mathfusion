import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$m$ = 0,001 = $10^{-3}$', 'sujet', 'xl')
box(ax, 4, 38, 26, 10, 'sujet', label=r'5 $mg$')
arrow(ax, (33, 43), (51, 43), 'varie')
box(ax, 54, 38, 30, 10, 'resultat', label='0,005 g')
for i in range(5):
    box(ax, 3 + i * 16.8, 16, 16, 10, 'sujet', label='0,001 g', size='s')
brace(ax, 3, 85, 14, 'resultat', '5 × 0,001 g = 0,005 g')
text(ax, 44, 4, '1 000 mg = 1 g', 'encre', 's')
save(fig, '11-042')
