import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 22, 66, 'A = 2·I', 'sujet', 'm', weight='bold')
text(ax, 22, 54, '2  0\n0  2', 'sujet', 'l')
for sgn, xx in ((-1, 12), (1, 32)):
    line(ax, [(xx - sgn * 1.5, 60), (xx, 60), (xx, 48), (xx - sgn * 1.5, 48)], 'encre', lw=0.9)
text(ax, 66, 66, 'deux chaînes de longueur 1', 'encre', 's')
for y, lab in ((56, 'e₁'), (42, 'e₂')):
    box(ax, 50, y - 5, 12, 10, 'sujet', label=lab, size='m')
    arrow(ax, (63, y), (74, y), 'varie')
    text(ax, 68.5, y + 3.5, 'T − 2', 'varie', 's')
    box(ax, 75, y - 5, 10, 10, 'resultat', label='0', size='m')
text(ax, 44, 28, 'deux blocs de taille 1', 'encre', 's')
text(ax, 44, 21, 'minimal : λ − 2   (degré 1)', 'autre', 's')
text(ax, 44, 14, 'caractéristique : (λ − 2)²', 'sujet', 's')
text(ax, 44, 7, 'degré 1 < degré 2', 'resultat', 's')
save(fig, '60-187')
