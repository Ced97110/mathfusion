import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(84)
u = 3.0; ox, oy = 23, 36
B = (ox, oy); C = (ox + 14 * u, oy); A = (ox + 5 * u, oy + 12 * u)
poly(ax, [B, C, A], 'fixe')
text(ax, (B[0] + A[0]) / 2 - 3, (B[1] + A[1]) / 2 + 1, '13', 'sujet', 'm', weight='bold')
text(ax, (C[0] + A[0]) / 2 + 3, (C[1] + A[1]) / 2 + 1, '15', 'autre', 'm', weight='bold')
text(ax, (B[0] + C[0]) / 2, B[1] - 3.5, '14', 'fixe', 'm', weight='bold')
text(ax, C[0] - 5, C[1] + 3, '53,13°', 'sujet', 's', ha='right'); text(ax, B[0] + 5, B[1] + 3, '67,38°', 'autre', 's', ha='left')
text(ax, 44, 79, 'triangle de côtés 13, 14, 15', 'fixe', 's')
text(ax, 44, 22, r'côtés : $(15-13)/(15+13)=2/28=0{,}0714$', 'sujet', 's')
text(ax, 44, 15, 'sinus : 0,1231 / 1,7231 = 0,0714', 'autre', 's')
text(ax, 44, 7, 'même rapport : annonce du chapitre suivant', 'resultat', 's')
save(fig, '35-108')
