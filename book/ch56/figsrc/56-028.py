import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw, gap, x0 = 5.4, 1.2, 4
def row(n, y):
    for k in range(n):
        box(ax, x0 + k * cw + (k // 3) * gap, y, cw, 7, 'sujet', lw=0.5, r=0.3)
    return x0 + n * cw + ((n - 1) // 3) * gap
row(3, 62)
row(6, 44)
xe = row(12, 26)
text(ax, x0, 73, 'c = 3', 'sujet', 's', ha='left')
text(ax, x0, 55, 'b = 6 = 3 × d, d = 2', 'sujet', 's', ha='left')
text(ax, x0, 37, 'a = 12 = 6 × e, e = 2', 'sujet', 's', ha='left')
brace(ax, x0, xe, 26, 'varie', label='c ∣ a : quotient d × e = 4')
text(ax, 44, 10, '12 = 3 × (2 × 2) = 3 × 4', 'resultat', 's')
save(fig, '56-028')
