import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
c = 6; x0, y0 = 24, 12
for i in range(8):
    for j in range(6):
        box(ax, x0 + i * c, y0 + j * c, c, c, 'resultat', lw=0.5, r=0.3)
brace(ax, x0, x0 + 8 * c, y0 + 6 * c + 2, 'sujet', down=False, label=r'8 choix de $u_1$')
text(ax, 11, y0 + 3 * c + 6, '6 choix', 'varie', 's')
text(ax, 11, y0 + 3 * c, r'de $u_2$', 'varie', 's')
text(ax, 44, 4, r'$8\times 6=48$ tableaux', 'resultat', 'l')
text(ax, 44, 76, r'$q=3$, $n=2$ : 9 vecteurs', 'sujet', 'm')
save(fig, '75-112')
