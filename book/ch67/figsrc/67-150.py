import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'$E/F$ cyclique, $G$ engendré par $\eta$', 'fixe', 's')
box(ax, 4, 52, 36, 12, 'sujet', label=r'$N(u)=1$')
box(ax, 48, 52, 36, 12, 'varie', label=r'$u=v/\eta(v)$')
arrow(ax, (40.5, 58), (47.5, 58), 'fixe', both=True)
text(ax, 44, 67, 'équivaut', 'fixe', 's')
text(ax, 44, 44, r'exemple dans $\mathbb{F}_9$ sur $\mathbb{F}_3$', 'encre', 's')
labs = [(r'$v=1+i$', 'sujet'), (r'$\eta(v)=1-i$', 'autre'), (r'$v/\eta(v)=i$', 'varie'), (r'$N(i)=1$', 'resultat')]
for k, (lab, role) in enumerate(labs):
    box(ax, 3 + 21.3 * k, 28, 18, 10, role, label=lab, size='s')
    if k < 3:
        arrow(ax, (21.3 + 21.3 * k, 33), (24.3 + 21.3 * k, 33), 'fixe')
box(ax, 8, 6, 72, 14, 'fixe', label=r'$v$ et $\eta(v)$ : même norme' + '\n' + 'donc quotient de norme 1', size='s')
save(fig, '67-150')
