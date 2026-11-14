import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$\eta : FM \to M$   (un seul)', 'sujet', 'l')
xs = [20, 40, 60]
for x, c, v in zip(xs, 'xyx', ['2', '3', '2']):
    box(ax, x - 6, 40, 12, 9, 'sujet', label=r'$'+c+r'$')
    box(ax, x - 6, 22, 12, 9, 'varie', label=v)
    arrow(ax, (x, 40), (x, 31.5), 'varie')
    arrow(ax, (x, 22), (40, 14.5), 'resultat')
text(ax, 2, 44.5, 'mot', 'sujet', 's', ha='left')
text(ax, 2, 26.5, 'choisi', 'varie', 's', ha='left')
text(ax, 73, 44.5, 'lettres', 'sujet', 's', ha='left')
text(ax, 73, 26.5, 'dans M', 'varie', 's', ha='left')
box(ax, 14, 5, 52, 9, 'resultat', label=r'$2\times3\times2=12$')
text(ax, 73, 9.5, 'imposé', 'resultat', 's', ha='left')
save(fig, '49-032')
