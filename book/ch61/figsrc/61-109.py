import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 24, 56, 'groupe : 12 éléments', 'sujet', 's')
text(ax, 65, 56, 'corps : degré 4', 'autre', 's')
for i in range(12):
    box(ax, 4 + i * 3.3, 32, 3.2, 8, 'sujet' if i < 10 else 'limite', r=0.3, lw=0.6)
brace(ax, 4, 20.7, 41, 'sujet', label='5', down=False)
brace(ax, 21, 37.7, 41, 'sujet', label='5', down=False)
for i in range(4):
    box(ax, 46 + i * 9.5, 32, 9, 8, 'autre' if i < 3 else 'limite', r=0.3, lw=0.6)
brace(ax, 46, 73, 41, 'autre', label='3', down=False)
text(ax, 24, 24, '5 ne divise pas 12', 'limite', 's')
text(ax, 65, 24, '3 ne divise pas 4', 'limite', 's')
line(ax, [(44, 20), (44, 50)], 'fixe', dash=True)
text(ax, 44, 9, 'même forme : la partie divise le tout', 'resultat', 's')
save(fig, '61-109')
