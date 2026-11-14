import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
h = 6.6
top = 68
for i in range(8):
    y = top - h * (i + 1)
    box(ax, 16, y, 16, h, 'resultat' if i == 0 else 'sujet', label=str(i), size='s', r=0.3)
y0 = top - h / 2
y1 = top - h * 1.5
y7 = top - h * 7.5
arrow(ax, (35, y0), (35, y1), 'varie')
text(ax, 38, (y0 + y1) / 2, '+ 1', 'varie', 's', ha='left')
arrow(ax, (14, y7), (14, y0), 'varie', curve=-0.2)
text(ax, 52, 34, r'$\mathbb{Z}/8$', 'sujet', 'xl')
text(ax, 62, 22, '8 pas de 1 :', 'varie', 's')
text(ax, 62, 15, 'retour à 0', 'varie', 's')
text(ax, 62, 50, r'diviseur élémentaire', 'resultat', 's')
text(ax, 62, 43, r'$2^3=8$', 'resultat', 'l')
save(fig, '60-100')
