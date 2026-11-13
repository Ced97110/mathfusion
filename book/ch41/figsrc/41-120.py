import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)

def panel(ox, first, second, ccw, comp, res):
    o = (ox, 18); s = 16
    P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
    poly(ax, [P((0, 0)), P((1, 0)), P((1, 1)), P((0, 1))], 'fixe')
    d = {'i': (1, 0), 'j': (0, 1)}
    role = {'i': 'sujet', 'j': 'autre'}
    fa, fb = d[first], d[second]
    arrow(ax, P((0, 0)), P(fa), role[first], lw=1.4)
    arrow(ax, P((0, 0)), P(fb), role[second], lw=1.4)
    # arc du premier vers le second
    a0 = math.atan2(fa[1], fa[0]); a1 = math.atan2(fb[1], fb[0])
    mid = (o[0] + 0.45 * s * math.cos((a0 + a1) / 2), o[1] + 0.45 * s * math.sin((a0 + a1) / 2))
    p0 = (o[0] + 0.45 * s * math.cos(a0 + (0.15 if ccw else -0.15)), o[1] + 0.45 * s * math.sin(a0 + (0.15 if ccw else -0.15)))
    p1 = (o[0] + 0.45 * s * math.cos(a1 - (0.15 if ccw else -0.15)), o[1] + 0.45 * s * math.sin(a1 - (0.15 if ccw else -0.15)))
    arrow(ax, p0, p1, 'varie', lw=1.2, curve=0.35 if ccw else -0.35)
    text(ax, P(fa)[0] + (3 if first == 'i' else 0), P(fa)[1] + (0 if first == 'i' else 3), f'${first}$', role[first], 'm')
    text(ax, P(fb)[0] + (3 if second == 'i' else 0), P(fb)[1] + (0 if second == 'i' else 3), f'${second}$', role[second], 'm')
    text(ax, ox + 8, 44, 'sens ↺ : $+$' if ccw else 'sens ↻ : $-$', 'varie', 's')
    text(ax, ox + 8, 9, comp, 'resultat', 's')
    text(ax, ox + 8, 3.5, res, 'resultat', 'm')

panel(8, 'i', 'j', True, r'$1\times1-0\times0=1$', r'$i\times j=k$')
panel(52, 'j', 'i', False, r'$0\times0-1\times1=-1$', r'$j\times i=-k$')
save(fig, '41-120')
