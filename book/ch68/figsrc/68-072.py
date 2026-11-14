import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 63, r'$B(000,\,t)$ grandit avec $t$', 'sujet', 'm')
rows = [(48, 0, 1, '000', 14), (30, 1, 4, '000   100   010   001', 40), (12, 3, 8, '000 001 010 011 100 101 110 111', 60)]
for y, t, n, ws, w in rows:
    text(ax, 11, y + 5, rf'$t={t}$' + f'\n{n} mot' + ('s' if n > 1 else ''), 'varie', 'm')
    box(ax, 24, y, w, 10, 'sujet', label=ws)
save(fig, '68-072')
