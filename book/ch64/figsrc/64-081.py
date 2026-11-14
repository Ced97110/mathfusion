import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
H = [0, 2, 4]; K = [0, 3]
text(ax, 6, 56, r'$H$', 'sujet', 'l')
text(ax, 28, 62, r'$K$', 'autre', 'l')
for j, k in enumerate(K):
    text(ax, 21 + j * 14, 56, str(k), 'autre', 'm')
for i, h in enumerate(H):
    y = 38 - i * 12
    text(ax, 6, y + 4.5, str(h), 'sujet', 'm')
    for j, k in enumerate(K):
        box(ax, 15 + j * 14, y, 12, 9, 'resultat', label=str((h + k) % 6), size='m')
text(ax, 67, 36, r'$HK=G$ :', 'resultat', 'm', weight='bold')
text(ax, 67, 28, 'les 6 heures,', 'resultat', 's')
text(ax, 67, 22, 'de 0 à 5', 'resultat', 's')
save(fig, '64-081')
