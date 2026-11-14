import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(66)
u = 5.0; x0 = 8
text(ax, 44, 61, r'$r$ = 3 m  $\rightarrow$  $d$', 'encre', 's')
for i in range(2):
    box(ax, x0 + i * 3 * u, 40, 3 * u, 8, 'sujet', label=r'$r$ = 3 m', size='s')
brace(ax, x0, x0 + 6 * u, 40, 'resultat', label=r'$d$ = 2 $\times$ 3 = 6 m')
text(ax, 44, 31, r'$d$ = 10 m  $\rightarrow$  $r$', 'encre', 's')
box(ax, x0, 18, 10 * u, 8, 'resultat', label=r'$d$ = 10 m', size='s')
for i in range(2):
    box(ax, x0 + i * 5 * u, 7, 5 * u, 8, 'sujet', label='5 m', size='s')
text(ax, x0 + 10 * u + 1, 11, r'$r$ = 10 $\div$ 2', 'sujet', 's', ha='left')
save(fig, '11-084')
