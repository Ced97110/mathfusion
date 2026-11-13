"""Bibliothèque commune des figures. Unités : millimètres. Largeur fixe 88 mm.
Origine en bas à gauche, x vers la droite, y vers le haut.
Chaque couleur a UN rôle, le même dans tout le livre :
  'sujet'    bleu   : l'objet que la fiche définit
  'varie'    orange : ce qui change, l'action, le geste
  'fixe'     gris   : le décor, ce qui ne change pas
  'resultat' vert   : ce qu'on obtient, ce qui est vrai
  'limite'   rouge  : ce qui est faux, interdit, le contre-exemple
  'autre'    violet : un second objet que l'on compare au sujet
  'encre'    noir   : texte neutre
"""
import math, os, itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon, Circle, Rectangle
W = 88.0
COL = dict(sujet='#1f4e79', varie='#b8500a', fixe='#5f6773', resultat='#1a7445',
           limite='#b3261e', autre='#6d3fa0', encre='#1c1c1c')
FILL = dict(sujet='#d6e4f2', varie='#fbe3cf', fixe='#eceef1', resultat='#d5eedd',
            limite='#f8d9d6', autre='#e6daf3', encre='#ffffff')
SIZE = dict(s=6.5, m=7.5, l=9.0, xl=11.0)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans',
                     'svg.fonttype': 'path', 'font.size': 7.5})
MM = 1 / 25.4

def canvas(h_mm):
    """Crée la figure : 88 mm de large, h_mm de haut (30 à 120). Renvoie (fig, ax)."""
    fig = plt.figure(figsize=(W * MM, h_mm * MM))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, h_mm)
    ax.set_aspect('equal'); ax.axis('off'); fig._h = h_mm
    return fig, ax

def text(ax, x, y, s, role='encre', size='m', ha='center', va='center', weight='normal', style='normal', rot=0):
    return ax.text(x, y, s, color=COL[role], fontsize=SIZE.get(size, size), ha=ha, va=va,
                   fontweight=weight, fontstyle=style, rotation=rot, zorder=5)

def box(ax, x, y, w, h, role='fixe', fill=True, label=None, size='m', lw=0.8, r=0.8, dash=False, weight='normal'):
    """Rectangle de coin bas-gauche (x, y). label est centré dedans."""
    p = FancyBboxPatch((x + r, y + r), w - 2 * r, h - 2 * r, boxstyle=f'round,pad={r}', lw=lw,
                       ec=COL[role], fc=FILL[role] if fill else 'none', ls='--' if dash else '-', zorder=2)
    ax.add_patch(p)
    if label is not None: text(ax, x + w / 2, y + h / 2, label, role, size, weight=weight)
    return p

def disc(ax, x, y, r, role='fixe', fill=True, label=None, size='m', lw=0.8):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=2))
    if label is not None: text(ax, x, y, label, role, size)

def line(ax, pts, role='fixe', lw=0.9, dash=False):
    xs, ys = zip(*pts); ax.plot(xs, ys, color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3, solid_capstyle='round')

def arrow(ax, p, q, role='varie', lw=1.0, curve=0.0, both=False):
    """Flèche de p vers q. curve : courbure (0 = droite ; 0.3 = arc)."""
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='<|-|>' if both else '-|>', mutation_scale=7, lw=lw,
                 color=COL[role], connectionstyle=f'arc3,rad={curve}', zorder=4, shrinkA=0, shrinkB=0))

def poly(ax, pts, role='fixe', fill=True, lw=0.8):
    ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=2, joinstyle='round'))

def brace(ax, x0, x1, y, role='fixe', label=None, down=True, size='s', depth=1.6):
    """Accolade horizontale de x0 à x1 ; label au milieu, dessous (down) ou dessus."""
    d = -depth if down else depth; xm = (x0 + x1) / 2
    line(ax, [(x0, y), (x0, y + d / 2), (xm - 0.8, y + d / 2), (xm, y + d), (xm + 0.8, y + d / 2), (x1, y + d / 2), (x1, y)], role, lw=0.8)
    if label is not None: text(ax, xm, y + d * 1.3 + (-1.6 if down else 1.6), label, role, size)

def numberline(ax, x0, x1, y, vmin, vmax, step=1, labels=True, role='fixe', arrow_right=True, every=1, size='s', tick=1.2):
    """Droite graduée de vmin à vmax entre x0 et x1. Renvoie f(valeur) -> abscisse en mm."""
    f = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    if arrow_right: arrow(ax, (x0, y), (x1 + 5, y), role, lw=0.9)
    else: line(ax, [(x0, y), (x1, y)], role)
    n = int(round((vmax - vmin) / step))
    for i in range(n + 1):
        v = vmin + i * step
        ax.plot([f(v), f(v)], [y - tick, y + tick], color=COL[role], lw=0.8, zorder=1.5, solid_capstyle='round')
        if labels and i % every == 0:
            text(ax, f(v), y - tick - 2.2, f'{v:g}'.replace('.', ','), role, size)
    return f

# ---- 3D rigoureuse : projection axonométrique (isométrique) --------------
_C, _S = math.cos(math.radians(30)), math.sin(math.radians(30))
def iso(x, y, z, origin=(0, 0), u=1.0):
    """Projection isométrique exacte du point (x, y, z) : axes x et y à 30° de l'horizontale, z vertical.
    Les trois axes sont raccourcis du même facteur ; u = longueur en mm d'une unité."""
    return (origin[0] + (x - y) * _C * u, origin[1] + (x + y) * _S * u + z * u)

def cubes(ax, cells, origin, u, role='sujet', lw=0.5):
    """Dessine des cubes unité. cells : liste de (i, j, k) entiers (coin du cube). Tri en profondeur exact
    (du plus loin au plus près), trois faces visibles : dessus, gauche, droite."""
    shade = {'top': 1.0, 'left': 0.86, 'right': 0.72}
    import matplotlib.colors as mc
    base = mc.to_rgb(FILL[role])
    for (i, j, k) in sorted(cells, key=lambda c: (-(c[0] + c[1]), c[2]) if False else (c[2] - c[0] - c[1], c[2])):
        P = lambda a, b, c: iso(i + a, j + b, k + c, origin, u)
        faces = {'top': [P(0,0,1), P(1,0,1), P(1,1,1), P(0,1,1)],
                 'left': [P(0,0,0), P(0,0,1), P(1,0,1), P(1,0,0)][::1],
                 'right': [P(0,0,0), P(0,1,0), P(0,1,1), P(0,0,1)]}
        for name, pts in faces.items():
            fc = tuple(min(1, v * shade[name]) for v in base)
            ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=fc, lw=lw, zorder=2, joinstyle='round'))

def save(fig, code, outdir=None):
    """Enregistre figs/<code>.svg et .png. ÉCHOUE si un texte sort du cadre ou si deux textes se chevauchent."""
    outdir = outdir or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figs')
    fig.canvas.draw(); r = fig.canvas.get_renderer(); fb = fig.bbox
    boxes = []
    for ax in fig.axes:
        for t in ax.texts:
            if not t.get_text().strip(): continue
            b = t.get_window_extent(r)
            if b.x0 < fb.x0 - 0.5 or b.x1 > fb.x1 + 0.5 or b.y0 < fb.y0 - 0.5 or b.y1 > fb.y1 + 0.5:
                raise SystemExit(f'[{code}] TEXTE HORS CADRE : {t.get_text()!r}')
            if t.get_fontsize() < 6.4: raise SystemExit(f'[{code}] TEXTE TROP PETIT (<6.5 pt) : {t.get_text()!r}')
            boxes.append((b, t.get_text()))
    for (a, ta), (b, tb) in itertools.combinations(boxes, 2):
        ox = min(a.x1, b.x1) - max(a.x0, b.x0); oy = min(a.y1, b.y1) - max(a.y0, b.y0)
        if ox > 1.0 and oy > 1.0: raise SystemExit(f'[{code}] TEXTES QUI SE CHEVAUCHENT : {ta!r} / {tb!r}')
    from matplotlib.transforms import Bbox
    tb = fig.get_tightbbox(r); pad = 2.0 * MM
    bb = Bbox.from_extents(0, max(0, tb.y0 - pad), W * MM, min(fig._h * MM, tb.y1 + pad))
    fig.savefig(os.path.join(outdir, code + '.svg'), bbox_inches=bb); fig.savefig(os.path.join(outdir, code + '.png'), dpi=220, bbox_inches=bb)
    plt.close(fig); print('OK', code)
