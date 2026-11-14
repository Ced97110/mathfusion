import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(48)
stages = [(3, '01111', 'fixe', r'reçu $r$'), (26, '010', 'sujet', 'syndrome'),
          (49, '00010', 'varie', 'chef (table)'), (72, '01101', 'resultat', 'mot décodé')]
for k, (x, lab, role, name) in enumerate(stages):
    box(ax, x, 22, 16, 9, role, label=lab, size='s')
    text(ax, x + 8, 36, name, role, 's')
    if k < 3:
        arrow(ax, (x + 16.5, 26.5), (x + 22.5, 26.5), 'fixe')
text(ax, 34, 17, '0, 1, 0', 'fixe', 's')
text(ax, 44, 6, '01111 + 00010 = 01101', 'resultat', 'm')
save(fig, '68-172')
