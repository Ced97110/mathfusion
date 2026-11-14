import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'$y^5$ = 5 facteurs $y$', 'encre', 'm')
for i in range(5):
    box(ax, 5+i*16, 50, 14, 12, role='sujet' if i < 4 else 'fixe', fill=True, label=r'$y$')
brace(ax, 5, 67, 50, 'sujet', label=r'$y^4$ : exposant pair')
brace(ax, 69, 83, 50, 'fixe', label=r'$y$')
arrow(ax, (36, 41), (36, 30), 'resultat')
text(ax, 39, 36, r'$4\div2=2$', 'resultat', 's', ha='left')
box(ax, 21, 18, 30, 12, role='resultat', fill=True, label=r'$y^2$', size='l')
arrow(ax, (76, 41), (76, 30), 'fixe')
box(ax, 64, 18, 24, 12, role='fixe', fill=True, label=r'$\sqrt{y}$', size='l')
text(ax, 44, 8, r'$\sqrt{y^5}=y^2\sqrt{y}$', 'encre', 'm')
save(fig, '22-079')
