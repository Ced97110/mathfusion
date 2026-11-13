import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, u = 14, 12, 4.5
C = 0.866
cubes(ax, [(i, j, k) for i in range(4) for j in range(2) for k in range(3)], (ox, oy), u, 'sujet')
text(ax, ox+2*C*u+4, oy+u-3, 'L = 4', 'encre', 's')
text(ax, ox-1*C*u-5, oy+u-2, 'l = 2', 'encre', 's')
text(ax, ox+4*C*u+5, oy+1.5*u+2*u*0.5, 'h = 3', 'encre', 's')
text(ax, 42, 50, 'V : volume', 'sujet', ha='left', weight='bold')
text(ax, 42, 43, 'L : longueur', 'encre', 's', ha='left')
text(ax, 42, 37, 'l : largeur', 'encre', 's', ha='left')
text(ax, 42, 31, 'h : hauteur', 'encre', 's', ha='left')
text(ax, 42, 21, 'V = L × l × h', 'sujet', ha='left')
text(ax, 42, 12, 'V = 4 × 2 × 3 = 24', 'resultat', ha='left', weight='bold')
save(fig, '11-125')
