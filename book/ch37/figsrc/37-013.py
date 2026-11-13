import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role='varie', lw=0.9):
    line(ax, [(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/30)), c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/30))) for i in range(31)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    line(ax, [(p[0]+d1[0]*s, p[1]+d1[1]*s), (p[0]+(d1[0]+d2[0])*s, p[1]+(d1[1]+d2[1])*s), (p[0]+d2[0]*s, p[1]+d2[1]*s)], role, 0.7)
def field(k=0.5, O=(14, 10)):
    th = math.radians(53)
    C = O; A = (O[0]+120*k, O[1]); B = (O[0]+110*math.cos(th)*k, O[1]+110*math.sin(th)*k); H = (B[0], O[1])
    return C, A, B, H
fig, ax = canvas(68)
k = 0.5; x0 = 8
box(ax, x0, 50, 110*k, 6, 'sujet'); text(ax, x0+55*k, 59, r'$a$ = 110 m : se mesure', 'sujet', 's')
w = 110*0.7986*k
box(ax, x0, 34, w, 6, 'resultat')
line(ax, [(x0+w, 40), (x0+w, 56)], 'varie', 1.0, dash=True)
text(ax, x0+w/2, 30.5, r'$h$ ≈ 87,85 m', 'resultat', 's')
text(ax, x0+w+3, 45, r'$\sin C \approx 0{,}7986$', 'varie', 's', ha='left')
text(ax, x0+w+3, 41.5, 'de la clôture', 'varie', 's', ha='left')
box(ax, 10, 8, 68, 13, 'fixe', label=r'$h = a \times \sin C$', size='l')
text(ax, 44, 65, 'hauteur = produit de 2 mesures', 'encre', 'm')
save(fig, '37-013')
