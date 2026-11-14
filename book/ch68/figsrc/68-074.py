import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 46, 50, r'$d$ : distance minimale', 'fixe', 's')
text(ax, 75, 50, r'$t$ : erreurs corrigées', 'fixe', 's')
for y, name, d, t, role in [(34, 'répétition triple', 3, 1, 'resultat'), (14, 'bit de parité', 2, 0, 'fixe')]:
    text(ax, 2, y, name, 'encre', 'm', ha='left')
    text(ax, 46, y, rf'$d={d}$', 'sujet', 'l')
    arrow(ax, (54, y), (63, y), 'varie')
    box(ax, 64, y - 5, 22, 10, role, label=rf'$t={t}$', size='l', dash=(t == 0))
save(fig, '68-074')
