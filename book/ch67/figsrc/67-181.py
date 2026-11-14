import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def sq(x, y, s, role):
    poly(ax, [(x, y), (x + s, y), (x + s, y + s), (x, y + s)], role)

text(ax, 44, 60, r'$\mathbb{F}_{8}$ n’est pas dans $\mathbb{F}_{16}$', 'encre', 'l')
# ligne A : 4 cases, paquets de 3
s, g = 8, 1.5
x0 = (88 - (4 * s + 3 * g)) / 2
for i in range(4):
    sq(x0 + i * (s + g), 38, s, 'sujet' if i < 3 else 'limite')
box(ax, x0 - 1, 36.5, 3 * s + 2 * g + 2, s + 3, 'sujet', fill=False, dash=True)
text(ax, 44, 52, r'$\mathbb{F}_{16}$ : 4 cases, paquets de 3', 'sujet', 'm')
text(ax, 44, 31, '3 ne divise pas 4 (reste 1)', 'limite', 'm')
# ligne B : 15 cases, paquets de 7
s, g, x0 = 4.6, 0.8, 3.9
gx = lambda i: x0 + i * (s + g)
for i in range(15):
    sq(gx(i), 12, s, 'sujet' if i < 14 else 'limite')
for a in (0, 7):
    box(ax, gx(a) - 0.2, 11, 7 * s + 6 * g + 0.4, s + 2, 'sujet', fill=False, dash=True)
text(ax, 44, 22.5, '15 cases, paquets de 7', 'sujet', 'm')
text(ax, 44, 5, '7 ne divise pas 15 (reste 1)', 'limite', 'm')
save(fig, '67-181')
