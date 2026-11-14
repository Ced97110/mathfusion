import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
xs = [3, 33, 63]
for x, l, r in zip(xs, ['0,75', '75', '75 %'], ['sujet', 'varie', 'resultat']):
    box(ax, x, 22, 22, 12, r, label=l, size='l')
arrow(ax, (26, 28), (32, 28), 'varie')
arrow(ax, (56, 28), (62, 28), 'varie')
text(ax, 29, 39, r'$\times$ 100', 'varie', 's')
text(ax, 59, 39, r'$\times\frac{1}{100}$', 'varie', 's')
brace(ax, 14, 74, 20, 'fixe', label=r"$100\times\frac{1}{100}=1$ : même valeur")
save(fig, '09-076')
