import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [('pente 1 : 45°', 45), ('pente 10 : 84,29°', 5.71), ('pente 100 : 89,43°', 0.57), ('pente 1 000 : 89,94°', 0.06)]
vals = ['45°', '5,71°', '0,57°', '0,06°']
k = 30/45; x0 = 38
text(ax, x0 + 12, 50, 'écart à 90°', 'varie', 's')
for i, (lab, e) in enumerate(rows):
    y = 40 - i*11
    text(ax, 2, y, lab, 'sujet', 's', ha='left')
    line(ax, [(x0, y), (x0 + e*k, y)], 'varie', lw=3.2)
    disc(ax, x0 + e*k, y, 0.9, 'varie')
    text(ax, x0 + e*k + 2.5, y, vals[i], 'varie', 's', ha='left')
line(ax, [(x0, 45), (x0, 9)], 'fixe', lw=0.6)
text(ax, x0+10, 3.5, 'jamais 90°', 'resultat', 's')
save(fig, '33-127')
