// Copyright: Your Name. Apache 2.0
// Contract of the « Vent de travers » film, version 2 (10 shots, 58 s). Constants, colours,
// deterministic helpers and the film state etat(t, d). Every module renders as a pure function of
// the film time t (seconds). Engine: Babylon.js 9.33.1 (global BABYLON), right-handed scenes.
//
// Central idea: three things leave the same point at the same instant —
//   the ghost aeroplane (blue): where the aeroplane would be if the air stood still;
//   the balloon (violet): where the air itself goes (wind alone);
//   the real aeroplane (green track): ghost position + balloon displacement, at every instant.
//
// Two scenes, two scales (never mix them):
//   CARTE  (shots 4-9): 1 unit = 1 km, +x east, -z north, +y up, fixed top-down camera, north up.
//   PROCHE (shots 1-3, 10): 1 unit = 1 metre, same axes, cinematic camera.
// All on-screen quantities are in km and km/h (no knots, no degrees, no jargon).

export const DUREE = 58;

/** Role colours (dark filmic scenes). One meaning per colour. */
export const COULEUR = Object.freeze({
  bleu: '#4f9dff', // the aeroplane in still air: ghost aeroplane, blue arrow
  violet: '#b78cff', // the wind: balloon, violet arrow
  vert: '#4fe08f', // the result: real aeroplane's path over the ground, green arrow
  orange: '#ff9a3d', // what changes: ONLY the rotation arc of shot 9
  rouge: '#ff5a4f', // the wrong idea: ONLY in shot 8
  gris: '#aab2bf', // what does not change: runway line, offsets, neutral text
});

/** Shots: [start, end) in seconds, and which scene renders them. */
export const PLANS = Object.freeze({
  lacher: { t: [0, 4], scene: 'proche' }, // 1. close-up: the balloon is released
  derive: { t: [4, 9], scene: 'proche' }, // 2. the balloon drifts with the air; violet line on the ground
  avion: { t: [9, 14], scene: 'proche' }, // 3. the Cessna, three-quarter view, aims at the runway far ahead
  question: { t: [14, 19], scene: 'carte' }, // 4. fixed map, frozen: where is it in one hour? A, B, C
  airSeul: { t: [19, 25], scene: 'carte' }, // 5. ghost aeroplane alone: blue arrow, 220 km straight
  ventSeul: { t: [25, 30], scene: 'carte' }, // 6. balloon alone: violet arrow, 34 km sideways
  boutABout: { t: [30, 38], scene: 'carte' }, // 7. violet slides to the tip of blue; green appears; replay of the three
  ideeFausse: { t: [38, 43], scene: 'carte' }, // 8. lengths laid end to end on one line: red, crossed out
  correction: { t: [43, 51], scene: 'carte' }, // 9. the blue arrow turns; the green tip lands on the runway
  pose: { t: [51, 58], scene: 'proche' }, // 10. landing close-up, then the final triangle on a plate
});

export const clamp01 = (x) => Math.min(1, Math.max(0, x));
export const lerp = (a, b, k) => a + (b - a) * k;
export const smooth = (x) => { const k = clamp01(x); return k * k * (3 - 2 * k); };
export const smoother = (x) => { const k = clamp01(x); return k * k * k * (k * (k * 6 - 15) + 10); };
/** Progress of t inside [a, b], clamped to 0..1. */
export const prog = (t, a, b) => clamp01((t - a) / (b - a));
export const rad = (d) => (d * Math.PI) / 180;

/** Seeded generator: the only allowed randomness (never Math.random / Date.now in rendering). */
export function prng(graine) {
  let a = graine >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let x = Math.imul(a ^ (a >>> 15), 1 | a);
    x = (x + Math.imul(x ^ (x >>> 7), 61 | x)) ^ x;
    return ((x ^ (x >>> 14)) >>> 0) / 4294967296;
  };
}

/** Loads the measured data (built by tools/niveau/donnees_anim.py). Use d.km for everything shown. */
export async function chargerDonnees() {
  const r = await fetch(new URL('./donnees.json', import.meta.url));
  if (!r.ok) throw new Error(`donnees.json : ${r.status}`);
  return r.json();
}

/** French number: decimal comma, thin no-break space for thousands, real minus sign. */
export function fr(x, decimales = 0) {
  const s = Math.abs(x).toFixed(decimales);
  const [ent, dec] = s.split('.');
  const groupes = ent.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  const signe = x < 0 && Number(s) !== 0 ? '−' : '';
  return signe + groupes + (dec ? `,${dec}` : '');
}

/** Name of the shot that contains t. */
export function planA(t) {
  for (const [nom, p] of Object.entries(PLANS)) if (t >= p.t[0] && t < p.t[1]) return nom;
  return 'pose';
}

/** (east, north) in km → CARTE world coordinates. */
export const carte = (est, nord) => ({ x: est, z: -nord });

/**
 * Film state at time t. Positions are exact: sol = air + vent, component by component, in km.
 * The CARTE origin is the midpoint of the intended route: depart at x = -D/2, runway threshold at x = +D/2.
 * @param {number} t film time in seconds
 * @param {any} d data from chargerDonnees()
 */
export function etat(t, d) {
  const k = d.km;
  const P = PLANS;
  const plan = planA(t);
  const depart = carte(-k.distance / 2, 0);
  const piste = carte(k.distance / 2, 0);
  const versCarte = (p) => ({ x: depart.x + p.est, z: depart.z - p.nord });

  // --- shot 9: the blue arrow turns from "nose at the runway" to "nose into the wind a little"
  const virage = smoother(prog(t, P.correction.t[0] + 1.2, P.correction.t[0] + 5.2)); // 0 → 1
  const tourne = t >= P.correction.t[0] ? virage : 0;
  const capDeg = lerp(k.faux.cap, k.bon.cap, tourne);
  const air = { est: k.avion_kmh * Math.sin(rad(capDeg)), nord: k.avion_kmh * Math.cos(rad(capDeg)) }; // one hour, still air
  const vent = k.vent; // one hour of wind
  const sol = { est: air.est + vent.est, nord: air.nord + vent.nord };

  // --- hours elapsed for each of the three things (0..1), per shot
  let hAir = 0; // ghost aeroplane
  let hVent = 0; // balloon
  let hSol = 0; // real aeroplane
  if (plan === 'airSeul') hAir = prog(t, 19.8, 24.0);
  else if (plan === 'ventSeul') { hAir = 1; hVent = prog(t, 25.6, 29.0); }
  else if (plan === 'boutABout') {
    const rejoue = prog(t, 34.6, 37.4); // the three leave together again
    hAir = t < 34.4 ? 1 : rejoue;
    hVent = t < 34.4 ? 1 : rejoue;
    hSol = t < 34.4 ? 0 : rejoue;
  } else if (t >= P.ideeFausse.t[0] && t < P.pose.t[0]) { hAir = 1; hVent = 1; hSol = 1; }

  // --- shot 7: the violet arrow, drawn from the departure in shot 6, slides to the tip of the blue one
  const glisse = t < P.boutABout.t[0] ? 0 : smoother(prog(t, 30.4, 32.8));
  const origineVent = { est: air.est * glisse, nord: air.nord * glisse }; // tail of the violet arrow
  const visVert = t < P.boutABout.t[0] ? 0 : smooth(prog(t, 33.0, 34.2));

  // --- shot 8: the wrong idea — both lengths end to end on the straight line (254.6 km), in red
  const aPlat = smoother(prog(t, 38.6, 40.2)) * (1 - smoother(prog(t, 42.2, 42.9)));
  const barre = smooth(prog(t, 40.8, 41.5)) * (1 - smooth(prog(t, 42.2, 42.9)));

  // --- close shots
  const lacher = smooth(prog(t, 1.2, 3.6)); // 1: the hand lets go, the balloon rises to its level
  const heureBallon = prog(t, 4.6, 8.6); // 2: one hour of drift, compressed
  const approche = prog(t, 51.2, 54.6); // 10: final approach and touchdown
  const plaque = smooth(prog(t, 55.2, 56.2)); // 10: final plate

  return {
    t, plan, scene: P[plan].scene,
    depart, piste,
    capDeg, tourne,
    /** one-hour vectors in km (east, north) */
    air, vent, sol,
    hAir, hVent, hSol,
    /** CARTE positions of the three things right now */
    posFantome: versCarte({ est: air.est * hAir, nord: air.nord * hAir }),
    posBallon: versCarte({ est: vent.est * hVent, nord: vent.nord * hVent }),
    posAvion: versCarte({ est: sol.est * hSol, nord: sol.nord * hSol }),
    /** CARTE arrows: [tail, tip]; lengths grow with the hours */
    flecheAir: [versCarte({ est: 0, nord: 0 }), versCarte({ est: air.est * hAir, nord: air.nord * hAir })],
    flecheVent: [
      versCarte(origineVent),
      versCarte({ est: origineVent.est + vent.est * hVent, nord: origineVent.nord + vent.nord * hVent }),
    ],
    flecheSol: [versCarte({ est: 0, nord: 0 }), versCarte(sol)],
    glisse, visVert,
    /** shot 8: tip of the flattened red sum on the straight line */
    aPlat, barre, pointNaif: versCarte({ est: k.naif.est, nord: 0 }),
    /** offset of the real arrival from the runway line, km (positive = south) */
    ecartKm: -sol.nord,
    /** shot 4: the three candidate answers (CARTE); B is the true arrival after one hour, nose at the runway */
    reponses: {
      A: versCarte({ est: k.distance, nord: 0 }),
      B: versCarte(k.faux.sol),
      C: versCarte({ est: k.faux.sol.est, nord: -k.faux.sol.nord }),
    },
    lacher, heureBallon, approche, plaque,
  };
}

/**
 * Captions: French, plain words, at most 12 words, each on screen at least 3 s, one at a time.
 * Numbers come from d.km. `cle` marks the rule that must stay at least 6 s.
 */
export function legendes(d) {
  const k = d.km;
  return [
    { t: [0.4, 4.0], texte: 'De Bilt, Pays-Bas, 12 novembre 2026. On lâche un ballon.' },
    { t: [4.3, 9.0], texte: `Le vent l’emporte : ${fr(k.vent_kmh, 0)} km en une heure, vers le sud-est.` },
    { t: [9.3, 14.0], texte: `Un petit avion vole à ${fr(k.avion_kmh, 0)} km/h. Il vise la piste, droit devant.` },
    { t: [14.3, 19.0], texte: 'Où sera-t-il dans une heure : A, B ou C ?' },
    { t: [19.3, 25.0], texte: `Sans vent : ${fr(k.avion_kmh, 0)} km tout droit.` },
    { t: [25.3, 30.0], texte: `Le vent seul : ${fr(k.vent_kmh, 0)} km de côté.` },
    { t: [30.3, 38.0], texte: 'On met les deux flèches bout à bout. Il arrive là : B.', cle: true },
    { t: [38.3, 43.0], texte: `Additionner les longueurs, ${fr(k.avion_kmh, 0)} + ${fr(k.vent_kmh, 0)}, donne un point faux.` },
    { t: [43.3, 51.0], texte: `On tourne un peu le nez vers le vent. La flèche verte tombe sur la piste.` },
    { t: [51.3, 55.0], texte: 'Posé.' },
    { t: [55.3, 58.0], texte: 'Vert = bleu, puis violet, bout à bout.', cle: true },
  ];
}
