import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
base, k, w = 48, 1.4, 10
text(ax, 44, 84, r'$N(4,2)=\frac{1}{4}\,(16-4+0)$', 'encre', 'l')
line(ax, [(5, base), (84, base)], 'fixe')
cols = [(14, 'd = 1', '$\\mu(1)=1$\n$\\times2^{4}$', 16, 'sujet', '+16'),
        (36, 'd = 2', '$\\mu(2)=-1$\n$\\times2^{2}$', -4, 'varie', '−4'),
        (58, 'd = 4', '$\\mu(4)=0$\n$\\times2^{1}$', 0, 'fixe', '0')]
for cx, dl, ml, v, role, vl in cols:
    if v > 0:
        poly(ax, [(cx - w / 2, base), (cx + w / 2, base), (cx + w / 2, base + v * k), (cx - w / 2, base + v * k)], role)
        text(ax, cx, base + v * k + 3, vl, role, 'm')
    elif v < 0:
        poly(ax, [(cx - w / 2, base), (cx + w / 2, base), (cx + w / 2, base + v * k), (cx - w / 2, base + v * k)], role)
        text(ax, cx, base + v * k - 3, vl, role, 'm')
    else:
        text(ax, cx, base + 3, vl, role, 'm')
    text(ax, cx, 32, dl, 'encre', 'm')
    text(ax, cx, 23.5, ml, role, 's')
cx = 78
poly(ax, [(cx - w / 2, base), (cx + w / 2, base), (cx + w / 2, base + 12 * k), (cx - w / 2, base + 12 * k)], 'resultat')
text(ax, cx, base + 12 * k + 3, '12', 'resultat', 'm')
text(ax, cx, 32, 'somme', 'encre', 'm')
text(ax, 44, 9, '16 − 4 + 0 = 12 ; 12 ÷ 4 = 3', 'resultat', 'm')
save(fig, '67-195')
