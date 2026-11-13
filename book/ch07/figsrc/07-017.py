import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
X, CW, H = 12, 8, 9
fig,ax=canvas(72)
for y, d, a, b in ((46, 7, 2, 4), (12, 5, 3, 1)):
    row(ax, X, y, CW, H, ['fixe'] * a + ['sujet'] * b + [None] * (d - a - b))
    xa = X + a * CW / 2; xb = X + (a + b / 2) * CW
    text(ax, xa, y + H + 5, f'{a}/{d}', 'fixe', 'l'); text(ax, (xa + xb) / 2, y + H + 5, '+', 'encre', 'l')
    text(ax, xb, y + H + 5, f'{b}/{d}', 'sujet', 'l')
    brace(ax, X + 0.5, X + a * CW - 0.5, y, 'fixe', f'$a={a}$')
    brace(ax, X + a * CW + 0.5, X + (a + b) * CW - 0.5, y, 'sujet', f'$b={b}$')
    text(ax, X + d * CW + 3, y + H / 2, f'$d={d}$', 'fixe', 'm', ha='left')
save(fig,'07-017')
