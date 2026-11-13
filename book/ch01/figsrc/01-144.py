import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'Permis : un seul rang $k$', 'resultat', 'm')
xs = [6 + 10*i for i in range(8)]
for i, x in enumerate(xs):
    if i == 3:
        box(ax, x, 44, 8, 8, 'sujet', label=r'$k$', size='l', r=0.6)
    elif i == 0:
        box(ax, x, 44, 8, 8, 'fixe', fill=False, label=r'$n_0$', size='s', r=0.6)
    else:
        box(ax, x, 44, 8, 8, 'fixe', fill=False, r=0.6)
arrow(ax, (10, 40), (80, 40), 'varie', both=True)
text(ax, 44, 36, r'$k$ quelconque, au moins $n_0$', 'varie', 's')
text(ax, 44, 28, 'Refusé : tous les rangs', 'limite', 'm')
for i, x in enumerate(xs):
    box(ax, x, 14, 8, 8, 'limite', label=(r'$n_0$' if i == 0 else None), size='s', r=0.6)
brace(ax, 6, 84, 12, 'limite', label="= ce qu'on veut prouver", down=True)
save(fig, '01-144')
