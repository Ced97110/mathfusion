import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
Rr, r = 11, 3.2
cl, cr, cy = 22, 66, 46
labs = [r'$1$', r'$z$', r'$z^2$']

def tri(cx, role, fill):
    ax.add_patch(Circle((cx, cy), Rr, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
    for k in range(3):
        a = math.radians(120 * k)
        p = (cx + Rr * math.cos(a), cy + Rr * math.sin(a))
        disc(ax, p[0], p[1], r, role, fill=fill)
        text(ax, cx + (Rr + 7) * math.cos(a), cy + (Rr + 5.5) * math.sin(a), labs[k], role, 'm')

text(ax, 44, 74, 'racines cubiques de l\'unité', 'encre', 'm')
tri(cl, 'resultat', True)
tri(cr, 'limite', False)
text(ax, cl, 26, r'dans $F$ : groupe cyclique', 'resultat', 's')
text(ax, cr, 26, r'pas dans $F$ (fractions)', 'limite', 's')
box(ax, 44, 4, 42, 15, 'limite', label=r'$x^3=2$ : 6 éléments' + '\n' + 'pas abélien')
box(ax, 2, 4, 38, 15, 'resultat', label='hypothèse\nremplie')
save(fig, '64-152')
