import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$q=2$, $n=2$ : 4 vecteurs', 'sujet', 'm')
for a in range(3):
    y = 44 - a * 14
    box(ax, 4, y - 4.5, 22, 9, 'sujet', label=f'$u_1$ n°{a + 1}', size='s')
    for b in range(2):
        line(ax, [(26, y), (40, y + (3 if b == 0 else -3))], 'varie', lw=0.9)
        disc(ax, 44, y + (3 if b == 0 else -3), 2.0, 'varie')
text(ax, 64, 44, '3 choix de $u_1$', 'sujet', 's')
text(ax, 64, 30, 'puis 2 choix de $u_2$', 'varie', 's')
text(ax, 64, 16, r'$3\times 2=6$', 'resultat', 'l')
text(ax, 44, 3, '= les 6 feuilles de l’arbre', 'resultat', 's')
save(fig, '75-111')
