// Copyright: Your Name. Apache 2.0
// Parts of the procedural Cessna 172S (« Vent de travers », v2), built in the MODEL FRAME
// (metres; x = right wing, y = up, z = toward the tail; nose along -z). Static parts are returned
// grouped by material key so avion.js can merge them; moving parts come with their pivot.

import {
  maillage, fermerBout, boucle, peau, fA, fB, fC, FUS, ouvertures, epaisseur,
  AILE, sectionAile, stationsBout, STAB, sectionStab, DERIVE, sectionDerive,
} from './avion_formes.js';
import { uvFuselage, uvAile } from './avion_peau.js';

const B = globalThis.BABYLON;
const V = (x, y, z) => new B.Vector3(x, y, z);
const lerp = (a, b, k) => a + (b - a) * k;
const plage = (a, b, pas) => { const n = Math.max(1, Math.round((b - a) / pas)), out = []; for (let i = 0; i <= n; i++) out.push(lerp(a, b, i / n)); return out; };
const miroir = (rangs) => rangs.map((r) => r.map((p) => [-p[0], p[1], p[2]]));

/** Material keys of the static parts. */
export const CLES = ['peau', 'aile', 'peinture', 'bleu', 'vitre', 'sombre', 'pneu', 'metal', 'interieur', 'paroi', 'siege'];

/**
 * Builds every part.
 * @param {any} scene
 * @param {{fuselageN?:number}} o tessellation around the fuselage
 */
export function construirePieces(scene, o = {}) {
  const P = Object.fromEntries(CLES.map((k) => [k, []]));
  const add = (k, m) => { P[k].push(m); return m; };
  const tube = (k, pts, r, tess = 12, cap = true) => add(k, B.MeshBuilder.CreateTube('avion-tube', { path: pts, radius: r, tessellation: tess, cap: cap ? B.Mesh.CAP_ALL : B.Mesh.NO_CAP }, scene));
  const NT = o.fuselageN || 144;
  const ths = Array.from({ length: NT }, (_, j) => -Math.PI / 2 + (2 * Math.PI * j) / NT);
  const centreFus = (z) => [0, fC(z), z];

  /* fuselage skin: one smooth loft, seam under the belly, uv = (length, angle) */
  const zf = [FUS.z0, ...plage(-2.93, 4.82, 0.03), FUS.z1];
  const rangsFus = zf.map((z, i) => (i === 0 || i === zf.length - 1 ? ths.map(() => centreFus(z)) : ths.map((th) => peau(z, th))));
  const uvF = (zl) => (i, j) => [uvFuselage(zl[i], 0)[0], j / NT];
  add('peau', maillage(scene, 'avion-fuselage', rangsFus, { fermer: true, uv: uvF(zf), centre: (i) => centreFus(zf[i]) }));

  /* cabin liner (inside, same window cut-outs), bulkheads, glazing, seals */
  const zl = plage(-1.8, 1.65, 0.03);
  add('paroi', maillage(scene, 'avion-paroi', zl.map((z) => ths.map((th) => peau(z, th, -0.025))), { fermer: true, uv: uvF(zl), centre: (i) => centreFus(zl[i]), inverser: true }));
  for (const z of [-1.8, 1.65]) {
    const anneau = ths.map((th) => peau(z, th, -0.025));
    add('interieur', maillage(scene, 'avion-cloison', [anneau, anneau.map(() => centreFus(z))], { fermer: true }));
  }
  for (const ouv of ouvertures()) {
    if (ouv.kind === 'vitre') {
      let z0 = Infinity, z1 = -Infinity, t0 = Infinity, t1 = -Infinity;
      for (const [z, th] of ouv.pts) { z0 = Math.min(z0, z); z1 = Math.max(z1, z); t0 = Math.min(t0, th); t1 = Math.max(t1, th); }
      const zz = plage(z0 - 0.03, z1 + 0.03, 0.03), tt = plage(t0 - 0.05, t1 + 0.05, 0.03);
      add('vitre', maillage(scene, 'avion-vitre', zz.map((z) => tt.map((th) => peau(z, th, -0.006))), { centre: (i) => centreFus(zz[i]) }));
    }
    const pts = ouv.pts.map(([z, th]) => V(...peau(z, th, ouv.kind === 'vitre' ? 0.002 : 0.0005)));
    if (ouv.kind === 'vitre') tube('sombre', [...pts, pts[0]], 0.009, 6, false);
  }
  for (const s of [1, -1]) tube('metal', [V(...peau(-0.36, s > 0 ? 0.16 : Math.PI - 0.16, 0.014)), V(...peau(-0.22, s > 0 ? 0.16 : Math.PI - 0.16, 0.014))], 0.011, 10); // door handles

  /* wing: root (full chord), box (ahead of the flaps), rounded tip, flaps and ailerons with gaps */
  const plein = boucle('complet', { n: 34 }), avant = boucle('avant', { n: 30, coupe: 0.72 }), arr = boucle('arriere', { n: 16, coupe: 0.745 });
  const volets = [];
  const ailePiece = (nom, xs, loop, cle, caps) => {
    let rangs = xs.map((x) => sectionAile(x, loop.pts));
    if (caps.includes('debut')) rangs = fermerBout(rangs, true);
    if (caps.includes('fin')) rangs = fermerBout(rangs, false);
    const m = loop.pts.length;
    const uv = (i, j, p) => uvAile(p[0], loop.pts[j % m].v);
    return { rangs, uv, cle, nom };
  };
  const piecesAile = [
    ailePiece('avion-aile-racine', plage(0, 0.6, 0.15), plein, 'aile', ['fin']),
    ailePiece('avion-aile-caisson', plage(0.6, 5.24, 0.08), avant, 'aile', []),
    ailePiece('avion-aile-bout', stationsBout(5.24, AILE.rond, AILE.bout, 14), plein, 'aile', ['debut']),
  ];
  const charniere = (x, h) => sectionAile(x, [{ c: h.c, y: h.y, v: 0.5 }])[0];
  for (const s of [1, -1]) {
    for (const pc of piecesAile) add(pc.cle, maillage(scene, pc.nom, s > 0 ? pc.rangs : miroir(pc.rangs), { fermer: true, uv: pc.uv }));
    for (const [nom, x0, x1] of [['volet', 0.62, 3.33], ['aileron', 3.37, 5.22]]) {
      const pc = ailePiece(`avion-${nom}`, plage(x0, x1, 0.1), arr, 'peinture', ['debut', 'fin']);
      const rangs = s > 0 ? pc.rangs : miroir(pc.rangs);
      const a = charniere(x0, arr.charniere), b = charniere(x1, arr.charniere);
      if (s < 0) { a[0] = -a[0]; b[0] = -b[0]; }
      const pivot = V(...a), axe = V(b[0] - a[0], b[1] - a[1], b[2] - a[2]).normalize();
      if (axe.x < 0) axe.scaleInPlace(-1); // positive angle = trailing edge down on both sides
      const mesh = maillage(scene, pc.nom, rangs, { fermer: true });
      volets.push({ type: nom, cote: s, mesh, pivot, axe });
    }
    // strut with elliptic section and end cuffs
    const a = V(s * 0.56, -0.42, -0.55), b = V(s * 2.6, sectionAile(2.6, [{ c: 0.31, y: -0.06, v: 1 }])[0][1] - 0.01, -0.55);
    const dir = b.subtract(a);
    const hauban = B.MeshBuilder.CreateCylinder('avion-hauban', { height: dir.length(), diameter: 0.055, tessellation: 24 }, scene);
    hauban.scaling.z = 2.1;
    hauban.rotation.z = Math.atan2(-dir.x, dir.y);
    hauban.position = a.add(b).scale(0.5);
    add('peinture', hauban);
    for (const [p, d] of [[a, 0.13], [b, 0.11]]) {
      const cuff = B.MeshBuilder.CreateSphere('avion-manchon', { diameter: d, segments: 16 }, scene);
      cuff.scaling.set(0.8, 0.7, 2.4);
      cuff.position = p.clone();
      add('peinture', cuff);
    }
  }

  /* tailplane: fixed part, rounded tip, elevator halves on a common hinge */
  const sPlein = boucle('complet', { n: 24, m: 0, ep: 0.09 }), sAvant = boucle('avant', { n: 20, m: 0, ep: 0.09, coupe: 0.6 });
  const sArr = boucle('arriere', { n: 12, m: 0, ep: 0.09, coupe: 0.62 });
  const profondeur = [];
  for (const s of [1, -1]) {
    const f = (r) => (s > 0 ? r : miroir(r));
    add('peinture', maillage(scene, 'avion-stab', f(plage(0, STAB.rond, 0.08).map((x) => sectionStab(x, sAvant.pts))), { fermer: true }));
    add('peinture', maillage(scene, 'avion-stab-bout', f(fermerBout(stationsBout(STAB.rond - 0.02, STAB.rond, STAB.bout, 10).map((x) => sectionStab(x, sPlein.pts)), true)), { fermer: true }));
    let r = plage(0, STAB.rond - 0.03, 0.08).map((x) => sectionStab(x, sArr.pts));
    r = fermerBout(fermerBout(r, true), false);
    profondeur.push(maillage(scene, 'avion-profondeur', f(r), { fermer: true }));
  }
  const h0 = sectionStab(0, [{ c: sArr.charniere.c, y: 0, v: 0.5 }])[0];
  const pivotProf = V(...h0);

  /* fin with dorsal fillet, blue band, rudder hinge groove */
  const fPlein = boucle('complet', { n: 26, m: 0, ep: 1 });
  const ys = stationsBout(DERIVE.y0, DERIVE.rond, DERIVE.haut, 9);
  add('peinture', maillage(scene, 'avion-derive', ys.map((y) => sectionDerive(y, fPlein.pts)), { fermer: true }));
  for (const s of [1, -1]) {
    const cote = [];
    for (let k = 0; k <= 24; k++) { const c = k / 24; cote.push({ c, y: s * epaisseur(c, 1), v: 0 }); }
    const yb = plage(1.08, 1.17, 0.015);
    add('bleu', maillage(scene, 'avion-bande-derive', yb.map((y) => sectionDerive(y, cote, 0.0025)), { centre: (i) => [0, yb[i], 4.4] }));
    tube('sombre', [V(s * 0.03, 0.55, 4.62), V(s * 0.017, 1.42, 4.66)], 0.005, 6);
  }

  /* cowling details: inlets, lower air exit, exhaust */
  for (const sx of [-1, 1]) {
    const entree = B.MeshBuilder.CreateDisc('avion-entree', { radius: 0.1, tessellation: 40, sideOrientation: B.Mesh.DOUBLESIDE }, scene);
    entree.scaling.y = 0.6;
    entree.position.set(sx * 0.26, -0.03, -2.92);
    add('sombre', entree);
  }
  const sortie = B.MeshBuilder.CreateBox('avion-sortie', { width: 0.5, height: 0.05, depth: 0.14 }, scene);
  sortie.position.set(0, fC(-1.95) - fB(-1.95) + 0.012, -1.95);
  add('sombre', sortie);
  const echap = [V(0.24, -0.4, -2.1), V(0.27, -0.66, -1.98)];
  add('metal', B.MeshBuilder.CreateTube('avion-echappement', { path: echap, radius: 0.034, tessellation: 20, cap: B.Mesh.NO_CAP, sideOrientation: B.Mesh.DOUBLESIDE }, scene));

  /* landing gear: main group (legs, wheels, fairings) and nose group (piston, wheel) */
  const lathe = (nom, profil, tess = 48) => B.MeshBuilder.CreateLathe(nom, { shape: profil, tessellation: tess, cap: B.Mesh.NO_CAP }, scene);
  const train = { principal: [], avant: [] };
  const carenage = (groupe, longueur, rmax, cx, cy, cz, largeur) => {
    const profil = [];
    for (let i = 0; i <= 24; i++) {
      const u = i / 24;
      const r = rmax * (u < 0.35 ? Math.sqrt(1 - ((0.35 - u) / 0.35) ** 2) : Math.sqrt(Math.max(0, 1 - ((u - 0.35) / 0.65) ** 1.6)));
      profil.push(V(Math.max(r, 0.0005), u * longueur, 0));
    }
    const m = lathe('avion-carenage', profil);
    m.rotation.x = Math.PI / 2;
    m.scaling.set(largeur, 1, 0.75);
    m.position.set(cx, cy, cz - 0.35 * longueur);
    groupe.push(['peinture', m]);
  };
  const roue = (groupe, rayon, x, y, z) => {
    const pneu = B.MeshBuilder.CreateTorus('avion-pneu', { diameter: 2 * (rayon - 0.055), thickness: 0.11, tessellation: 48 }, scene);
    pneu.rotation.z = Math.PI / 2;
    pneu.scaling.set(1, 1.15, 1);
    pneu.position.set(x, y, z);
    groupe.push(['pneu', pneu]);
    const moyeu = B.MeshBuilder.CreateCylinder('avion-moyeu', { diameter: 2 * (rayon - 0.09), height: 0.1, tessellation: 32 }, scene);
    moyeu.rotation.z = Math.PI / 2;
    moyeu.position.set(x, y, z);
    groupe.push(['metal', moyeu]);
  };
  for (const sx of [1, -1]) {
    const jambe = B.MeshBuilder.CreateTube('avion-jambe', {
      path: [V(sx * 0.4, -0.57, 0.05), V(sx * 0.8, -0.8, 0.09), V(sx * 1.17, -0.99, 0.12)],
      radiusFunction: (i) => [0.042, 0.035, 0.028][i], tessellation: 16, cap: B.Mesh.CAP_ALL,
    }, scene);
    train.principal.push(['peinture', jambe]);
    roue(train.principal, 0.27, sx * 1.27, -1.0, 0.12);
    carenage(train.principal, 1.0, 0.26, sx * 1.27, -0.92, 0.12, 0.45);
  }
  tube('metal', [V(0, -0.4, -2.3), V(0, -0.8, -2.36)], 0.045, 20);
  train.avant.push(['metal', B.MeshBuilder.CreateTube('avion-piston', { path: [V(0, -0.7, -2.345), V(0, -1.05, -2.42)], radius: 0.03, tessellation: 16, cap: B.Mesh.CAP_ALL }, scene)]);
  roue(train.avant, 0.22, 0, -1.05, -2.42);
  carenage(train.avant, 0.8, 0.21, 0, -0.98, -2.42, 0.4);

  /* simple interior: floor, seats, panel, glare shield, yokes, gauges */
  const boite = (cle, w, h, d, x, y, z, rx = 0) => {
    const b = B.MeshBuilder.CreateBox('avion-int', { width: w, height: h, depth: d }, scene);
    b.position.set(x, y, z); b.rotation.x = rx;
    return add(cle, b);
  };
  boite('interieur', 1.1, 0.03, 3.2, 0, -0.33, -0.1);
  for (const sx of [-0.27, 0.27]) {
    boite('siege', 0.46, 0.13, 0.5, sx, -0.18, -0.42);
    boite('siege', 0.46, 0.66, 0.11, sx, 0.2, -0.13, -0.22);
    boite('siege', 0.3, 0.12, 0.08, sx, 0.6, -0.04, -0.22); // headrest
    tube('interieur', [V(sx, 0.08, -1.44), V(sx, 0.08, -1.2)], 0.014, 8);
    tube('interieur', [V(sx - 0.13, 0.12, -1.2), V(sx, 0.08, -1.2), V(sx + 0.13, 0.12, -1.2)], 0.014, 8);
  }
  boite('siege', 1.0, 0.13, 0.5, 0, -0.18, 0.45);
  boite('siege', 1.0, 0.62, 0.11, 0, 0.2, 0.74, -0.2);
  boite('interieur', 1.08, 0.32, 0.12, 0, 0.18, -1.5);
  boite('interieur', 1.08, 0.035, 0.26, 0, 0.35, -1.45);
  const cadrans = [];
  for (const gx of [-0.42, -0.31, -0.2, 0.2, 0.31]) for (const gy of [0.24, 0.13]) {
    const g = B.MeshBuilder.CreateDisc('avion-cadran', { radius: 0.04, tessellation: 24, sideOrientation: B.Mesh.DOUBLESIDE }, scene);
    g.position.set(gx, gy, -1.437);
    cadrans.push(g);
  }

  /* spinner */
  const prof = [];
  for (let i = 0; i <= 24; i++) { const u = i / 24; prof.push(V(Math.max(0.0005, 0.21 * Math.sqrt(Math.max(0, 1 - u ** 1.7))), 0.36 * u, 0)); }
  const cone = lathe('avion-cone', prof, 64);
  cone.rotation.x = -Math.PI / 2; // lathe axis +y → forward (-z)
  const bague = B.MeshBuilder.CreateTorus('avion-bague', { diameter: 0.41, thickness: 0.026, tessellation: 64 }, scene);
  bague.rotation.x = Math.PI / 2;
  bague.position.z = -0.02;

  /* light positions (model frame) */
  const nav = sectionAile(5.48, [{ c: 0.1, y: 0, v: 0.5 }])[0];
  const strobe = sectionAile(5.48, [{ c: 0.45, y: 0, v: 0.5 }])[0];
  const phare = sectionAile(1.9, [{ c: 0, y: 0, v: 0.5 }])[0];
  const feux = {
    navG: V(-nav[0] - 0.035, nav[1], nav[2]), navD: V(nav[0] + 0.035, nav[1], nav[2]),
    strobeG: V(-strobe[0] - 0.03, strobe[1], strobe[2]), strobeD: V(strobe[0] + 0.03, strobe[1], strobe[2]),
    queue: V(0, fC(4.82) + 0.01, 4.86), balise: V(0, DERIVE.haut + 0.01, 4.6), phare: V(-phare[0], phare[1], phare[2] + 0.008),
  };

  return { P, volets, profondeur, pivotProf, train, cadrans, cone, bague, feux, rotor: V(0, -0.08, -2.95) };
}

/** Top-view outline of the aeroplane, model frame, as [x, z] (closed, counter-clockwise from the nose). */
export function contourDessus() {
  const droite = [];
  for (let i = 24; i >= 0; i--) { const u = i / 24; droite.push([0.21 * Math.sqrt(Math.max(0, 1 - u ** 1.7)), -2.95 - 0.36 * u]); }
  for (const z of plage(-2.93, -1.05, 0.06)) droite.push([fA(z), z]);
  const xsB = stationsBout(fA(-1.05), AILE.rond, AILE.bout, 12);
  for (const x of xsB) droite.push([x, sectionAile(x, [{ c: 0, y: 0, v: 0.5 }])[0][2]]);
  for (const x of [...xsB].reverse()) droite.push([x, sectionAile(x, [{ c: 1, y: 0, v: 0.5 }])[0][2]]);
  for (const z of plage(AILE.bf + 0.01, 3.86, 0.1)) droite.push([fA(z), z]);
  const xsS = stationsBout(fA(3.88), STAB.rond, STAB.bout, 10);
  for (const x of xsS) droite.push([x, sectionStab(x, [{ c: 0, y: 0, v: 0.5 }])[0][2]]);
  for (const x of [...xsS].reverse()) droite.push([x, sectionStab(x, [{ c: 1, y: 0, v: 0.5 }])[0][2]]);
  droite.push([0, sectionStab(0, [{ c: 1, y: 0, v: 0.5 }])[0][2]]);
  const gauche = droite.slice(1, -1).reverse().map(([x, z]) => [-x, z]);
  const tout = [...droite, ...gauche];
  return tout.filter((p, i) => i === 0 || Math.hypot(p[0] - tout[i - 1][0], p[1] - tout[i - 1][1]) > 1e-5);
}
