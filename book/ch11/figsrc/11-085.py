import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(66)
d = 20.0; x0 = 10
disc(ax, 22, 50, 10, 'sujet'); ring(ax, 22, 50, 10, 'sujet')
arrow(ax, (12, 50), (32, 50), 'fixe', lw=1.0, both=True)
text(ax, 22, 54, r'$d$', 'fixe', 's')
text(ax, 22, 36.5, r'$C$ = tour du cercle', 'sujet', 's')
text(ax, 62, 56, 'on le coupe et on le déroule', 'varie', 's')
arrow(ax, (36, 52), (52, 52), 'varie', lw=1.2)
for i in range(3):
    box(ax, x0 + i * d, 14, d, 8, 'sujet', label=r'$d$', size='s')
box(ax, x0 + 3 * d, 14, 0.14 * d, 8, 'varie', r=0.3)
text(ax, x0 + 3 * d + 1.4, 26.5, 'reste < 1 $d$', 'varie', 's', ha='center')
brace(ax, x0, x0 + 3.14 * d, 14, 'sujet', label=r'$C$ : 3 $d$ et un reste')
save(fig, '11-085')
