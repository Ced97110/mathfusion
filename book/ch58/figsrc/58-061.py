import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cy = [66, 44, 22]
box(ax, 2, 34, 21, 20, 'sujet', label='base de\n$M$ et\nrègle $\\mu$', size='s')
box(ax, 65, 34, 21, 20, 'resultat', label='isomor-\nphisme', size='s')
steps = [('sujet', '1  $\\mu$ respecte + et ×\n(2, 3) ↦ (7, 5)'),
         ('sujet', '2  tout élément\nest atteint'),
         ('varie', '3  seul le zéro\nva sur zéro')]
for (role, lab), y in zip(steps, cy):
    box(ax, 27, y - 8, 34, 16, role, label=lab, size='s')
    arrow(ax, (23, 44), (27, y), 'fixe', lw=0.8)
    arrow(ax, (61, y), (65, 44), 'resultat', lw=0.8)
text(ax, 44, 8, 'étape décisive : la 3', 'varie', 's')
save(fig, '58-061')
