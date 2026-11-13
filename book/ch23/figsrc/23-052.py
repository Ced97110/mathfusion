import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(108)
L = [(r'$ax^2+bx+c=0$','sujet',''),
     (r'$x^2+\frac{b}{a}x=-\frac{c}{a}$','fixe','ligne 1'),
     (r'$x^2+\frac{b}{a}x+\frac{b^2}{4a^2}=-\frac{c}{a}+\frac{b^2}{4a^2}$','varie','ligne 2'),
     (r'$(x+\frac{b}{2a})^2=\frac{b^2-4ac}{4a^2}$','fixe','ligne 3'),
     (r'$x+\frac{b}{2a}=\pm\frac{\sqrt{b^2-4ac}}{2a}$','fixe','ligne 4'),
     (r'$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$','resultat','ligne 5')]
h = 14; gap = 3.2; y = 108 - 3 - h
prev = None
for i, (t, r, l) in enumerate(L):
    box(ax, 17, y, 69, h, r, label=t, size='s' if i == 2 else 'm')
    if l: text(ax, 2, y + h/2, l, 'fixe', 's', ha='left')
    if prev is not None: arrow(ax, (51, prev - 0.2), (51, y + h + 0.2), 'fixe')
    prev = y; y -= h + gap
save(fig, '23-052')
