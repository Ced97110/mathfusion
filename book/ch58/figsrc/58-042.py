import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# le signe, découpé
text(ax, 20, 59, r'$n$', 'varie', 'l')
text(ax, 20, 50, r'$\sum$', 'sujet', 28)
text(ax, 20, 41, r'$i=1$', 'varie', 'l')
text(ax, 34, 50, r'$x_i\,e_i$', 'sujet', 'l', ha='left')
text(ax, 60, 59, 'dernier numéro', 'varie', 's', ha='left')
text(ax, 60, 41, 'premier numéro', 'varie', 's', ha='left')
text(ax, 34, 44, 'le terme', 'sujet', 's', ha='left')
text(ax, 44, 31, 'pour n = 3, trois termes :', 'encre', 's')
for k in range(3):
    xc = 4 + k * 28
    box(ax, xc, 14, 22, 9, 'varie', label=r'$i=%d$' % (k + 1), size='s')
    arrow(ax, (xc + 11, 14), (xc + 11, 9), 'fixe', lw=0.8)
    box(ax, xc, 0.5, 22, 8.5, 'sujet', label=r'$x_%d\,e_%d$' % (k + 1, k + 1), size='s')
    if k < 2: text(ax, xc + 25, 4.7, '+', 'varie', 'l', weight='bold')
save(fig, '58-042')
