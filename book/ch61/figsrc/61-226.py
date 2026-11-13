import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 6, 62, 76, 12, 'resultat', label=r'$\sqrt{3}=(t^3-14t)/4$')
text(ax, 44, 80, r'donc $\sqrt{3}$ est dans ℚ$(t)$', 'encre', 's')
for i in range(4):
    box(ax, 10 + 17 * i, 30, 17, 12, 'sujet' if i < 2 else 'varie')
brace(ax, 10, 44, 42, 'sujet', r'$\sqrt{3}$ : degré 2', down=False)
brace(ax, 44, 78, 42, 'varie', 'encore 2', down=False)
brace(ax, 10, 78, 30, 'resultat', r'ℚ$(t)$ : degré 4', down=True)
text(ax, 44, 14, 'reste de 4 ÷ 2 : 0', 'resultat', 's')
save(fig, '61-226')
