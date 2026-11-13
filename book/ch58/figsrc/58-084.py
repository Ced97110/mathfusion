import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 2, 76, 38, 13, 'sujet', label="module sur\nl'anneau $R$", size='s')
box(ax, 48, 76, 38, 13, 'autre', label='espace vectoriel\nsur le corps $F$', size='s')
text(ax, 44, 82.5, '$R=F$', 'varie', 'm')
box(ax, 2, 28, 84, 40, 'fixe', fill=True)
text(ax, 44, 63, 'les mêmes quatre règles', 'encre', 'm', weight='bold')
rules = [r'$\alpha(\beta v)=(\alpha\beta)v$', r'$(\alpha+\beta)v=\alpha v+\beta v$',
         r'$\alpha(u+v)=\alpha u+\alpha v$', r'$1v=v$']
for i, r in enumerate(rules):
    text(ax, 44, 55 - 7 * i, r, 'encre', 'm')
arrow(ax, (21, 76), (21, 68), 'sujet'); arrow(ax, (67, 76), (67, 68), 'autre')
arrow(ax, (44, 28), (44, 22), 'resultat')
box(ax, 10, 2, 68, 20, 'resultat', label='en plus dans $F$ :\non divise par un\nscalaire non nul', size='s')
save(fig, '58-084')
