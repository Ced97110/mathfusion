import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 20, 52, r'$0\times x=5$', 'limite', 'l'); text(ax, 68, 52, r'$0\times x=0$', 'resultat', 'l')
for i, y in enumerate((36, 26, 16)):
    box(ax, 4, y, 28, 7, 'limite', label='0 ≠ 5')
    box(ax, 56, y, 28, 7, 'resultat', label='0 = 0')
    text(ax, 44, y + 3.5, f'$x={i + 1}$', 'encre', 'm')
text(ax, 18, 8, 'jamais vrai', 'limite', 'm'); text(ax, 70, 8, 'toujours vrai', 'resultat', 'm')
save(fig, '16-076')
