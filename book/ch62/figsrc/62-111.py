import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# left: residues mod 5, a^5 = a for each, so F = F^p. right: t is not in F^p
text(ax, 22, 68, 'restes modulo 5', 'resultat', 'm', weight='bold')
disc(ax, 22, 44, 19, 'resultat')
for k in range(5):
    a = math.radians(90 + 72 * k)
    disc(ax, 22 + 11 * math.cos(a), 44 + 11 * math.sin(a), 4, 'sujet', label=str(k))
text(ax, 22, 44, r'$a^5=a$', 'resultat', 's')
box(ax, 2, 6, 40, 11, 'resultat', label=r'$F=F^p$ : parfait', size='s')
text(ax, 22, 20, r'$2^5=32$, reste $2$', 'fixe', 's')
text(ax, 66, 68, r'fractions en $t$', 'autre', 'm', weight='bold')
disc(ax, 66, 44, 19, 'fixe')
disc(ax, 66, 40, 9, 'autre', label=r'$F^p$')
disc(ax, 66, 58, 3.5, 'limite', label=r'$t$')
text(ax, 66, 51.5, r'$t\notin F^p$', 'limite', 's')
box(ax, 46, 6, 40, 11, 'limite', label=r'$F\neq F^p$ : pas parfait', size='s')
save(fig, '62-111')
