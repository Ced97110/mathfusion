import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def case(cx, cy, rot, alpha, title, lab):
    c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    R = lambda x, y: (cx + x * c - y * s, cy + x * s + y * c)
    a = math.radians(alpha)
    line(ax, [R(-17, 0), R(17, 0)], 'fixe', lw=1.4)
    A = R(-14, 0); L = 28
    Hp = R(-14 + L * math.cos(a), 0); G = R(-14 + L * math.cos(a), L * math.sin(a))
    line(ax, [Hp, G], 'fixe', lw=0.9, dash=True)
    pts = [A] + [R(-14 + 14 * math.cos(a * k / 12), 14 * math.sin(a * k / 12)) for k in range(13)]
    poly(ax, pts, 'sujet', lw=0.5)
    line(ax, [A, G], 'autre', lw=1.8)
    line(ax, [A, Hp], 'sujet', lw=2.2)
    text(ax, *R(-14 + 21, -4.5), lab, 'sujet', 'm')
    text(ax, cx, cy + 40, title, 'encre', 's')
case(23, 22, 0, 21.8, 'le câble et le sol', r'$\alpha$ = 21,80°')
case(66, 18, 18, 38, 'une aiguille, un plan incliné', r'$\alpha$')
text(ax, 44, 6, 'α : angle de la droite avec le plan', 'sujet', 's')
save(fig, '27-059')
