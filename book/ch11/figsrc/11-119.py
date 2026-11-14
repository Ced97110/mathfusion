import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
n = 10; r = 11; cx, cy = 14, 34
w = 2*math.pi*r/n
for k in range(n):
    role = 'sujet' if k % 2 == 0 else 'autre'
    a0, a1 = 360/n*k, 360/n*(k+1)
    pts = [(cx, cy)] + [(cx+r*math.cos(math.radians(a0+(a1-a0)*i/6)), cy+r*math.sin(math.radians(a0+(a1-a0)*i/6))) for i in range(7)]
    poly(ax, pts, role)
X0 = 40; yb = cy - r/2; yt = cy + r/2
for k in range(n):
    role = 'sujet' if k % 2 == 0 else 'autre'
    xk = X0 + w/2 + k*w/2
    if k % 2 == 0: pts = [(xk-w/2, yb), (xk+w/2, yb), (xk, yt)]
    else: pts = [(xk-w/2, yt), (xk+w/2, yt), (xk, yb)]
    poly(ax, pts, role)
arrow(ax, (27, cy), (36, cy), 'varie')
text(ax, cx, 49, '10 secteurs', 'sujet', 's')
text(ax, 58, 46, 'rangés tête-bêche', 'varie', 's')
brace(ax, X0, X0+5*w, yb, 'resultat', 'base ≈ π r = 9,42')
x_d = X0 + 5.5*w + 2.5
arrow(ax, (x_d, yb), (x_d, yt), 'fixe', both=True)
text(ax, x_d+3.5, cy, 'r = 3', 'fixe', 's', rot=90)
text(ax, 44, 9, 'A ≈ 9,42 × 3 = 28,26', 'resultat', weight='bold')
save(fig, '11-119')
