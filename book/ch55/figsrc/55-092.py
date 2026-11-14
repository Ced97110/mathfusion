import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 7.0                      # hauteur d'une unité d'exposant
y0 = 18
A = (2, 1, 1); B = (1, 3, 2)
gx = [18, 42, 66]            # centre de chaque groupe
bw = 9
line(ax, [(8, y0), (84, y0)], 'fixe')
for g, (a, b) in enumerate(zip(A, B)):
    xa, xb = gx[g] - bw - 0.5, gx[g] + 0.5
    ax.add_patch(Rectangle((xa, y0), bw, a * u, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    ax.add_patch(Rectangle((xb, y0), bw, b * u, ec=COL['autre'], fc=FILL['autre'], lw=0.8, zorder=2))
    text(ax, xa + bw / 2, y0 + a * u + 2.2, str(a), 'sujet', 'm', weight='bold')
    text(ax, xb + bw / 2, y0 + b * u + 2.2, str(b), 'autre', 'm', weight='bold')
    text(ax, gx[g], y0 - 3.5, rf'$x_{g + 1}$', 'fixe', 'm')
# premier exposant : celui qui décide
box(ax, gx[0] - 11.5, y0 - 1, 23, 3 * u + 9, 'resultat', fill=False, lw=1.4, r=1.5)
text(ax, gx[0], y0 + 3 * u + 11, r'$2>1$ : on s’arrête', 'resultat', 'm', weight='bold')
brace(ax, gx[1] - 11, gx[2] + 11, y0 - 7, 'fixe', label='ne comptent plus', down=True)
text(ax, 22, 60, r'$x_1^2x_2x_3$ : degré 4', 'sujet', 'm')
text(ax, 62, 60, r'$x_1x_2^3x_3^2$ : degré 6', 'autre', 'm')
save(fig, '55-092')
