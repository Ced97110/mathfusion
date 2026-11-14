import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
cx, cy, R = 44, 10, 40
arc = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in range(0, 181, 3)]
line(ax, arc, 'fixe', lw=1.0); line(ax, [(4, cy), (84, cy)], 'fixe', lw=1.0)
hh = math.sqrt(3) * 20
line(ax, [(24, cy), (24, cy + hh)], 'resultat', lw=1.6)
for x in (4, 24, 84): disc(ax, x, cy, 0.9, 'sujet')
disc(ax, 24, cy + hh, 1.0, 'resultat')
brace(ax, 4, 24, cy, 'sujet', label='1'); brace(ax, 24, 84, cy, 'varie', label='r = 3')
text(ax, 19, 28, r'$\sqrt{3}$', 'resultat')
text(ax, 58, 20, r'diamètre $1+r$', 'fixe', 's')
save(fig, '61-167')
