import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'coefficients dans ℝ, un corps', 'resultat', 's')
box(ax, 2, 36, 20, 12, 'sujet', label='(2 ; 1)')
for y, s in [(56, '×2 : (4 ; 2)'), (40, '×(−1) : (−2 ; −1)'), (24, '×½ : (1 ; ½)')]:
    box(ax, 50, y, 36, 9, 'resultat', label=s, size='s')
    arrow(ax, (23, 42), (49, y + 4.5), 'varie')
line(ax, [(2, 19), (86, 19)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 15, 'coefficients dans ℤ', 'limite', 's')
box(ax, 2, 2, 20, 9, 'sujet', label='(2 ; 1)')
box(ax, 50, 2, 36, 9, 'limite', label='×½ : interdit', size='s')
arrow(ax, (23, 6.5), (49, 6.5), 'limite')
save(fig, '57-087')
