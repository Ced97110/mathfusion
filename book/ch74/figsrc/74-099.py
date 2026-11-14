import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
c = (30, 42); R = 17
for k in range(6):
    t = math.radians(60 * k)
    p = lambda r, da: (c[0] + r * math.cos(t + math.radians(da)), c[1] + r * math.sin(t + math.radians(da)))
    poly(ax, [c, p(9, -16), p(R, 0), p(9, 16)], 'varie' if k == 0 else 'sujet')
    q = (c[0] + (R + 8) * math.cos(t), c[1] + (R + 8) * math.sin(t))
    text(ax, q[0], q[1], f'{60*k}°', 'fixe', 's')
disc(ax, c[0], c[1], 1.4, 'encre')
text(ax, 72, 62, r'$C_n$', 'sujet', 'xl')
text(ax, 72, 52, r'$n=6$', 'sujet', 'l')
text(ax, 72, 40, '6 rotations', 'resultat', 's')
text(ax, 72, 34, 'même centre', 'fixe', 's')
text(ax, c[0], 7, 'la pétale orange part de 0°', 'varie', 's')
save(fig, '74-099')
