import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 3.4; x = 4; base = 12
groups = [([1, 2], 'sujet', '$Q(x)=5$'), ([2, 3], 'autre', '$Q(y)=13$'), ([4, 7], 'resultat', '$Q(xy)=65$')]
for sides, role, lab in groups:
    x_start = x
    for s in sides:
        box(ax, x, base, s * u, s * u, role, label=str(s), size='s', r=0.3)
        x += s * u + 1
    x_end = x - 1
    text(ax, (x_start + x_end) / 2, base + max(sides) * u + 4, lab, role, 's')
    x = x_end + 5
text(ax, 44, 5, r'$5\times13=65$', 'resultat', 'l')
save(fig, '78-073')
