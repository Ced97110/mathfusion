import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(82)
box(ax, 2, 66, 84, 14, 'sujet', label=r"$\dfrac{(x^6-1)(x-1)}{(x^3-1)(x^2-1)}$", size='m')
box(ax, 2, 42, 84, 14, 'varie', label=r"$\dfrac{(x^3-1)(x^3+1)(x-1)}{(x^3-1)(x-1)(x+1)}$", size='m')
box(ax, 2, 18, 84, 14, 'resultat', label=r"$\dfrac{x^3+1}{x+1}=x^2-x+1$", size='m')
arrow(ax, (30, 66), (30, 56), 'varie'); text(ax, 34, 61, 'on factorise', 'varie', 's', ha='left')
arrow(ax, (30, 42), (30, 32), 'varie'); text(ax, 34, 37, 'on simplifie', 'varie', 's', ha='left')
text(ax, 44, 9, r"$(x+1)(x^2-x+1)=x^3+1$", 'resultat', 's')
save(fig, '80-412')
