import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 51, r'$12\div6=2$', 'varie', 'l')
for i in range(12): box(ax, 8 + 6 * i, 28, 6, 8, 'sujet' if i < 6 else 'varie', r=0.2, lw=0.5)
brace(ax, 8, 44, 28, 'sujet', 'groupe de 6'); brace(ax, 44, 80, 28, 'varie', 'groupe de 6')
text(ax, 44, 9, r'$\frac{1}{6}=\frac{1\times2}{6\times2}=\frac{2}{12}$', 'resultat', 'm')
save(fig, '21-077')
