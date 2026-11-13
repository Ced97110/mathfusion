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
fig, ax = canvas(66)
box(ax, 24, 46, 40, 14, 'resultat', label='aire ≈ 992,2', size='l')
box(ax, 2, 6, 38, 14, 'autre', label='mare : 13,23', size='m')
box(ax, 48, 6, 38, 14, 'sujet', label='puits : 30,24', size='m')
arrow(ax, (36, 45), (22, 21), 'varie', both=True); arrow(ax, (52, 45), (66, 21), 'varie', both=True)
text(ax, 17, 34, '× 75', 'varie', 's', ha='right'); text(ax, 17, 30.5, '÷ 75', 'varie', 's', ha='right')
text(ax, 71, 36, '120 000', 'varie', 's', ha='left'); text(ax, 71, 32.5, '÷ (4 × aire)', 'varie', 's', ha='left')
text(ax, 44, 64, '75 = (40+50+60) ÷ 2', 'fixe', 's')
save(fig, '37-007')
