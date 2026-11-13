import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# Row builder: list of (label, width_in_cells, role); cell = 26 mm
C = 26.0; X0 = 5.0
def row(y, title, cells, brace_idx, brace_role):
    text(ax, 44, y + 14, title, 'encre', 's')
    x = X0
    for k, (lab, n, role) in enumerate(cells):
        box(ax, x, y, n * C - 1.0, 9, role, label=lab, size='s')
        if k == brace_idx:
            brace(ax, x, x + n * C - 1.0, y - 0.5, brace_role, label='« Sylow II »', down=True, size='s')
        x += n * C
row(40, 'Livre de Léa : trois numéros',
    [('I  Existence', 1, 'fixe'), ('II  Conjugaison', 1, 'autre'), ('III  Nombre', 1, 'fixe')], 1, 'autre')
row(14, 'Livre de Tom : deux numéros (Jacobson)',
    [('I  Existence', 1, 'fixe'), ('II  Conjugaison + nombre', 2, 'sujet')], 1, 'sujet')
text(ax, 44, 60, 'mêmes énoncés, regroupés autrement', 'varie', 's')
save(fig, '50-049')
