import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# ligne du haut : degré 2, une formule existe
box(ax, 2, 52, 30, 12, 'fixe', label='second degré', size='s')
arrow(ax, (32, 58), (44, 58), 'resultat')
box(ax, 44, 52, 42, 12, 'resultat', label=r'formule avec $\sqrt{a}$, $\sqrt[3]{a}$…', size='s')
# ligne du bas : degré 5
box(ax, 2, 24, 84, 14, 'sujet', label=r'$x^5-4x+2=0$', size='l')
for i in range(5):
    x = 9 + i * 12.5
    disc(ax, x, 12, 4.2, 'sujet', label=f'$r_{i + 1}$', size='s')
    arrow(ax, (x, 24), (x, 16.5), 'sujet')
text(ax, 34, 3.2, r'5 solutions dans $\mathbb{C}$', 'sujet', 's')
text(ax, 44, 46.5, 'et au degré 5 ?', 'varie', 's')
box(ax, 66, 4, 20, 14, 'varie', label='formule du\nmême genre ?', size='s', dash=True)
arrow(ax, (76, 24), (76, 18.5), 'varie')
save(fig, '65-003')
