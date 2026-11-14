import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cw, gap, h, y = 4.4, 0.6, 7, 32
x0 = (88 - (16 * cw + 15 * gap)) / 2
gx = lambda i: x0 + i * (cw + gap)
for i in range(16):
    role = 'fixe' if i < 2 else ('autre' if i < 4 else 'sujet')
    poly(ax, [(gx(i), y), (gx(i) + cw, y), (gx(i) + cw, y + h), (gx(i), y + h)], role)
text(ax, 44, 62, r'$q=2,\ n=4$ : 16 racines', 'encre', 'm')
text(ax, (gx(0) + gx(1) + cw) / 2, 46, r'$x,\ x+1$', 'fixe', 's')
text(ax, (gx(2) + gx(3) + cw) / 2, 53, r'$x^{2}+x+1$', 'autre', 's')
text(ax, (gx(4) + gx(15) + cw) / 2, 46, 'reste : 16 − 2 − 2 = 12', 'sujet', 's')
brace(ax, gx(0), gx(3) + cw, y - 1, 'fixe', label='2 + 2')
for j in range(3):
    brace(ax, gx(4 + 4 * j), gx(7 + 4 * j) + cw, y - 1, 'sujet', label='degré 4')
text(ax, 44, 14, '12 ÷ 4 = 3 polynômes', 'resultat', 'm')
save(fig, '67-194')
