// Copyright: Your Name. Apache 2.0
// Scene CARTE (shots 4-9): the proof, seen from straight above on a fixed map, north up.
// 1 unit = 1 km, +x east, -z north, +y up. Rendering is a pure function of the film time t:
// maj(t, e) sets every uniform from etat(t, d); nothing accumulates between frames.
// The whole picture is two quads with fwidth-filtered signed-distance shaders (see carte_glsl.js),
// so edges are anti-aliased analytically at any render size, without MSAA or FXAA.

import { COULEUR, PLANS, fr, prog, smooth, rad, clamp01 } from './communs.js';
import { VERTEX, SOL, DESSIN } from './carte_glsl.js';

const B = () => globalThis.BABYLON;

/** Frame of the fixed camera (km): x from depart margin to beyond the naive point and labels. */
const CADRE = Object.freeze({ gauche: -136, droite: 162, centreZ: 1 });

const hex3 = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16) / 255);
const melange = (a, b, k) => a.map((v, i) => v + (b[i] - v) * k);
const versHex = (c) => '#' + c.map((v) => Math.round(clamp01(v) * 255).toString(16).padStart(2, '0')).join('');
const RGB = Object.freeze(Object.fromEntries(Object.entries(COULEUR).map(([k, v]) => [k, hex3(v)])));

/** Atlas of the few fixed words drawn on the map (system font, no font file). */
function creerAtlas(scene) {
  const BJ = B();
  const tex = new BJ.DynamicTexture('carteAtlas', { width: 1024, height: 512 }, scene, true, BJ.Texture.TRILINEAR_SAMPLINGMODE);
  const ctx = tex.getContext();
  ctx.clearRect(0, 0, 1024, 512);
  ctx.fillStyle = '#ffffff';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  const police = (px) => `600 ${px}px "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`;
  ctx.font = police(178);
  ['A', 'B', 'C', 'N'].forEach((l, i) => ctx.fillText(l, 128 + 256 * i, 140));
  ctx.font = police(150);
  ctx.fillText('50 km', 256, 384);
  tex.update(true);
  tex.hasAlpha = true;
  tex.wrapU = BJ.Texture.CLAMP_ADDRESSMODE;
  tex.wrapV = BJ.Texture.CLAMP_ADDRESSMODE;
  tex.anisotropicFilteringLevel = 8;
  return tex;
}

const UNIFORMES = [
  'uFl0', 'uFl1', 'uFl2', 'uCo0', 'uCo1', 'uCo2', 'uLigne', 'uDivers', 'uRA', 'uRB', 'uRC', 'uLet',
  'uLien0', 'uLien1', 'uDivers2', 'uTrace', 'uEcart', 'uArc', 'uCroix', 'uBallon', 'uFant', 'uAvion',
  'uNord', 'uEch', 'uEp', 'uBleu', 'uViolet', 'uVert', 'uOrange', 'uRouge', 'uGris',
];

/**
 * Builds the CARTE scene.
 * @param {any} engine Babylon engine created by the director
 * @param {any} d data from chargerDonnees()
 * @returns {{ scene: any, camera: any, maj: (t: number, e: any) => void, etiquettes: (e: any) => Array<{x:number,y:number,z:number,texte:string,couleur:string,ancre:string}> }}
 */
export function creerCarte(engine, d) {
  const BJ = B();
  const k = d.km;
  const scene = new BJ.Scene(engine);
  scene.useRightHandedSystem = true;
  scene.clearColor = new BJ.Color4(0.07, 0.078, 0.084, 1);
  scene.skipPointerMovePicking = true;

  // --- fixed top-down orthographic camera, north (-z) at the top of the screen
  const cx = (CADRE.gauche + CADRE.droite) / 2;
  const camera = new BJ.TargetCamera('carteCam', new BJ.Vector3(cx, 400, CADRE.centreZ), scene);
  camera.upVector = new BJ.Vector3(0, 0, -1);
  camera.setTarget(new BJ.Vector3(cx, 0, CADRE.centreZ));
  camera.mode = BJ.Camera.ORTHOGRAPHIC_CAMERA;
  camera.minZ = 1;
  camera.maxZ = 1000;
  const demiL = (CADRE.droite - CADRE.gauche) / 2;
  let demiH = demiL * 9 / 16; // half extent across the route (along z), km
  let vertical = false; // phone layout: east up the screen, so the route runs upwards
  const vue = { cx, demiX: demiL }; // visible span along x (east), for the map vignette
  const cadrer = () => {
    const w = engine.getRenderWidth(); const h = engine.getRenderHeight();
    const ok = h > 0 && w > 0;
    if (!vertical) {
      demiH = demiL * (ok ? h / w : 9 / 16);
      camera.orthoLeft = -demiL; camera.orthoRight = demiL;
      camera.orthoTop = demiH; camera.orthoBottom = -demiH;
      vue.cx = cx; vue.demiX = demiL;
    } else {
      // the route fills the upper 72 % of the frame; the captions own the lower part
      // tighter span along the route than in landscape (+12 % scale); the crossed point of shot 8
      // (x = 134.6 km) and its cross (6 km) stay inside the top edge
      const haut = CADRE.droite - 16;
      const bas = haut - (CADRE.droite - 22 - (CADRE.gauche + 10)) / 0.72;
      vue.cx = (haut + bas) / 2; vue.demiX = (haut - bas) / 2;
      demiH = vue.demiX * (ok ? w / h : 9 / 16);
      camera.orthoLeft = -demiH; camera.orthoRight = demiH;
      camera.orthoTop = haut - cx; camera.orthoBottom = bas - cx;
    }
  };
  /** Screen side for a world direction (dx east, dz south) — follows the map rotation. */
  const coteEcran = (dx, dz) => {
    if (Math.abs(dx) > Math.abs(dz)) return vertical ? (dx > 0 ? 'haut' : 'bas') : (dx > 0 ? 'droite' : 'gauche');
    return vertical ? (dz > 0 ? 'droite' : 'gauche') : (dz > 0 ? 'bas' : 'haut');
  };
  /** Phone layout: the camera turns a quarter turn (east up, north to the left). */
  function setVertical(v) {
    vertical = !!v;
    camera.upVector = vertical ? new BJ.Vector3(1, 0, 0) : new BJ.Vector3(0, 0, -1);
    camera.setTarget(new BJ.Vector3(cx, 0, CADRE.centreZ));
    cadrer();
  }
  cadrer();

  BJ.Effect.ShadersStore.carteVertexShader = VERTEX;
  BJ.Effect.ShadersStore.carteSolFragmentShader = SOL;
  BJ.Effect.ShadersStore.carteDessinFragmentShader = DESSIN;

  // --- the map (static pattern; only the vignette frame uniform changes with the aspect ratio)
  const sol = BJ.MeshBuilder.CreateGround('carteSol', { width: 1400, height: 1000, subdivisions: 1 }, scene);
  sol.position.x = cx;
  const matSol = new BJ.ShaderMaterial('carteSol', scene, { vertex: 'carte', fragment: 'carteSol' }, {
    attributes: ['position'], uniforms: ['world', 'viewProjection', 'uCadre'],
  });
  matSol.backFaceCulling = false;
  sol.material = matSol;
  sol.isPickable = false;

  // --- every drawn element, in one premultiplied-alpha quad just above the map
  const dessin = BJ.MeshBuilder.CreateGround('carteDessin', { width: 1400, height: 1000, subdivisions: 1 }, scene);
  dessin.position.set(cx, 0.5, 0);
  const mat = new BJ.ShaderMaterial('carteDessin', scene, { vertex: 'carte', fragment: 'carteDessin' }, {
    attributes: ['position'], uniforms: ['world', 'viewProjection', ...UNIFORMES], samplers: ['atlas'], needAlphaBlending: true,
  });
  mat.backFaceCulling = false;
  mat.disableDepthWrite = true;
  mat.alphaMode = BJ.Constants.ALPHA_PREMULTIPLIED_PORTERDUFF;
  mat.setTexture('atlas', creerAtlas(scene));
  for (const [n, c] of [['uBleu', 'bleu'], ['uViolet', 'violet'], ['uVert', 'vert'], ['uOrange', 'orange'], ['uRouge', 'rouge'], ['uGris', 'gris']]) {
    mat.setVector3(n, new BJ.Vector3(...RGB[c]));
  }
  dessin.material = mat;
  dessin.isPickable = false;
  dessin.renderingGroupId = 1;

  const v4 = (n, a, b, c, dd) => mat.setVector4(n, new BJ.Vector4(a, b, c, dd));
  const seg = (n, a, b) => v4(n, a.x, a.z, b.x, b.z);
  const coul = (n, rgb, a) => v4(n, rgb[0], rgb[1], rgb[2], a);

  /**
   * Sets the whole picture for film time t.
   * @param {number} t film time (s)
   * @param {any} e etat(t, d)
   */
  function maj(t, e) {
    cadrer();
    matSol.setVector4('uCadre', new BJ.Vector4(vue.cx, CADRE.centreZ, vue.demiX, demiH));
    v4('uEp', vertical ? 1.4 : 1, smooth(prog(t, 43.0, 43.8)), 0, 0); // stroke widths (thicker on the phone frame); runway grows in shot 9
    const g = vues(t, e);

    // furniture: intended line, runway, north mark (top right), scale bar (bottom left)
    seg('uLigne', e.depart, e.piste);
    v4('uDivers', 1, g.arrivee, 0.5 + 0.5 * Math.cos(Math.max(0, t - 49) * 5), t < PLANS.ideeFausse.t[0] ? 1 : 0);
    // (hidden in the phone layout, where their words would be turned sideways)
    v4('uNord', cx + demiL - 12, CADRE.centreZ - demiH + 16, vertical ? 0 : 1, 0);
    v4('uEch', cx - demiL + 12, CADRE.centreZ - demiH + 19, vertical ? 0 : 1, 0); // top left: the captions own the bottom

    // answer rings A, B, C and their letters
    const r = e.reponses;
    v4('uRA', r.A.x, r.A.z, g.ringAC, 0);
    v4('uRB', r.B.x, r.B.z, g.ringB, g.vertB);
    v4('uRC', r.C.x, r.C.z, g.ringAC, 0);
    // the letters themselves are HTML plates drawn by the director (texte.js): only B's ring pulse here
    v4('uLet', 0, 0, 0, Math.sin(Math.PI * prog(t, 37.2, 38.0)));

    // arrows: shot 8 lays the violet one flat on the straight line and turns the pair red
    const [vq, vt] = flecheVentPosee(e);
    seg('uFl0', e.flecheAir[0], e.flecheAir[1]);
    seg('uFl1', vq, vt);
    seg('uFl2', e.flecheSol[0], e.flecheSol[1]);
    coul('uCo0', melange(RGB.bleu, RGB.rouge, e.aPlat), e.hAir > 0 ? 1 : 0);
    coul('uCo1', melange(RGB.violet, RGB.rouge, e.aPlat), e.hVent > 0 ? 1 : 0);
    coul('uCo2', RGB.vert, e.visVert * (1 - 0.6 * e.aPlat));
    v4('uCroix', e.pointNaif.x, e.pointNaif.z, e.barre, 0);

    // replay of shot 7: trail of the real aeroplane, dashed parallelogram ghost / balloon / real
    seg('uTrace', e.depart, e.posAvion);
    seg('uLien0', e.posFantome, e.posAvion);
    seg('uLien1', e.posBallon, e.posAvion);
    v4('uDivers2', g.liens, g.trace, g.ecart, 0);

    // shot 9: orange arc of the turn, offset between the green tip and the runway line
    v4('uArc', e.depart.x, e.depart.z, rad(90 - e.capDeg), g.arc);
    const bout = e.flecheSol[1];
    v4('uEcart', bout.x, bout.z, bout.x, e.piste.z);

    // the three things
    v4('uBallon', e.posBallon.x, e.posBallon.z, g.ballon, 0);
    v4('uFant', e.posFantome.x, e.posFantome.z, rad(e.capDeg), g.fantome);
    v4('uAvion', e.posAvion.x, e.posAvion.z, rad(e.capDeg), g.avion);
  }

  /** Visibility of each element at time t (all pure functions of t and e). */
  function vues(t, e) {
    const sortie = 1 - smooth(prog(t, 38.0, 38.5)); // ghost, balloon, links leave at the start of shot 8
    const confirme = smooth(prog(t, 37.2, 37.8));
    const attenue = 1 - 0.45 * smooth(prog(t, 19.0, 19.8)) + 0.45 * confirme;
    const sortieB = 1 - smooth(prog(t, 43.0, 44.5));
    const tour9 = t >= PLANS.correction.t[0] ? 1 : 0;
    return {
      ringAC: Math.min(1, attenue) * (1 - confirme),
      ringB: Math.min(1, attenue) * sortieB * (1 - 0.35 * e.aPlat),
      vertB: confirme,
      avion: t < 19.8 ? 1 - smooth(prog(t, 19.0, 19.8)) : smooth(prog(t, 34.4, 34.8)),
      fantome: smooth(prog(t, 19.0, 19.8)) * sortie,
      ballon: smooth(prog(t, 25.0, 25.6)) * sortie,
      liens: smooth(prog(t, 34.5, 35.0)) * sortie,
      trace: (e.hSol > 0 ? 1 : 0) * sortie,
      arc: tour9 * smooth(prog(t, 43.6, 44.2)),
      ecart: tour9 * smooth(prog(t, 43.4, 44.0)) * clamp01(Math.abs(e.ecartKm) / 0.8),
      arrivee: tour9 * clamp01(1 - Math.abs(e.ecartKm) / 3),
    };
  }

  /** Violet arrow, rotated flat onto the straight line by e.aPlat (shot 8), length kept. */
  function flecheVentPosee(e) {
    // The tail follows the CURRENT blue tip (identical to etat() whenever hAir = 1; during the
    // replay of shot 7 etat() keeps it at the full blue tip while the blue arrow regrows).
    const [a0, a1] = e.flecheAir;
    const [v0, v1] = e.flecheVent;
    const q = e.glisse > 0 ? { x: a0.x + (a1.x - a0.x) * e.glisse, z: a0.z + (a1.z - a0.z) * e.glisse } : v0;
    const b = { x: q.x + v1.x - v0.x, z: q.z + v1.z - v0.z };
    if (e.aPlat <= 0) return [q, b];
    const dx = b.x - q.x; const dz = b.z - q.z;
    const L = Math.hypot(dx, dz);
    const ang = Math.atan2(dz, dx); // world angle; east = 0
    const a = ang * (1 - e.aPlat);
    return [q, { x: q.x + L * Math.cos(a), z: q.z + L * Math.sin(a) }];
  }

  /** Label placed at the middle of an arrow, offset perpendicular towards side (unit vector). */
  function surFleche(a, b, cote, texte, couleur, ecart = 6.5) {
    const mx = (a.x + b.x) / 2; const mz = (a.z + b.z) / 2;
    const ux = b.x - a.x; const uz = b.z - a.z; const L = Math.hypot(ux, uz) || 1;
    let nx = -uz / L; let nz = ux / L;
    if (nx * cote.x + nz * cote.z < 0) { nx = -nx; nz = -nz; }
    const ancre = coteEcran(nx, nz);
    return { x: mx + nx * ecart, y: 0, z: mz + nz * ecart, texte, couleur, ancre };
  }

  /**
   * HTML labels for the director (CARTE coordinates, at most 3). `ancre` says on which side of the
   * point the text box sits: 'haut' above, 'bas' below, 'gauche' left, 'droite' right (box edge at the point).
   * @param {any} e etat(t, d)
   */
  function etiquettes(e) {
    const t = e.t;
    const out = [];
    if (t < PLANS.airSeul.t[0] || t >= PLANS.pose.t[0]) return out;
    const huit = e.plan === 'ideeFausse';
    const [vq, vt] = flecheVentPosee(e);
    // centroid of the triangle as drawn now: labels go to the side away from it (the outer side)
    const s = e.flecheSol[1]; const a = e.flecheAir[0]; const bAir = e.flecheAir[1];
    const g = { x: (a.x + bAir.x + vt.x) / 3, z: (a.z + bAir.z + vt.z) / 3 };
    const dehors = (p, q) => ({ x: (p.x + q.x) / 2 - g.x, z: (p.z + q.z) / 2 - g.z });
    const nord = { x: 0, z: -1 };

    // replay of shot 7: the arrows regrow; no running numbers, the full lengths were already given
    if (e.plan === 'boutABout' && t >= 34.4 && e.hSol < 1) return out;
    // shot 7 once the green arrow comes: only its length (blue and violet were given in shots 5-6)
    const seulVert = e.plan === 'boutABout' && t >= 33.0;
    // phone frame: the violet arrow is narrower than its label; the label sits beside the arrival
    const violetDehors = vertical && !huit && e.plan !== 'ventSeul';
    if (e.hAir > 0.02 && !seulVert) {
      const c = versHex(melange(RGB.bleu, RGB.rouge, e.aPlat));
      out.push(surFleche(e.flecheAir[0], e.flecheAir[1], nord, fr(k.avion_kmh * e.hAir) + ' km', c));
    }
    if (e.hVent > 0.02 && !seulVert) {
      const c = versHex(melange(RGB.violet, RGB.rouge, e.aPlat));
      const txt = fr(k.vent_kmh * e.hVent) + ' km';
      if (e.plan === 'ventSeul') {
        // shot 6: the arrow starts at the frame's left margin; the label hangs under its tip (the balloon)
        out.push({ x: vt.x, y: 0, z: vt.z + 4, texte: txt, couleur: c, ancre: coteEcran(0, 1) });
      } else if (violetDehors) {
        out.push({ x: vt.x, y: 0, z: vt.z + 9, texte: txt, couleur: c, ancre: 'droite' });
      } else out.push(surFleche(vq, vt, huit ? nord : dehors(vq, vt), txt, c));
    }
    if (huit && e.aPlat > 0.6) {
      out.push({ x: e.pointNaif.x, y: 0, z: e.pointNaif.z - 12, texte: fr(Math.round(k.avion_kmh) + Math.round(k.vent_kmh)) + ' km', couleur: COULEUR.rouge, ancre: coteEcran(0, -1) });
    } else if (e.plan === 'correction') {
      // under the arrival (south of both the green tip and the runway), never on top of them
      const ec = Math.abs(e.ecartKm);
      const txt = 'à côté : ' + (ec < 0.05 ? '0 km' : fr(ec, 1) + ' km');
      out.push({ x: s.x, y: 0, z: Math.max(s.z, e.piste.z) + 11, texte: txt, couleur: COULEUR.gris, ancre: coteEcran(0, 1) });
    } else if (e.visVert > 0.5 && !huit && (e.hSol <= 0 || e.hSol >= 1)) {
      const L = Math.hypot(e.sol.est, e.sol.nord);
      out.push(surFleche(e.flecheSol[0], e.flecheSol[1], { x: 0, z: 1 }, fr(L) + ' km', COULEUR.vert));
    }
    return out.slice(0, 3);
  }

  /**
   * Points the labels must keep clear of (CARTE coordinates): arrow tips, aeroplanes, balloon,
   * answer rings. `r` = radius of the drawn object in km (0 = a tip only).
   * @param {any} e etat(t, d)
   */
  function obstacles(e) {
    const t = e.t;
    const out = [];
    if (t < PLANS.question.t[0] || t >= PLANS.pose.t[0]) return out;
    const g = vues(t, e);
    const [, vt] = flecheVentPosee(e);
    if (e.hAir > 0.02) out.push({ x: e.flecheAir[1].x, z: e.flecheAir[1].z, r: 4 });
    if (e.hVent > 0.02) out.push({ x: vt.x, z: vt.z, r: 4 });
    if (e.visVert > 0.05) out.push({ x: e.flecheSol[1].x, z: e.flecheSol[1].z, r: 4 });
    if (g.avion > 0.05) out.push({ x: e.posAvion.x, z: e.posAvion.z, r: 7.5 });
    if (g.fantome > 0.05) out.push({ x: e.posFantome.x, z: e.posFantome.z, r: 7.5 });
    if (g.ballon > 0.05) out.push({ x: e.posBallon.x, z: e.posBallon.z, r: 3.5 });
    if (g.ringB > 0.05) out.push({ x: e.reponses.B.x, z: e.reponses.B.z, r: 5.8 });
    if (g.ringAC > 0.05) for (const n of ['A', 'C']) out.push({ x: e.reponses[n].x, z: e.reponses[n].z, r: 5.8 });
    if (e.plan === 'correction') out.push({ x: e.piste.x + 8, z: e.piste.z, r: 7 }); // the enlarged runway
    return out;
  }

  return { scene, camera, maj, etiquettes, obstacles, setVertical };
}
