import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
CL, CR = 25, 65          # centres des deux colonnes
text(ax, 4, 76, r'$x=$', 'encre', 'l', ha='left')
text(ax, CL, 76, r'$\sqrt[3]{2+\sqrt{-121}}$', 'sujet', 'l')
text(ax, 45, 76, r'$+$', 'encre', 'l')
text(ax, CR, 76, r'$\sqrt[3]{2-\sqrt{-121}}$', 'autre', 'l')
# 1 : dans chaque racine cubique se cache la racine carrée de -121
ys = [51, 36, 21]
for c in (CL, CR):
    box(ax, c - 19, ys[0], 38, 10, 'limite', label=r'$\sqrt{-121}$ : pas un réel', size='s')
    arrow(ax, (c, 70), (c, ys[0] + 10), 'limite')
# 2 : les deux nombres formés avec 2
box(ax, CL - 19, ys[1], 38, 10, 'sujet', label=r'$2+\sqrt{-121}$')
box(ax, CR - 19, ys[1], 38, 10, 'autre', label=r'$2-\sqrt{-121}$')
# 3 : racine cubique de chacun
box(ax, CL - 19, ys[2], 38, 10, 'varie', label='racine cubique', size='s')
box(ax, CR - 19, ys[2], 38, 10, 'varie', label='racine cubique', size='s')
for c in (CL, CR):
    arrow(ax, (c, ys[0]), (c, ys[1] + 10), 'fixe')
    arrow(ax, (c, ys[1]), (c, ys[2] + 10), 'fixe')
# 4 : somme
box(ax, 2, 4, 84, 9, 'resultat', label='on additionne : somme = 4')
arrow(ax, (CL, ys[2]), (38, 13), 'fixe')
arrow(ax, (CR, ys[2]), (50, 13), 'fixe')
save(fig, '39-006')
