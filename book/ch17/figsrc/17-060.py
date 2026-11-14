import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 1.3; x0 = 6
def bars(y, n, w, role, lab):
    for i in range(n): box(ax, x0 + i * w * u, y, w * u, 8, role, r=0.3, lw=0.6)
    text(ax, x0, y + 12, lab, role, 'm', ha='left')
bars(44, 8, 3, 'sujet', r'8 fois 3 = 24')
bars(20, 8, 7, 'autre', r'8 fois 7 = 56')
for v in (24, 56):
    line(ax, [(x0 + v * u, 44), (x0 + v * u, 14)], 'fixe', dash=True)
    text(ax, x0 + v * u, 10, str(v), 'resultat', 'm')
text(ax, 58, 10, '<', 'resultat', 'l')
text(ax, 44, 3, 'chaque 3 est plus petit que 7', 'fixe', 's')
save(fig, '17-060')
