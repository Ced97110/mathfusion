import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 15, 66, 'fonction de départ', 'sujet', 's')
text(ax, 44, 66, 'restriction + inverse', 'varie', 's')
text(ax, 73, 66, 'réciproque obtenue', 'resultat', 's')
for y, a, b in ((50, 'carré', 'racine carrée'), (36, 'sinus', 'arcsinus'), (22, 'cosinus', 'arccosinus'), (8, 'tangente', 'arctangente')):
    box(ax, 2, y, 27, 9, 'sujet', label=a)
    box(ax, 59, y, 27, 9, 'resultat', label=b)
    arrow(ax, (31, y + 4.5), (57, y + 4.5), 'varie')
save(fig, '33-028')
