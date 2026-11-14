import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, lab, role in ((50, r'$4x-7=9$', 'sujet'), (30, r'$4x=16$', 'fixe'), (10, r'$x=4$', 'resultat')):
    box(ax, 6, y, 34, 10, role, label=lab, size='l')
arrow(ax, (23, 50), (23, 40), 'varie'); arrow(ax, (23, 30), (23, 20), 'varie')
text(ax, 28, 45, '+ 7 aux deux membres', 'varie', 's', ha='left')
text(ax, 28, 25, '÷ 4 aux deux membres', 'varie', 's', ha='left')
text(ax, 44, 15, 'vérif. : 4 × 4 − 7 = 9', 'resultat', 's', ha='left')
save(fig, '16-080')
