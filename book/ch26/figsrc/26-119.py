import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(62)
for i, (n, y) in enumerate((('sinus', 44), ('cosinus', 31), ('tangente', 18))):
    box(ax, 4, y, 24, 9, 'sujet', label=n, size='s')
line(ax, [(30, 22.5), (32, 22.5), (32, 48.5), (30, 48.5)], 'sujet', lw=0.9)
line(ax, [(32, 35.5), (36, 35.5)], 'sujet', lw=0.9)
arrow(ax, (36, 35.5), (52, 35.5), 'varie', lw=1.2)
text(ax, 44, 40, 'inverse', 'varie', 's')
text(ax, 44, 31, '1 ÷ nombre', 'varie', 's')
box(ax, 54, 14, 30, 44, 'autre')
text(ax, 69, 49, 'sécante', 'autre', 'm'); text(ax, 69, 36, 'cosécante', 'autre', 'm'); text(ax, 69, 23, 'cotangente', 'autre', 'm')
text(ax, 44, 7, r'$\sin 30°=0{,}5$ : $1\div 0{,}5=2$', 'resultat', 's')
text(ax, 44, 2.5, 'qui va avec qui : chapitre 31', 'fixe', 's')
save(fig, '26-119')
