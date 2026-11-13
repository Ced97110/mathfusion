import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
steps = [(r'$x^2+6x=16$', 'sujet', '+ 9 des deux côtés'), (r'$x^2+6x+9=25$', 'varie', 'écrit en carré'),
         (r'$(x+3)^2=25$', 'varie', 'racine carrée'), (r'$x+3=5$', 'varie', r'$-3$'), (r'$x=2$', 'resultat', None)]
for i, (s, role, act) in enumerate(steps):
    y = 66 - i * 15
    box(ax, 4, y, 40, 9, role, True, label=s)
    if act:
        arrow(ax, (24, y - 0.5), (24, y - 5.5), 'fixe')
        text(ax, 30, y - 3, act, 'encre', 's', ha='left')
save(fig, '23-012')
