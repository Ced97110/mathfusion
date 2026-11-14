import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tri(cx, cy, R, axis, role):
    c30 = math.cos(math.radians(30))
    V = {'A': (cx, cy + R), 'B': (cx - R * c30, cy - R / 2), 'C': (cx + R * c30, cy - R / 2)}
    poly(ax, [V['A'], V['B'], V['C']], 'fixe')
    v = V[axis]
    line(ax, [(cx + 1.3 * (v[0] - cx), cy + 1.3 * (v[1] - cy)), (cx - 0.85 * (v[0] - cx), cy - 0.85 * (v[1] - cy))], role, lw=1.8)
fig, ax = canvas(92)
text(ax, 15, 86, r'$H=\{e,\ s_A\}$', 'sujet', 's')
tri(15, 75, 6, 'A', 'sujet')
heads = ['1 prendre\nchaque $g$', '2 garder si', '3 comparer\nà $H$']
text(ax, 58, 86.5, 'lire de gauche à droite :', 'fixe', 's')
text(ax, 58, 80, '$g$, puis « tel que $gHg^{-1}=H$ »', 'fixe', 's')
cols = [(14, 'e', 'A', 'resultat', 'passe', r'$\{e,\ s_A\}$'), (44, 's_A', 'A', 'resultat', 'passe', r'$\{e,\ s_A\}$'), (74, 'r', 'B', 'limite', 'échoue', r'$\{e,\ s_B\}$')]
for x, g, ax_, role, verdict, conj in cols:
    box(ax, x - 12, 54, 24, 9, role, label='$g = %s$' % g, size='s')
    arrow(ax, (x, 53), (x, 47), 'varie', lw=1.0)
    tri(x, 36, 7.5, ax_, role)
    text(ax, x, 23, 'conjugué : ' , role, 's')
    text(ax, x, 18.5, conj, role, 's')
    text(ax, x, 10, verdict, role, 'm', weight='bold')
save(fig, '50-074')
