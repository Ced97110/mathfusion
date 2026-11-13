import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$n=2$ générateurs du plan', 'sujet', 's')
box(ax, 8, 60, 24, 9, 'sujet', label='(1, 0)', size='s')
box(ax, 34, 60, 24, 9, 'sujet', label='(0, 1)', size='s')
text(ax, 44, 30, r'$m=3$ vecteurs indépendants ?', 'varie', 's')
xs = [8, 34, 60]
labs = ['(3, 1)', '(1, 2)', '(−1, 3)']
for i, (x, l) in enumerate(zip(xs, labs)):
    if i < 2:
        box(ax, x, 38, 24, 9, 'varie', label=l, size='s')
        arrow(ax, (x + 12, 48), (x + 12, 59), 'varie')
    else:
        box(ax, x, 38, 24, 9, 'limite', dash=True, label=l, size='s')
text(ax, 72, 56, 'plus de place', 'limite', 's')
arrow(ax, (72, 53), (72, 49), 'limite')
text(ax, 44, 20, r'$3>2$ est impossible', 'limite', 's')
box(ax, 22, 4, 44, 10, 'resultat', label=r'donc $m\leq n$', weight='bold')
save(fig, '58-172')
