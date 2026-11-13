import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
vals = [-3, -2, -1, 0, 1, 2, 3]
f = lambda v: 8 + (v + 3) / 6 * 72
for v in vals:
    if v == 0:
        disc(ax, f(v), 30, 4.2, 'limite', fill=False, label='0')
    else:
        disc(ax, f(v), 30, 4.2, 'sujet', label=str(v).replace('-', '−'))
text(ax, f(0), 20, '0 est retiré', 'limite', 's')
brace(ax, f(-3) - 4, f(-1) + 4, 24, 'sujet', down=True)
brace(ax, f(1) - 4, f(3) + 4, 24, 'sujet', down=True)
text(ax, 44, 48, r'$D^{*}$ = tout $D$ sauf 0', 'sujet', 'l')
text(ax, 44, 8, 'les entiers non nuls', 'sujet', 's')
save(fig, '54-033')
