import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(66)
x = 8
for s, role in [('3', 'sujet'), (',', None), ('1', 'sujet'), ('4', 'sujet'), ('1', 'fixe'), ('5', 'fixe'), ('9', 'fixe')]:
    if role is None:
        text(ax, x + 1.2, 52.5, ',', 'sujet', 'l'); x += 4.3; continue
    box(ax, x, 50, 8, 9, role, label=s, size='m', dash=(role == 'fixe')); x += 9
text(ax, x + 3, 54.5, '…', 'fixe', 'l')
line(ax, [(37.2, 46), (37.2, 63)], 'varie', lw=1.2, dash=True)
text(ax, 37.2, 42, 'on coupe ici', 'varie', 's')
box(ax, 6, 14, 36, 12, 'resultat', label=r'$\pi$ ≈ 3,14 : vrai', size='s')
box(ax, 46, 14, 36, 12, 'limite', label=r'$\pi$ = 3,14 : faux', size='s')
text(ax, 24, 8, '≈ : à peu près égal', 'resultat', 's')
text(ax, 64, 8, '= : exactement égal', 'limite', 's')
save(fig, '11-095')
