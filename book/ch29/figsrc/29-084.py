import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

u = 5
r, s = 15, 30
cx, cy = 18, 14
a0, a1 = 90 - 57.3, 90 + 57.3
poly(ax, [(cx, cy)] + arcp(cx, cy, r, a0, a1), 'resultat')
line(ax, arcp(cx, cy, r, a0, a1), 'varie', lw=1.8)
for a in (a0, a1):
    line(ax, [(cx, cy), (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))], 'sujet', lw=1.3)
text(ax, cx, cy + r + 4.5, 's = 6 cm', 'varie', 's')
text(ax, 8, 14.5, 'r = 3 cm', 'sujet', 's', ha='center')
poly(ax, [(52, 14), (82, 14), (52, 29)], 'resultat')
line(ax, [(52, 14), (82, 14)], 'varie', lw=1.8)
line(ax, [(52, 14), (52, 29)], 'sujet', lw=1.3)
text(ax, 50.5, 21.5, 'hauteur r', 'sujet', 's', ha='right')
text(ax, 67, 9.5, 'base s', 'varie', 's')
text(ax, 41, 33, '=', 'encre', 'l')
text(ax, 44, 44, r'$A=\frac{1}{2}\times r\times s=9$ cm²', 'resultat', 'l')
save(fig, '29-084')
