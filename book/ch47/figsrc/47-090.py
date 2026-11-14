import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
u = 5.0
for y, n, role, lab in [(66, 12, 'sujet', r'$|G|=12$'), (52, 4, 'varie', r'$|H|=4$'), (38, 2, 'autre', r'$|K|=2$')]:
    for i in range(n):
        box(ax, 4 + i * u, y, u - 0.6, 7, role, r=0.3, lw=0.6)
    text(ax, 4 + n * u + 2, y + 3.5, lab, role, 's', ha='left')
text(ax, 44, 30, r'on multiplie et divise par $|H|$', 'varie', 's')
text(ax, 44, 20, r'$\frac{12}{2}=\frac{12}{4}\times\frac{4}{2}$', 'encre', 'l')
text(ax, 44, 8, r'$[G:K]=[G:H]\times[H:K]$', 'resultat', 'm')
save(fig, '47-090')
