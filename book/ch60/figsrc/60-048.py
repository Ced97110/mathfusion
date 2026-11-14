import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'g = 2 et h = 6 : facteur 2 commun', 'limite', 'm')
w = 6.8
for n in range(12):
    if n in (0, 6): r, fill = 'sujet', True
    elif n % 2 == 0: r, fill = 'autre', True
    elif n == 1: r, fill = 'limite', True
    else: r, fill = 'fixe', False
    lab = str(n) if (n % 2 == 0 or n == 1) else None
    box(ax, 3.2 + w * n, 38, w, 9, r, fill=fill, dash=not fill, label=lab, size='s', r=0.3)
text(ax, 44, 28, r'$Dy$ = {0, 6}', 'sujet', 'm')
text(ax, 44, 21, r'$Dz$ = les heures paires', 'autre', 'm')
text(ax, 44, 13, r'$Dy \cap Dz$ = {0, 6} : pas seulement 0', 'limite', 's')
text(ax, 44, 6, r'$Dy + Dz$ n’atteint pas 1', 'limite', 'm', weight='bold')
save(fig, '60-048')
