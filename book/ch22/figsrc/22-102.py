import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
u, x0 = 22, 6
f = numberline(ax, x0, x0 + 3 * u, 8, 0, 3, 1)
r2, r3, r5 = 2 ** 0.5, 3 ** 0.5, 5 ** 0.5
box(ax, f(0), 26, r2 * u, 8, 'sujet', label=r'$\sqrt{2}\approx1{,}414$', size='s')
box(ax, f(r2), 26, r3 * u, 8, 'autre', label=r'$\sqrt{3}\approx1{,}732$', size='s')
brace(ax, f(0), f(r2 + r3), 35, 'fixe', r'$\approx3{,}146$', down=False)
box(ax, f(0), 14, r5 * u, 8, 'limite', label=r'$\sqrt{5}\approx2{,}236$', size='s')
text(ax, f(r5) + 3, 18, "n'est pas la somme", 'limite', 's', ha='left')
save(fig, '22-102')
