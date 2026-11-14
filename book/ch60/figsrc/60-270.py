import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, 'deux matrices, deux listes', 'fixe', 's')
for k, (L, y, role) in enumerate((('d', 52, 'sujet'), ('e', 32, 'autre'))):
    for i in range(3):
        last = i == 2
        lab = rf'${L}_3=m$' if last else rf'${L}_{i+1}$'
        box(ax, 4 + 13 * i, y, 12, 9, 'resultat' if last else role, label=lab, size='s')
    text(ax, 46, y + 4.5, rf'$f={L}_1{L}_2{L}_3$', role, 's', ha='left')
text(ax, 30, 46.5, 'même produit f, même m', 'resultat', 's')
text(ax, 44, 22, 'mêmes listes, ou listes différentes ?', 'varie', 'm')
text(ax, 80, 42, '?', 'varie', 'xl', weight='bold')
save(fig, '60-270')
