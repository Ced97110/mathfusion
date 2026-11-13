import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 22, 66, 44, 11, 'sujet', label=r'$(a-b)(c-d)$', size='l')
arrow(ax, (44, 66), (44, 58), 'varie')
text(ax, 62, 62, 'distributivité', 'varie', 's', ha='left')
items = [(r'$+\ a\times c$', 'resultat'), (r'$-\ a\times d$', 'varie'), (r'$-\ b\times c$', 'varie'), (r'$+\ b\times d$', 'resultat')]
for i, (s, r) in enumerate(items):
    box(ax, 2.25 + i * 21.5, 42, 19, 11, r, label=s)
box(ax, 2, 10, 38, 14, 'resultat', label=r'$a\times c+b\times d$', size='m')
box(ax, 48, 10, 38, 14, 'varie', label=r'$a\times d+b\times c$', size='m')
text(ax, 44, 17, '−', 'encre', 'xl')
arrow(ax, (11.75, 42), (14, 24), 'resultat'); arrow(ax, (54.75 + 0, 42), (66, 24), 'varie')
arrow(ax, (76.25, 42), (30, 24), 'resultat')
arrow(ax, (33.25, 42), (62, 24), 'varie')
text(ax, 21, 4.5, 'ce qu’on a', 'resultat', 's'); text(ax, 67, 4.5, 'ce qu’on doit', 'varie', 's')
save(fig, '13-113')
