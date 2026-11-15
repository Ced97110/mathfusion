// Copyright: Your Name. Apache 2.0
// Text system of « Vent de travers »: HTML over the canvas, one sans-serif family, three sizes,
// tabular figures, every text on a dark plate. Everything is a pure function of the film time t:
// one caption (legendes(d)), at most 3 arrow labels (carte.etiquettes(e)) pushed apart when they
// overlap, the letters A B C, the "1 heure" bar of shot 2 and the final plate with the triangle.

import { COULEUR, fr, legendes, prog, smooth } from './communs.js';

/** Type table: [size at 1920 px wide, size at 390 px wide], CSS px. */
export const TAILLES = Object.freeze({ legende: [44, 20], etiquette: [32, 16], source: [22, 12] });
const MAX_ETIQUETTES = 3;
const FONDU = 0.25; // caption fade, s

/**
 * Text sizes for a film frame `largeur` px wide. Landscape: linear between the 390 and 1920 columns
 * (proportional above 1920). Vertical: the 390 column scaled to the frame width.
 */
export function tailles(largeur, vertical) {
  const out = {};
  for (const [nom, [grand, petit]] of Object.entries(TAILLES)) {
    if (vertical) out[nom] = (petit * largeur) / 390;
    else if (largeur >= 1920) out[nom] = (grand * largeur) / 1920;
    else out[nom] = petit + ((grand - petit) * Math.max(0, largeur - 390)) / (1920 - 390);
  }
  return out;
}

/** Role colour (name or hex) -> { trait: solid colour, texte: tint light enough for >= 7:1 on the plate }. */
export function teinte(couleur) {
  const hex = (COULEUR[couleur] || (typeof couleur === 'string' && couleur.startsWith('#') ? couleur : COULEUR.gris)).slice(1);
  const c = [0, 2, 4].map((i) => parseInt(hex.slice(i, i + 2), 16));
  const clair = c.map((v) => Math.round(v + (255 - v) * 0.6));
  return { trait: `#${hex}`, texte: `rgb(${clair.join(',')})` };
}

/** Accepts the label shapes carte.etiquettes(e) may return. */
function normaliser(et) {
  if (!et) return null;
  const texte = et.texte ?? et.text ?? et.label;
  const pos = et.pos ?? et.position ?? et.p ?? (typeof et.x === 'number' ? et : null);
  if (!texte || !pos) return null;
  const opacite = Number(et.opacite ?? et.opacity ?? et.vis ?? et.alpha ?? 1);
  const ancre = ['haut', 'bas', 'gauche', 'droite'].includes(et.ancre) ? et.ancre : 'haut';
  return { texte: String(texte), couleur: et.couleur ?? et.role ?? et.color ?? 'gris', pos, opacite, ancre };
}

const intersecte = (a, b, marge) => a.x < b.x + b.w + marge && b.x < a.x + a.w + marge && a.y < b.y + b.h + marge && b.y < a.y + a.h + marge;

/**
 * Pushes movable rectangles apart (and away from fixed ones), then keeps them in the frame.
 * Deterministic: fixed order, fixed iteration count.
 */
export function separer(rects, largeur, hauteur, marge) {
  for (let it = 0; it < 24; it += 1) {
    let bouge = false;
    for (let i = 0; i < rects.length; i += 1) {
      for (let j = i + 1; j < rects.length; j += 1) {
        const a = rects[i];
        const b = rects[j];
        if ((a.fixe && b.fixe) || !intersecte(a, b, marge)) continue;
        const dx = Math.min(a.x + a.w + marge - b.x, b.x + b.w + marge - a.x);
        const dy = Math.min(a.y + a.h + marge - b.y, b.y + b.h + marge - a.y);
        const ka = a.fixe ? 0 : b.fixe ? 1 : 0.5;
        const kb = 1 - ka;
        if (dy <= dx) {
          const s = a.y + a.h / 2 <= b.y + b.h / 2 ? -1 : 1;
          a.y += s * dy * ka;
          b.y -= s * dy * kb;
        } else {
          const s = a.x + a.w / 2 <= b.x + b.w / 2 ? -1 : 1;
          a.x += s * dx * ka;
          b.x -= s * dx * kb;
        }
        bouge = true;
      }
    }
    for (const r of rects) {
      if (r.fixe) continue;
      r.x = Math.min(largeur - marge - r.w, Math.max(marge, r.x));
      r.y = Math.min(hauteur - marge - r.h, Math.max(marge, r.y));
    }
    if (!bouge) break;
  }
  return rects;
}

function el(parent, tag, cls, texte) {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (texte) n.textContent = texte;
  parent.appendChild(n);
  return n;
}

const SVGNS = 'http://www.w3.org/2000/svg';
function svg(parent, tag, attrs) {
  const n = document.createElementNS(SVGNS, tag);
  for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, String(v));
  parent.appendChild(n);
  return n;
}

/** Final plate: the triangle at true proportions (km), blue then violet tip to tail, green from start. */
function creerPlaque(racine, d, e) {
  const k = d.km;
  const plaque = el(racine, 'div', 'plaque');
  el(plaque, 'p', 'plaque-regle', 'Vert = bleu, puis violet, bout à bout.');
  const zone = el(plaque, 'div', 'plaque-zone');
  // geometry in km (east, north) from etat() at the end of the film (nose turned into the wind)
  const A = e.air;
  const S = e.sol;
  const ext = Math.max(S.est, A.est) * 1.0;
  const U = 1000 / (ext * 1.06); // viewBox units per km
  const nordMax = Math.max(A.nord, 0);
  const nordMin = Math.min(S.nord, 0, A.nord + e.vent.nord);
  const bord = 34;
  const H = (nordMax - nordMin) * U + 2 * bord;
  const X = (est) => 30 + est * U;
  const Y = (nord) => bord + (nordMax - nord) * U;
  const s = svg(zone, 'svg', { viewBox: `0 0 1000 ${H.toFixed(1)}`, role: 'img', 'aria-label': 'Triangle des trois flèches' });
  const fleche = (x0, y0, x1, y1, couleur) => {
    const L = Math.hypot(x1 - x0, y1 - y0);
    const ux = (x1 - x0) / L;
    const uy = (y1 - y0) / L;
    const t = 26; // head length
    const xb = x1 - ux * t;
    const yb = y1 - uy * t;
    const trait = svg(s, 'line', {
      x1: x0, y1: y0, x2: xb, y2: yb, stroke: COULEUR[couleur], 'stroke-width': 7, 'stroke-linecap': 'round',
      pathLength: 1, 'stroke-dasharray': '1 1', 'stroke-dashoffset': 1,
    });
    const tete = svg(s, 'polygon', {
      points: `${x1},${y1} ${xb - uy * 13},${yb + ux * 13} ${xb + uy * 13},${yb - ux * 13}`, fill: COULEUR[couleur], opacity: 0,
    });
    return { trait, tete };
  };
  const O = [X(0), Y(0)];
  const P = [X(A.est), Y(A.nord)];
  const Q = [X(S.est), Y(S.nord)];
  const fl = {
    bleu: fleche(...O, ...P, 'bleu'),
    violet: fleche(...P, ...Q, 'violet'),
    vert: fleche(...O, ...Q, 'vert'),
  };
  const etiquette = (texte, couleur, x, y, ancre) => {
    const n = el(zone, 'span', 'plaque-etq', texte);
    n.style.color = teinte(couleur).texte;
    n.style.left = `${(x / 10).toFixed(2)}%`;
    n.style.top = `${((y / H) * 100).toFixed(2)}%`;
    n.style.transform = ancre;
    n.style.opacity = '0';
    return n;
  };
  const etq = {
    bleu: etiquette(`avion dans l’air : ${fr(k.avion_kmh, 0)} km`, 'bleu', (O[0] + P[0]) / 2, (O[1] + P[1]) / 2, 'translate(-50%, -170%)'),
    violet: etiquette(`vent : ${fr(k.vent_kmh, 0)} km`, 'violet', P[0], (P[1] + Q[1]) / 2, 'translate(-104%, -50%)'),
    vert: etiquette(`au sol : ${fr(k.bon.vitesse_sol_kmh, 0)} km`, 'vert', (O[0] + Q[0]) / 2, O[1], 'translate(-50%, 45%)'),
  };
  return {
    plaque,
    maj(t, vis) {
      plaque.style.opacity = vis.toFixed(3);
      plaque.style.visibility = vis > 0.001 ? 'visible' : 'hidden';
      // drawn early enough that the whole triangle and its three labels stay on screen about 1.4 s
      const kk = { bleu: smooth(prog(t, 55.3, 55.8)), violet: smooth(prog(t, 55.7, 56.2)), vert: smooth(prog(t, 56.1, 56.6)) };
      for (const [nom, v] of Object.entries(kk)) {
        fl[nom].trait.setAttribute('stroke-dashoffset', (1 - v).toFixed(4));
        fl[nom].tete.setAttribute('opacity', smooth((v - 0.9) / 0.1).toFixed(3));
        etq[nom].style.opacity = smooth((v - 0.6) / 0.4).toFixed(3);
      }
    },
  };
}

/**
 * @param {HTMLElement} racine film frame (position: relative)
 * @param {any} d data
 * @param {(t: number) => any} etatFin state at the end (for the triangle)
 */
export function creerTexte(racine, d, etatFin) {
  const couche = el(racine, 'div', 'textes');
  const lignes = legendes(d);
  const legende = el(couche, 'div', 'legende plaq');
  const etqs = Array.from({ length: MAX_ETIQUETTES }, () => el(couche, 'div', 'etq plaq'));
  const lettres = ['A', 'B', 'C'].map((l) => el(couche, 'div', 'lettre plaq', l));
  const heure = el(couche, 'div', 'heure plaq');
  const heureBarre = el(heure, 'span', 'heure-barre');
  const heureRemplie = el(heureBarre, 'i');
  el(heure, 'span', 'heure-texte', '1 heure');
  const plaque = creerPlaque(couche, d, etatFin);
  let dims = { largeur: 1, hauteur: 1, vertical: false, px: tailles(1280, false) };
  const mesures = new Map();

  function dimensionner(largeur, hauteur, vertical) {
    dims = { largeur, hauteur, vertical, px: tailles(largeur, vertical) };
    racine.style.setProperty('--t-legende', `${dims.px.legende.toFixed(2)}px`);
    racine.style.setProperty('--t-etiquette', `${dims.px.etiquette.toFixed(2)}px`);
    racine.style.setProperty('--t-source', `${dims.px.source.toFixed(2)}px`);
    racine.classList.toggle('vertical', vertical);
    mesures.clear();
  }

  function mesurer(n, cle) {
    const c = `${n.className}|${cle}`;
    if (!mesures.has(c)) mesures.set(c, { w: n.offsetWidth, h: n.offsetHeight });
    return mesures.get(c);
  }

  /** Caption: the one whose interval contains t; the final rule is carried by the plate. */
  function majLegende(t, e) {
    const l = lignes.find((x) => t >= x.t[0] && t < x.t[1]);
    const vis = l ? smooth(prog(t, l.t[0], l.t[0] + FONDU)) * (1 - smooth(prog(t, l.t[1] - FONDU, l.t[1]))) : 0;
    const surPlaque = l && e.plaque > 0.001 && l.texte === 'Vert = bleu, puis violet, bout à bout.';
    const v = surPlaque ? 0 : vis;
    if (l && legende.textContent !== l.texte) legende.textContent = l.texte;
    legende.style.opacity = v.toFixed(3);
    legende.style.visibility = v > 0.001 ? 'visible' : 'hidden';
    if (v <= 0.001) return null;
    return { x: legende.offsetLeft, y: legende.offsetTop, w: legende.offsetWidth, h: legende.offsetHeight, fixe: true };
  }

  /**
   * @param {number} t
   * @param {any} e etat(t, d)
   * @param {{ etiquettes: any[], projeter: (p: any) => ({x:number, y:number}|null),
   *   obstacles?: Array<{x:number, y:number, rayon:number}> }} ctx obstacles: drawn things in frame px
   *   (arrow tips, aeroplanes, balloon, rings) that no label may cover
   */
  function maj(t, e, ctx) {
    const rects = [];
    const zoneLegende = majLegende(t, e);
    if (zoneLegende) rects.push(zoneLegende);
    const marge = Math.round(dims.px.source * 0.7);
    // fixed squares (no node) around what the map draws: separer() moves the labels off them
    const cote0 = 1.6 * dims.px.etiquette;
    for (const o of ctx.obstacles || []) {
      const c = Math.max(cote0, 2 * (o.rayon || 0));
      rects.push({ x: o.x - c / 2, y: o.y - c / 2, w: c, h: c, fixe: true });
    }

    // letters A B C: shot 4; B again when the green arrow lands (shot 7)
    const visABC = smooth(prog(t, 14.6, 15.2)) * (1 - smooth(prog(t, 18.6, 19.0)));
    const visB7 = t >= 30 && t < 38 ? e.visVert * (1 - smooth(prog(t, 37.6, 38.0))) : 0;
    ['A', 'B', 'C'].forEach((nom, i) => {
      const v = nom === 'B' ? Math.max(visABC, visB7) : visABC;
      const n = lettres[i];
      // anchor just outside the ring (radius about 6 km), on its east side: right of it in the
      // landscape frame, above it in the phone frame (east is up there)
      const R = e.reponses[nom];
      const p = v > 0.001 ? ctx.projeter({ x: R.x + 6.5, y: 0, z: R.z }) : null;
      if (!p) { n.style.visibility = 'hidden'; return; }
      const m = mesurer(n, nom);
      // landscape: right of the ring; phone (route up the screen, rings side by side): above it
      const r = dims.vertical
        ? { x: p.x - m.w / 2, y: p.y - m.h - marge * 0.3, w: m.w, h: m.h, fixe: false, n, v }
        : { x: p.x + marge * 0.3, y: p.y - m.h / 2, w: m.w, h: m.h, fixe: false, n, v };
      rects.push(r);
    });

    // arrow labels from the map, at most three
    const liste = (ctx.etiquettes || []).map(normaliser).filter((x) => x && x.opacite > 0.001).slice(0, MAX_ETIQUETTES);
    etqs.forEach((n, i) => {
      const et = liste[i];
      const p = et ? ctx.projeter(et.pos) : null;
      if (!p) { n.style.visibility = 'hidden'; return; }
      if (n.textContent !== et.texte) n.textContent = et.texte;
      const c = teinte(et.couleur);
      n.style.color = c.texte;
      n.style.borderLeftColor = c.trait;
      const m = mesurer(n, et.texte);
      // `ancre`: side of the point where the box sits (box edge at the point)
      const g = marge * 0.5;
      const pos = {
        haut: [p.x - m.w / 2, p.y - m.h - g], bas: [p.x - m.w / 2, p.y + g],
        gauche: [p.x - m.w - g, p.y - m.h / 2], droite: [p.x + g, p.y - m.h / 2],
      }[et.ancre];
      rects.push({ x: pos[0], y: pos[1], w: m.w, h: m.h, fixe: false, n, v: et.opacite });
    });

    // "1 heure" bar, shot 2
    const visHeure = smooth(prog(t, 4.4, 4.8)) * (1 - smooth(prog(t, 8.7, 9.0)));
    heure.style.opacity = visHeure.toFixed(3);
    heure.style.visibility = visHeure > 0.001 ? 'visible' : 'hidden';
    heureRemplie.style.transform = `scaleX(${e.heureBallon.toFixed(4)})`;
    if (visHeure > 0.001) rects.push({ x: heure.offsetLeft, y: heure.offsetTop, w: heure.offsetWidth, h: heure.offsetHeight, fixe: true });

    separer(rects, dims.largeur, dims.hauteur, marge);
    for (const r of rects) {
      if (!r.n) continue;
      // whole pixels: sub-pixel placements rasterise the rounded corners differently between visits
      r.n.style.transform = `translate(${Math.round(r.x)}px, ${Math.round(r.y)}px)`;
      r.n.style.opacity = r.v.toFixed(3);
      r.n.style.visibility = 'visible';
    }

    plaque.maj(t, e.plaque);
  }

  return { maj, dimensionner, couche };
}
