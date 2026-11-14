import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 24, 64, 40, 13, 'sujet', label=r'$\sqrt{4 \times 9}$', size='l')
arrow(ax, (34, 64), (24, 48), 'fixe'); arrow(ax, (54, 64), (64, 48), 'varie')
box(ax, 3, 34, 38, 13, 'fixe', label=r'$\sqrt{36} = 6$', size='m')
box(ax, 47, 34, 38, 13, 'varie', label=r'$\sqrt{4} \times \sqrt{9}$', size='m')
arrow(ax, (66, 34), (66, 28), 'varie')
box(ax, 47, 16, 38, 11, 'varie', label=r'$2 \times 3 = 6$', size='m')
arrow(ax, (22, 34), (36, 12), 'resultat'); arrow(ax, (66, 16), (56, 12), 'resultat')
box(ax, 26, 1, 36, 11, 'resultat', label=r'même résultat : 6', size='s')
text(ax, 4, 22, r'comme $(ab)^n = a^n b^n$', 'sujet', 's', ha='left') if False else None
text(ax, 44, 83, r'$\sqrt{a}$ suit les règles de $a^{1/2}$', 'sujet', 's')
save(fig, '14-098')
