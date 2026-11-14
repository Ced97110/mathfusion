import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 23, 56, r'$\mathbb{R}$ : chapitre 24', 'fixe', 'm'); text(ax, 65, 56, r'$\mathbb{Z}$ : ce chapitre', 'sujet', 'm')
box(ax, 4, 40, 80, 10, 'fixe', label='I : ajouter un multiple')
box(ax, 4, 26, 38, 10, 'fixe', label=r'II : multiplier par $u\neq0$', size='s')
box(ax, 46, 26, 38, 10, 'varie', label=r'II : par $u$ inversible', size='s')
box(ax, 4, 12, 80, 10, 'fixe', label='III : échanger deux lignes')
text(ax, 44, 5, 'seule différence : le type II', 'varie', 'm')
save(fig, '59-058')
