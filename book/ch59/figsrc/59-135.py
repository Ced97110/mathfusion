import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)

def clock(cx, cy, n, role, r=7.0):
    disc(ax, cx, cy, r, role, fill=False)
    for k in range(n):
        a = math.pi / 2 - 2 * math.pi * k / n
        disc(ax, cx + r * math.cos(a), cy + r * math.sin(a), 0.9, role)

cy = 42
for cx, n, role in [(12, 6, 'autre'), (32, 4, 'autre'), (58, 2, 'sujet'), (78, 12, 'sujet')]:
    clock(cx, cy, n, role)
    text(ax, cx, cy - 11, r'$\mathbb{Z}/%d$' % n, role, 's')
text(ax, 22, cy, r'$\oplus$', 'encre', 'l')
text(ax, 68, cy, r'$\oplus$', 'encre', 'l')
text(ax, 45, cy, r'$\cong$', 'encre', 'xl')
text(ax, 22, 21, '6 ne divise pas 4', 'limite', 's')
text(ax, 68, 21, '2 divise 12', 'resultat', 's')
text(ax, 44, 9, '24 éléments de chaque côté', 'encre', 's')
save(fig, '59-135')
