import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians

s = 0.0075
fig, ax = canvas(66)
def quad(ox, oy, diag, role):
    pt = lambda d, a: (ox + d*s*cos(radians(a)), oy + d*s*sin(radians(a)))
    A = (ox, oy); B = pt(3000, 0); D = pt(4000, 30); C = pt(5000, 60)
    poly(ax, [A, B, D, C], role)
    line(ax, [A, B, D, C, A], 'fixe', 1.2)
    p, q = (A, D) if diag == 0 else (B, C)
    line(ax, [p, q], role, 2.2, dash=True)
quad(9, 20, 0, 'sujet')
quad(55, 20, 1, 'autre')
text(ax, 22, 59, '1ʳᵉ diagonale', 'sujet', 's', weight='bold')
text(ax, 68, 59, 'autre diagonale', 'autre', 's', weight='bold')
text(ax, 22, 13, '8,00 km²', 'sujet', 'l', weight='bold')
text(ax, 68, 13, '8,35 km²', 'autre', 'l', weight='bold')
text(ax, 45, 38, '≠', 'limite', 'xl', weight='bold')
text(ax, 45, 3.5, 'même aire, deux résultats : une erreur', 'limite', 's', weight='bold')
save(fig, '38-064')
