import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
line(ax, [(8, 12), (38, 12)], 'fixe')
for x in (8, 38):
    line(ax, [(x, 12), (x, 46)], 'limite', dash=True)
    line(ax, [(x + (1.5 if x == 8 else -1.5), 12), (x + (1.5 if x == 8 else -1.5), 13.5), (x, 13.5)], 'limite', lw=0.6)
text(ax, 15, 21, '90°', 'limite', 's'); text(ax, 31, 21, '90°', 'limite', 's')
text(ax, 23, 52, 'triangle impossible', 'limite', 's')
text(ax, 23, 5, 'les côtés ne se coupent pas', 'limite', 's')
text(ax, 66, 50, 'A = 30°, B = 90°', 'encre', 's')
text(ax, 66, 38, 'sin 120° = 0,866', 'sujet', 's')
text(ax, 66, 29, 'cos 30° = 0,866', 'sujet', 's')
text(ax, 66, 17, 'formule vraie', 'resultat', 'm')
save(fig, '34-152')
