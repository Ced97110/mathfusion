import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 23, 64, 'quotient entier', 'fixe', 's'); text(ax, 65, 64, 'quotient non entier', 'fixe', 's')
box(ax, 3, 48, 40, 10, 'sujet', label=r'$\sqrt{80}/\sqrt{5}$')
box(ax, 45, 48, 40, 10, 'autre', label=r'$\sqrt{3}/\sqrt{2}$')
for cx, lab in ((23, r'$80:5=16$'), (65, r'$\times\sqrt{2}/\sqrt{2}$')):
    arrow(ax, (cx, 48), (cx, 32), 'varie'); text(ax, cx + 3, 40, lab, 'varie', 's', ha='left')
box(ax, 3, 22, 40, 10, 'resultat', label=r'$\sqrt{16}$')
box(ax, 45, 22, 40, 10, 'resultat', label=r'$\sqrt{6}/2$')
text(ax, 23, 16, 'un seul radical', 'resultat', 's'); text(ax, 65, 16, 'dénominateur entier', 'resultat', 's')
save(fig, '22-097')
