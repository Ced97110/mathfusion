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
fig, ax = canvas(62)
k = 1.0
Ax, Ay = 12, 12
Bp = (Ax+60*k, Ay); Cx = (3600+2500-1600)/120; Cp = (Ax+Cx*k, Ay+math.sqrt(2500-Cx**2)*k)
poly(ax, [(Ax, Ay), Bp, Cp], 'sujet')
text(ax, Ax+30, Ay-5.5, '60 m', 'sujet', 's')
text(ax, (Ax+Cp[0])/2-3, (Ay+Cp[1])/2+3, '50 m', 'sujet', 's', ha='right')
text(ax, (Bp[0]+Cp[0])/2+3, (Bp[1]+Cp[1])/2+3, '40 m', 'sujet', 's', ha='left')
text(ax, Ax+31, Ay+12, 'aire fixée', 'resultat', 'm')
text(ax, 44, 57, 'trois clôtures seules', 'sujet', 'm')
box(ax, 64, 47, 22, 8, 'fixe', label='angles ?', size='s')
box(ax, 64, 37, 22, 8, 'fixe', label='hauteur ?', size='s')
save(fig, '37-004')
