import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cs = 5.0; x0 = 6.5; ytop = 34
count = 0
for n in range(60):
    r, c = divmod(n, 15)
    mult = n % 3 == 0
    count += mult
    x = x0 + c * cs; y = ytop - r * cs
    box(ax, x, y, cs, cs, 'sujet' if mult else 'fixe', r=0.4, lw=0.4)
    if (mult and r == 0) or n == 57:
        text(ax, x + cs / 2, y + cs / 2, str(n), 'sujet', 's')
assert count == 20
brace(ax, x0, x0 + 15 * cs, ytop + cs + 2, 'fixe', label='60 places en 4 rangées de 15', down=False)
text(ax, 44, 8, r'$60/3=20$ multiples de 3', 'sujet', 'm', weight='bold')
text(ax, 44, 15, 'une case bleue sur trois', 'fixe', 's')
save(fig, '64-043')
