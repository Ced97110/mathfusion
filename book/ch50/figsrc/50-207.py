import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
R = 9.0
def tri(cx, cy, mark):
    v = {k: (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for k, a in (('T', 90), ('L', 210), ('R', 330))}
    poly(ax, [v['T'], v['L'], v['R']], 'fixe')
    mx, my = v[mark]; disc(ax, cx + (mx - cx) * .62, cy + (my - cy) * .62, 1.5, 'varie')
text(ax, 44, 94, r'$H\cap K=\{e\}$ ✓', 'resultat', 'm'); text(ax, 44, 87, r'$|HK|=3\times2=6=|G|$ ✓', 'resultat', 'm')
text(ax, 44, 80, r'$hk=kh$ ✗', 'limite', 'm', weight='bold')
# marker starts at T; r = third of a turn (T->L->R->T), s = mirror (T fixed, L<->R)
r_map = {'T': 'L', 'L': 'R', 'R': 'T'}; s_map = {'T': 'T', 'L': 'R', 'R': 'L'}
a, b = s_map[r_map['T']], r_map[s_map['T']]; assert (a, b) == ('R', 'L')
tri(16, 46, 'T'); tri(64, 62, a); tri(64, 30, b)
text(ax, 16, 33, 'départ', 'fixe', 's')
arrow(ax, (26, 50), (54, 60), 'varie'); text(ax, 36, 59, r'$r$ puis $s$', 'varie', 's')
arrow(ax, (26, 42), (54, 32), 'varie'); text(ax, 36, 33, r'$s$ puis $r$', 'varie', 's')
text(ax, 64, 46, '≠', 'limite', 'xl', weight='bold')
text(ax, 4, 22, r'$r$ : tiers de tour ($H$)', 'fixe', 's', ha='left'); text(ax, 4, 16, r'$s$ : réflexion ($K$)', 'fixe', 's', ha='left')
text(ax, 44, 6, r'$G\ncong H\times K$', 'limite', 'l', weight='bold')
save(fig, '50-207')
