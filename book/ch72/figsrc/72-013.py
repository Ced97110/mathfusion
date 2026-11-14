import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(62)
box(ax, 4, 44, 36, 12, 'sujet', label=r'1. $B(y,x)$ = 4', size='m')
box(ax, 48, 44, 36, 12, 'sujet', label=r'2. $B(x,x)$ = 5', size='m')
box(ax, 26, 26, 36, 12, 'varie', label=r'3. 4 $\div$ 5', size='m')
arrow(ax, (22, 44), (38, 38.5), 'varie', lw=0.9); arrow(ax, (66, 44), (50, 38.5), 'varie', lw=0.9)
cw = 14
for i in range(5):
    poly(ax, [(9 + i*cw, 6), (9 + (i+1)*cw, 6), (9 + (i+1)*cw, 16), (9 + i*cw, 16)], 'resultat' if i < 4 else 'fixe')
text(ax, 44, 22, r'4. $p$ = (4/5) $x$', 'resultat', 'm')
text(ax, 9 + 2*cw, 1.8, r'$p$ = (1,6 ; 0,8) : 4 parts sur 5 de $x$', 'resultat', 's')
save(fig, '72-013')
