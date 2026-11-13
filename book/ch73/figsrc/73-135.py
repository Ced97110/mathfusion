import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 20, 36, r'$O$', 'sujet', 56); text(ax, 68, 36, r'$\Omega$', 'autre', 56)
text(ax, 44, 36, '≠', 'limite', 56)
text(ax, 20, 12, 'lettre latine', 'sujet', 's'); text(ax, 20, 5, 'groupe orthogonal', 'sujet', 's')
text(ax, 68, 12, 'lettre grecque', 'autre', 's'); text(ax, 68, 5, 'groupe dérivé', 'autre', 's')
text(ax, 20, 54, '« o »', 'sujet', 'm'); text(ax, 68, 54, '« oméga »', 'autre', 'm')
save(fig, '73-135')
