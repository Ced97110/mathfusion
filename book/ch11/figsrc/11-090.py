import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(62)
f = numberline(ax, 10, 78, 20, 3.13, 3.16, step=0.01, arrow_right=False)
disc(ax, f(3.14), 20, 1.0, 'varie'); disc(ax, f(3.14159), 20, 1.0, 'sujet')
text(ax, f(3.14) - 6, 31, '3,14', 'varie', 'm', weight='bold')
arrow(ax, (f(3.14) - 4, 29), (f(3.14) - 0.5, 21.8), 'varie', lw=0.8)
text(ax, f(3.14159) + 14, 31, r'$\pi$ = 3,14159…', 'sujet', 'm', weight='bold')
arrow(ax, (f(3.14159) + 8, 29), (f(3.14159) + 0.5, 21.8), 'sujet', lw=0.8)
box(ax, 22, 44, 44, 11, 'resultat', label=r'$\pi$ ≈ 3,14 : très proche', size='m')
text(ax, 44, 8, r'$\pi$ = 3,14 : faux', 'limite', 's')
save(fig, '11-090')
