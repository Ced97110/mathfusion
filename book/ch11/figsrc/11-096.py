import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(70)
d = 20.0; x0 = 10
box(ax, 4, 56, 80, 9, 'sujet', label=r'$C$ = $\pi$ $\times$ $d$   avec   $d$ = 20 cm', size='m')
box(ax, 4, 42, 38, 9, 'resultat', label=r'$C$ = 20$\pi$ cm', size='m')
text(ax, 23, 38, 'exact', 'resultat', 's')
box(ax, 46, 42, 38, 9, 'varie', label=r'$C$ ≈ 62,8 cm', size='m')
text(ax, 65, 38, r'avec $\pi$ ≈ 3,14', 'varie', 's')
for i in range(3):
    box(ax, x0 + i * d, 14, d, 8, 'sujet', label='20 cm', size='s')
box(ax, x0 + 3 * d, 14, 2.8, 8, 'varie', r=0.3)
text(ax, x0 + 3 * d + 1.4, 26.5, 'reste 2,8 cm', 'varie', 's')
brace(ax, x0, x0 + 62.8, 14, 'fixe', label=r'3 $\times$ 20 = 60, plus 2,8')
save(fig, '11-096')
