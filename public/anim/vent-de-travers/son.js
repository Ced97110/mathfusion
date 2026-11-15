// Copyright: Your Name. Apache 2.0
// Sound mix of « Vent de travers » as pure data: two real recordings only, never synthesized audio.
// Gains are piecewise-linear functions of the film time t, so the page (Web Audio) and the offline
// renderer (ffmpeg volume expressions) produce the same mix. No DOM, no BABYLON: importable from Node.
//
// Recordings:
//   son/vent.mp3      real wind, W.carter, CC BY-SA 4.0 (60.5 s)
//   son/cessna172.mp3 real Cessna 172, Groningen Eelde, Beeld en Geluid, CC BY-SA 3.0 (31 s,
//                     fly-by peak near 12 s, touchdown near 25 s)

/**
 * Which part of each file plays when: film time [film, film + duree) reads the file from `source`.
 * Engine shot 3 (9-14 s): the fly-by peak (12 s) lands at film 13 s.
 * Engine shot 10 (51-58 s): the touchdown (25 s) lands at film 54.6 s, the end of the approach in etat().
 */
export const PISTES = Object.freeze({
  vent: { fichier: 'son/vent.mp3', segments: [{ film: 0, source: 0, duree: 58 }] },
  moteur: {
    fichier: 'son/cessna172.mp3',
    segments: [
      { film: 8.5, source: 7.5, duree: 6.4 },
      { film: 50.6, source: 21.0, duree: 7.4 },
    ],
  },
});

/**
 * Gain keys [t, gain]. Wind carries shots 1-2, stays soft under the map, almost silent during the
 * proof (shots 7-9); the engine plays only in shots 3 and 10.
 */
export const CLES = Object.freeze({
  vent: [
    [0, 0], [0.4, 0.85], [8.6, 0.85], [9.6, 0.3], [13.8, 0.3], [14.4, 0.22], [29.6, 0.22],
    [30.4, 0.07], [50.6, 0.07], [51.4, 0.35], [57.0, 0.3], [58, 0],
  ],
  moteur: [
    [0, 0], [8.5, 0], [9.4, 0.9], [13.4, 0.9], [14.0, 0], [50.6, 0], [51.2, 0.95], [55.2, 0.7],
    [57.2, 0.25], [58, 0],
  ],
});

/** Piecewise-linear interpolation of keys [[t, v], ...] at time t (held at both ends). */
export function interpoler(cles, t) {
  if (t <= cles[0][0]) return cles[0][1];
  for (let i = 1; i < cles.length; i += 1) {
    const [t1, v1] = cles[i];
    if (t < t1) {
      const [t0, v0] = cles[i - 1];
      return v0 + ((v1 - v0) * (t - t0)) / (t1 - t0);
    }
  }
  return cles[cles.length - 1][1];
}

/** Position inside a recording for film time t, or null when that recording is silent. */
export function positionSource(piste, t) {
  for (const s of piste.segments) if (t >= s.film && t < s.film + s.duree) return s.source + (t - s.film);
  return null;
}

/**
 * Mix at film time t: gains (0..1) and where each recording is read.
 * @param {number} t film time in seconds
 * @returns {{ vent: number, moteur: number, sourceVent: number|null, sourceMoteur: number|null }}
 */
export function mixage(t) {
  const sourceVent = positionSource(PISTES.vent, t);
  const sourceMoteur = positionSource(PISTES.moteur, t);
  return {
    vent: sourceVent === null ? 0 : interpoler(CLES.vent, t),
    moteur: sourceMoteur === null ? 0 : interpoler(CLES.moteur, t),
    sourceVent,
    sourceMoteur,
  };
}

/** ffmpeg expression (variable t, seconds) equal to interpoler(cles, t). Commas are protected by quotes. */
export function expressionFfmpeg(cles) {
  const n = (x) => Number(x.toFixed(6)).toString();
  let expr = n(cles[cles.length - 1][1]);
  for (let i = cles.length - 1; i >= 1; i -= 1) {
    const [t0, v0] = cles[i - 1];
    const [t1, v1] = cles[i];
    const pente = (v1 - v0) / (t1 - t0);
    const segment = pente === 0 ? n(v0) : `(${n(v0)}${pente < 0 ? '-' : '+'}${n(Math.abs(pente))}*(t-${n(t0)}))`;
    expr = `if(lt(t,${n(t1)}),${segment},${expr})`;
  }
  return `if(lt(t,${n(cles[0][0])}),${n(cles[0][1])},${expr})`;
}
