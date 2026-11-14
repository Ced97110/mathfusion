import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, 'base de $E$ sur $F$ : 4 briques', 'sujet', 'm', weight='bold')
bs = ['1', r'$\sqrt{2}$', r'$\sqrt{3}$', r'$\sqrt{6}$']
for i, n in enumerate(bs):
    x = 3 + i * 21
    box(ax, x, 40, 17, 12, 'sujet', label=n, size='m')
    arrow(ax, (x + 8.5, 39), (x + 8.5, 31), 'resultat')
    text(ax, x + 8.5, 27, 'algébrique', 'resultat', 's')
text(ax, 44, 46 + 12.5, '', 'encre', 's')
brace(ax, 3, 83, 22, 'sujet', label=r'$E = F(u_1, \ldots, u_n)$', size='s')
text(ax, 44, 8, 'par le théorème $A$', 'resultat', 's')
save(fig, '61-121')
