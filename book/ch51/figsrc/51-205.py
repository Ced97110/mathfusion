import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, x, y, vals, roles, cw=10, ch=9):
    for r in range(2):
        for c in range(2):
            box(ax, x + c*cw, y + (1-r)*ch, cw, ch, roles[r][c], label=vals[r][c], size="m")
    for sx, d in ((x - 1.5, 1), (x + 2*cw + 1.5, -1)):
        line(ax, [(sx + d*1.5, y - 1), (sx, y - 1), (sx, y + 2*ch + 1), (sx + d*1.5, y + 2*ch + 1)], "encre")

fig, ax = canvas(70)
text(ax, 44, 64, r'$R$ et $S$ ne commutent pas', 'encre', 'm')
text(ax, 22, 54, r'vrai $(R+S)^2$', 'sujet', 's')
text(ax, 66, 54, r'$R^2+2RS+S^2$', 'autre', 's')
base = 'sujet'; oth = 'autre'
mat(ax, 12, 32, [['3', '−3'], ['3', '0']], [['sujet', 'limite'], ['limite', 'sujet']])
mat(ax, 56, 32, [['3', '−2'], ['4', '0']], [['autre', 'limite'], ['limite', 'autre']])
text(ax, 44, 41, r'$\neq$', 'limite', 'l')
text(ax, 44, 20, r'$R$ : lignes (0, −1) et (1, 0)', 'fixe', 's')
text(ax, 44, 13, r'$S$ : lignes (2, 0) et (0, 1)', 'fixe', 's')
text(ax, 44, 5, r'$RS\neq SR$ : regrouper est faux', 'limite', 's')
save(fig, '51-205')
