import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'degré 2, corps à 2 éléments', 'encre', 's')
items = [(4, 38, r'$x^2$ : se factorise', 'fixe'), (46, 38, r'$x^2+1$ : se factorise', 'fixe'),
         (4, 22, r'$x^2+x$ : se factorise', 'fixe'), (46, 22, r'$x^2+x+1$ : irréductible', 'sujet')]
for x, y, s, r in items:
    box(ax, x, y, 38, 12, r, label=s, size='s')
arrow(ax, (65, 22), (65, 12.5), 'sujet')
box(ax, 24, 3, 60, 9, 'sujet', label=r'$N(2,2)=1$ : un seul', size='m')
save(fig, '67-055')
