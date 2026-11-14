import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, c1, c2, r1, r2, head, tag, role):
    text(ax, 2, y + 20, head, role, 's', ha='left')
    box(ax, 2, y + 6, 12, 9, r1, label=c1, size='m')
    text(ax, 25, y + 10.5, r'$\times 1\;+$', 'encre', 'm')
    box(ax, 36, y + 6, 12, 9, r2, label=c2, size='m')
    text(ax, 60, y + 10.5, r'$\times\, e\;=\;0$', 'encre', 'm')
    text(ax, 2, y, tag, role, 's', ha='left')
row(36, r'$v_1$', r'$v_2$', 'sujet', 'sujet', r'coefficients algébriques ($A$)', r'alors $v_1=v_2=0$', 'resultat')
row(4, r'$e$', r'$-1$', 'limite', 'sujet', r'un coefficient hors de $A$ : $e$', r'vaut 0, sans coefficient nul', 'limite')
save(fig, '66-086')
