import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
nodes = {'e': (24, 14), 'B': (12, 36), 'K': (12, 58), 'C': (38, 40), 'T': (24, 74)}
def nb(k, role, lab): 
    x, y = nodes[k]; box(ax, x - 7, y - 4, 14, 8, role, label=lab, size='s')
line(ax, [(24, 18), (12, 32)]); line(ax, [(12, 40), (12, 54)]); line(ax, [(12, 62), (24, 70)])
line(ax, [(24, 18), (38, 36)]); line(ax, [(38, 44), (24, 70)])
nb('e', 'fixe', r'$\{e\}$'); nb('B', 'sujet', r'$B$'); nb('K', 'sujet', r'$K$'); nb('C', 'autre', r'$C$'); nb('T', 'fixe', r'$B \vee C$')
box(ax, 52, 56, 34, 10, 'fixe', label=r'$K \cap (B \vee C) = K$', size='s')
box(ax, 52, 38, 34, 10, 'fixe', label=r'$B \vee (K \cap C) = B$', size='s')
box(ax, 52, 20, 34, 10, 'limite', label=r'$K \neq B$ : M fausse', size='s')
arrow(ax, (69, 38), (69, 30), 'limite')
save(fig, '79-156')
