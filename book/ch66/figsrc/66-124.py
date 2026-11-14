import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 12, 34, 34, 'sujet', fill=False)
text(ax, 19, 50, 'algèbre : exact', 'sujet', 's')
for i, s in enumerate(['groupes de Galois', 'traces', 'modules']):
    box(ax, 5, 33 - i * 9.5, 28, 7.5, 'sujet', label=s, size='s')
text(ax, 19, 7, r'aucun « $<$ » ici', 'fixe', 's')
arrow(ax, (36, 29), (42, 29), 'varie')
box(ax, 42, 21, 16, 16, 'sujet', label='(63)')
arrow(ax, (58, 29), (64, 29), 'varie')
box(ax, 64, 21, 22, 16, 'autre', label='tailles', dash=True)
text(ax, 75, 50, 'analytique', 'autre', 's')
text(ax, 75, 12, 'à suivre', 'autre', 's')
save(fig, '66-124')
