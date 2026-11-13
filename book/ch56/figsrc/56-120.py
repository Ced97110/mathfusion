import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(48, 'Entiers', r'$-5$', r'$5$', r'$\delta(-5)=|-5|=5$'),
        (22, 'Polynômes', r'$x^3+1$', r'$8$', r'$\delta(x^3+1)=2^3=8$')]
for y, head, a, b, cap in rows:
    text(ax, 4, y + 10.5, head, 'fixe', 's', ha='left')
    box(ax, 4, y, 20, 9, 'fixe', label=a)
    arrow(ax, (24, y + 4.5), (34, y + 4.5), 'varie')
    disc(ax, 40, y + 4.5, 6, 'sujet', label=r'$\delta$', size='l')
    arrow(ax, (46, y + 4.5), (56, y + 4.5), 'varie')
    box(ax, 56, y, 20, 9, 'resultat', label=b)
    text(ax, 44, y - 4, cap, 'encre', 's')
text(ax, 44, 4, r'$\delta$ donne toujours un entier de $\mathbb{N}$', 'sujet', 's')
save(fig, '56-120')
