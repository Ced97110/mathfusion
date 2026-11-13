import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 0.55; ox, oy = 3, 14
A = (ox, oy); B = (ox + 60 * s, oy); C = (ox + 37.5 * s, oy + 33.07 * s)
poly(ax, [A, B, C], 'sujet')
text(ax, (A[0] + B[0]) / 2, oy - 3.5, '60 m', 'sujet', 's')
text(ax, 9, 31, '50 m', 'sujet', 's')
text(ax, 33, 31, '40 m', 'sujet', 's')
bx, bw, h, gap = 44, 42, 9.0, 4.0
rows = [(r'demi-périmètre $s=75$', 'sujet'), ('restes : 35 ; 25 ; 15', 'sujet'),
        (r'$75\times35\times25\times15=984\,375$', 'varie'), (r'$\Delta=375\sqrt{7}\approx 992{,}2$ m²', 'resultat')]
for i, (lab, role) in enumerate(rows):
    y = 51 - h - i * (h + gap)
    box(ax, bx, y, bw, h, role, label=lab, size='s')
    if i < 3: arrow(ax, (bx + bw / 2, y), (bx + bw / 2, y - gap), 'fixe')
save(fig, '37-109')
