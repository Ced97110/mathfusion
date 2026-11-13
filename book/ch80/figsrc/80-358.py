import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
box(ax, 6, 30, 26, 24, 'sujet')
text(ax, 11, 49, r'$U$', 'sujet', 'm')
disc(ax, 19, 39, 4, 'sujet', label='1')
box(ax, 40, 30, 42, 24, 'autre')
text(ax, 46, 49, r'$V$', 'autre', 'm')
disc(ax, 54, 39, 4, 'autre', label='2')
disc(ax, 70, 39, 4, 'autre', label='3')
text(ax, 44, 24, r"1 n'est pas dans $V$", 'limite', 's')
text(ax, 44, 15, r'$(-1)^1=-1$ : faux ici', 'limite', 's')
text(ax, 44, 6, r'$\mu(U,V)=0$', 'resultat', 'l')
save(fig, '80-358')
