import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 71, 'N : les rotations', 'sujet', 's')
box(ax, 10, 48, 70, 16, 'sujet', fill=False)
box(ax, 10, 8, 70, 16, 'resultat', fill=False, dash=True)
top = ['1', 'r', 'r²', 'r³']; bot = ['1', 'r³', 'r²', 'r']
for i in range(4):
    x = 20 + 16 * i
    ch = top[i] != bot[i]
    disc(ax, x, 56, 5, 'sujet', label=top[i])
    disc(ax, x, 16, 5, 'resultat', label=bot[i])
    arrow(ax, (x, 50.5), (x, 22), 'varie' if ch else 'fixe')
text(ax, 5, 36, 'conjuguer par s', 'varie', 's', rot=90)
text(ax, 44, 2, 'gNg⁻¹ avec g = s', 'resultat', 's')
save(fig, '47-127')
