import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, r'$x \mapsto Hx$ : somme des bits', 'encre', 'm')
for y, w, v in [(46, '0000', '0'), (36, '0110', '0'), (22, '0111', '1'), (12, '1000', '1')]:
    box(ax, 4, y - 4, 18, 8, 'resultat' if v == '0' else 'fixe', label=w)
    arrow(ax, (22, y), (62, 41 if v == '0' else 17), 'varie')
box(ax, 62, 35, 18, 12, 'resultat', label='0')
box(ax, 62, 11, 18, 12, 'fixe', label='1')
text(ax, 44, 3, 'noyau : mots envoyés sur 0', 'resultat', 's')
save(fig, '68-112')
