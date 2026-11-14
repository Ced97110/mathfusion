import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Aides du lot L05 (chapitre 68) : rangées de bits alignées et diagramme à trois cercles.
BL = ' '  # espace de la largeur d'un chiffre (case sans bit)

def bitrow(fig, ax, xc, y, s, role='encre', size='l', k=7, weight='normal'):
    """Un seul texte pour une rangée de chiffres espacés régulièrement. Renvoie (centres x, pas)."""
    sep = ' ' * k
    t = text(ax, xc, y, sep.join(s), role, size, weight=weight)
    t1 = text(ax, 0, 0, '0', 'encre', size, weight=weight); t2 = text(ax, 0, 0, '0' + sep + '0', 'encre', size, weight=weight)
    fig.canvas.draw(); r = fig.canvas.get_renderer(); kk = W / fig.bbox.width
    p = (t2.get_window_extent(r).width - t1.get_window_extent(r).width) * kk
    t1.remove(); t2.remove()
    n = len(s)
    return [xc + (i - (n - 1) / 2) * p for i in range(n)], p

def cell(ax, x, y, w, h, role='sujet', fill=True, dash=False, lw=0.8):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, ec=COL[role], fc=FILL[role] if fill else 'none',
                           lw=lw, ls='--' if dash else '-', zorder=2))

def cells(ax, xs, p, y, h, roles):
    for x, r in zip(xs, roles):
        if r: cell(ax, x, y, p - 0.8, h, r)

VR, VD = 17.0, 17.0
_REG = {7: (0, 0), 6: (-8.66, 5), 5: (8.66, 5), 3: (0, -10), 4: (0, 13), 2: (-11.3, -6.5), 1: (11.3, -6.5)}
def venn(ax, cx, cy, roles=('sujet', 'varie', 'resultat'), lw=1.1):
    """Trois cercles A (haut), B (bas gauche), C (bas droite). Renvoie centres et positions 1 à 7."""
    s3 = math.sqrt(3)
    cen = {'A': (cx, cy + VD / s3), 'B': (cx - VD / 2, cy - VD / (2 * s3)), 'C': (cx + VD / 2, cy - VD / (2 * s3))}
    for n, ro, l in zip('ABC', roles, lw if isinstance(lw, (list, tuple)) else (lw, lw, lw)):
        disc(ax, cen[n][0], cen[n][1], VR, ro, fill=False, lw=l)
    return cen, {k: (cx + v[0], cy + v[1]) for k, v in _REG.items()}

def venn_labels(cen):
    """Positions des étiquettes A, B, C : A au-dessus, B et C sous leurs cercles."""
    return {'A': (cen['A'][0], cen['A'][1] + VR + 3.2),
            'B': (cen['B'][0] - 5, cen['B'][1] - VR - 3.6),
            'C': (cen['C'][0] + 5, cen['C'][1] - VR - 3.6)}

def crop(fig, ax, y0, y1):
    """Recadre la figure sur la bande verticale [y0, y1] (mm) pour retirer les vides en haut et en bas."""
    fig.set_size_inches(W * MM, (y1 - y0) * MM); ax.set_ylim(y0, y1); fig._h = y1 - y0
