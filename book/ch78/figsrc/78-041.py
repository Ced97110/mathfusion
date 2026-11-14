import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$A$ avec lui-même', 'sujet', 'l')
text(ax, 22, 52, r'$A\cdot A$', 'limite', 'm'); text(ax, 66, 52, r'$[A,A]$', 'resultat', 'm')
for r_, c_ in [(0,0),(0,1),(1,0),(1,1)]:
    box(ax, 6 + c_ * 16, 20 + (1 - r_) * 14, 16, 14, 'limite', label=[['7','10'],['15','22']][r_][c_])
    box(ax, 50 + c_ * 16, 20 + (1 - r_) * 14, 16, 14, 'resultat', label='0')
text(ax, 22, 12, r'$\neq 0$', 'limite', 'm'); text(ax, 66, 12, r'$=0$', 'resultat', 'm')
save(fig, '78-041')
