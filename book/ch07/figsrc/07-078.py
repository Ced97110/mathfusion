import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 64, r'$\frac{55}{48} = 1\frac{7}{48}$', 'resultat', 'xl')
c = 3.0
for k in range(48): box(ax, 8 + (k % 8) * c, 28 + (k // 8) * c, c, c, 'sujet', lw=0.4, r=0.1)
text(ax, 39, 34, '+', 'varie', 'l')
for k in range(7): box(ax, 46 + k * c, 40.5, c, c, 'varie', lw=0.4, r=0.1)
brace(ax, 8, 67, 49, 'fixe', label='55 morceaux', down=False)
text(ax, 20, 20, 'un entier : 48 morceaux', 'sujet', 's')
text(ax, 56, 31, '7 morceaux de plus', 'varie', 's')
text(ax, 44, 8, r'$55 = 48 + 7$', 'fixe', 'm')
save(fig, '07-078')
