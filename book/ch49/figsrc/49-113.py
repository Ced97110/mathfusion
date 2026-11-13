import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, 'image des sommets A, B, C, D', 'encre', 's')
rows = [('neutre', 'ABCD', 'resultat'), ('quart de tour', 'BCDA', 'sujet'), ('demi-tour', 'CDAB', 'sujet'), ('réflexion (axe AC)', 'ADCB', 'sujet')]
y = 56
for name, im, role in rows:
    box(ax, 2, y - 5, 36, 10, role, label=name, size='s')
    arrow(ax, (39.5, y), (46, y), 'varie')
    for i, c in enumerate(im):
        box(ax, 48 + i * 9.5, y - 4.5, 8, 9, role, label=c, size='m')
    y -= 13
text(ax, 44, 5.5, '8 symétries, 8 lignes différentes', 'sujet', 's')
text(ax, 10, 63, '', 'encre', 's')
save(fig, '49-113')
