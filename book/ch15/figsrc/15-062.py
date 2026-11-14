import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 2, 14, 84, 40, 'sujet')
text(ax, 44, 48, 'polynôme : tous les cas', 'sujet', 'l', weight='bold')
labs = [('monôme\n1 terme', 'fixe'), ('binôme\n2 termes', 'fixe'), ('trinôme\n3 termes', 'fixe'), ('4 termes\nou plus', 'autre')]
for i, (t, r) in enumerate(labs): box(ax, 5.25 + i * 20, 20, 17.5, 18, r, label=t, size='s')
text(ax, 44, 7, r'$4x^2$ : monôme et polynôme', 'sujet', 'm')
save(fig, '15-062')
