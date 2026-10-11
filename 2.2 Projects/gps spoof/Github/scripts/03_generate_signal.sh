#!/usr/bin/env bash
# =============================================================================
# 03_generate_signal.sh — Generate the spoofed GPS L1 I/Q samples (gpssim.bin)
# for the configured coordinates using GPS-SDR-SIM.
# =============================================================================
set -euo pipefail
cd "$(dirname "$0")"
source ./config.sh

if [ ! -x "${GPS_SDR_SIM_BIN}" ]; then
  err "GPS-SDR-SIM binary not found. Run ./01_setup.sh first."
  exit 1
fi

if [ ! -f "${EPHEMERIS_FILE}" ]; then
  err "Ephemeris file not found: ${EPHEMERIS_FILE}"
  err "Run ./02_fetch_ephemeris.sh (or place a BRDC file there)."
  exit 1
fi

log "Generating spoofed GPS signal"
log "  Ephemeris : ${EPHEMERIS_FILE}"
log "  Location  : ${TARGET_LAT}, ${TARGET_LON}, ${TARGET_ALT} m"
log "  Format    : ${SAMPLE_BITS}-bit I/Q"
log "  Duration  : ${DURATION} s"
log "  Output    : ${OUTPUT_IQ}"

"${GPS_SDR_SIM_BIN}" \
  -e "${EPHEMERIS_FILE}" \
  -l "${TARGET_LAT},${TARGET_LON},${TARGET_ALT}" \
  -b "${SAMPLE_BITS}" \
  -d "${DURATION}" \
  -o "${OUTPUT_IQ}"

if [ -f "${OUTPUT_IQ}" ]; then
  ok "Signal generated: ${OUTPUT_IQ} ($(du -h "${OUTPUT_IQ}" | cut -f1))"
else
  err "Signal generation failed — ${OUTPUT_IQ} was not produced."
  exit 1
fi
