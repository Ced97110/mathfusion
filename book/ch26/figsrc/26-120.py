import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(60)
f = numberline(ax, 8, 76, 36, 0, 1.4, step=0.1, labels=False, arrow_right=False)
line(ax, [(f(0), 36), (f(1), 36)], 'sujet', lw=2.6)
brace(ax, f(0), f(1), 40, 'sujet', 'sinus possibles : de 0 à 1', down=False)
disc(ax, f(0.5), 36, 1.6, 'resultat'); disc(ax, f(1.2), 36, 1.6, 'limite')
text(ax, f(0), 30, '0', 'encre', 's'); text(ax, f(1), 30, '1', 'encre', 's')
text(ax, f(0.5), 30, '0,5', 'resultat', 's'); text(ax, f(1.2), 30, '1,2', 'limite', 's')
arrow(ax, (f(0.5), 26), (24, 17), 'resultat'); arrow(ax, (f(1.2), 26), (64, 17), 'limite')
box(ax, 4, 5, 40, 12, 'resultat', label=r'arcsin 0,5 = 30°', size='m')
box(ax, 46, 5, 38, 12, 'limite', label='arcsin 1,2 : erreur', size='m')
save(fig, '26-120')
