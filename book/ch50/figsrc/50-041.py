import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 16, 72, 26, 0, 2, 1, arrow_right=False, size='m')
text(ax, 81, 26, r'$k$', 'encre', 'm')
labs = [r'$2^0=1$', r'$2^1=2$', r'$2^2=4$']
for k in range(3):
    role = 'resultat' if k == 2 else 'sujet'
    box(ax, f(k) - 11, 36, 22, 9, role, label=labs[k])
    arrow(ax, (f(k), 35.5), (f(k), 28.5), 'fixe', lw=0.8)
text(ax, f(2) - 4, 52, r'$k=m=2$ : un 2-Sylow', 'resultat', 'm')
brace(ax, f(0), f(2), 19, 'fixe', r'$k$ va de 0 à $m$')
save(fig, '50-041')
