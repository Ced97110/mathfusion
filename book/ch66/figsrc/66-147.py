import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
f = numberline(ax, 6, 74, 40, 2, 6, step=1)
S = math.e + math.pi
disc(ax, f(math.e), 40, 1.5, 'sujet'); text(ax, f(math.e), 46, r'$e$', 'sujet', 'm')
disc(ax, f(math.pi), 40, 1.5, 'varie'); text(ax, f(math.pi), 46, r'$\pi$', 'varie', 'm')
disc(ax, f(S), 40, 1.8, 'autre'); text(ax, f(S), 46, r'$e+\pi$', 'autre', 'm')
text(ax, 3, 24, r'$e\approx2{,}71828$', 'sujet', 's', ha='left')
text(ax, 3, 17, r'$\pi\approx3{,}14159$', 'varie', 's', ha='left')
text(ax, 3, 10, r'$e+\pi\approx5{,}85987$', 'autre', 's', ha='left')
text(ax, 66, 24, 'algébrique ou transcendant ?', 'autre', 's')
box(ax, 46, 6, 40, 12, 'autre', label='on ne sait pas', dash=True)
save(fig, '66-147')
