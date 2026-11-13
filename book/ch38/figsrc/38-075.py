import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role='varie'):
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    line(ax, pts, role)

fig, ax = canvas(70)
# échelle : 1000 m = 60 mm ; hauteur = 1000 x tan 18° = 19,5 mm
k = 60 / 1000
h = 1000 * math.tan(math.radians(18)) * k
A, B, g = 8, 8 + 1000 * k, 22
poly(ax, [(A, g), (B, g), (B, g + h)], 'sujet')
line(ax, [(B, g), (B, g + h)], 'resultat', lw=1.6)
line(ax, [(B - 3, g), (B - 3, g + 3), (B, g + 3)], 'fixe')
arc(ax, A, g, 16, 0, 18, 'varie')
text(ax, A + 22, g + 2.2, r'$\alpha=18°$', 'varie', 's')
text(ax, A, g - 4, 'A', 'sujet', 'm')
text(ax, B, g - 4, 'B', 'sujet', 'm')
text(ax, B + 6, g + 2, r'$\beta=90°$', 'fixe', 's')
text(ax, B + 6, g + h / 2 + 2, r'$h$', 'resultat', 'l')
brace(ax, A, B, g - 6.5, 'sujet', r'$d=1000$ m')
box(ax, 4, 52, 80, 12, 'resultat', label=r'$h=d\,\tan\alpha=1000\times0{,}32492\approx324{,}9$ m', size='s')
save(fig, '38-075')
