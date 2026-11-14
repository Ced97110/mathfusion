import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 2, 40, 58, 12, 'fixe', label='tous les nombres algébriques', size='s')
text(ax, 65, 46, r'$=$', 'encre', 'l')
box(ax, 72, 40, 14, 12, 'sujet', label=r'$A$', size='l')
cols = [(r'$u\in A$', 'sujet', '$u$ est algébrique'), (r'$v\in A$', 'sujet', '$v$ est algébrique'), (r'$u+v\in A$', 'resultat', 'la somme aussi')]
for i, (lab, role, expl) in enumerate(cols):
    x = 2 + i * 28.5
    box(ax, x, 14, 26, 11, role, label=lab, size='m')
    text(ax, x + 13, 8, expl, role, 's')
text(ax, 44, 32, r'$\in$ : « appartient à »', 'varie', 's')
save(fig, '66-081')
