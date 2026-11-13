import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 12, 52, 28, 12, 'sujet', label='$(a+b)$')
box(ax, 48, 52, 28, 12, 'autre', label='$(c+d)$')
arrow(ax, (44, 52), (44, 41), 'varie')
text(ax, 47, 46, r'on distribue $(c+d)$', 'varie', 's', ha='left')
box(ax, 8, 28, 32, 12, 'varie', label='$(a+b)c$')
text(ax, 44, 34, '+', 'encre', 'l')
box(ax, 48, 28, 32, 12, 'varie', label='$(a+b)d$')
arrow(ax, (44, 28), (44, 17), 'varie')
text(ax, 47, 22, r'on distribue $(a+b)$', 'varie', 's', ha='left')
for i, t in enumerate(('$ac$', '$bc$', '$ad$', '$bd$')):
    box(ax, 5 + i * 20, 4, 18, 12, 'resultat', label=t)
save(fig, '15-089')
