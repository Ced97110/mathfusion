import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 4, 84, 54, 'sujet', lw=1.2)
text(ax, 12, 50, r'$F$', 'sujet', 'l')
text(ax, 58, 51, 'toutes les fractions de ℤ', 'sujet', 's')
for x, s in [(6, r'$\frac{2}{3}$'), (30, r'$\frac{1}{2}$'), (54, r'$-\frac{7}{4}$')]:
    box(ax, x, 18, 20, 18, 'encre', label=s, size='l')
text(ax, 80, 27, '…', 'sujet', 'l')
text(ax, 44, 10, 'chaque élément = un groupe de couples', 'sujet', 's')
save(fig, '54-042')
