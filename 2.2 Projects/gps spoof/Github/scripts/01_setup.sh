#!/usr/bin/env bash
# =============================================================================
# 01_setup.sh — Clone and compile GPS-SDR-SIM.
# =============================================================================
set -euo pipefail
cd "$(dirname "$0")"
source ./config.sh

log "GPS-SDR-SIM working directory: ${WORKDIR}"

if ! command -v gcc >/dev/null 2>&1; then
  err "gcc not found. Install build tools (e.g. 'sudo apt install build-essential')."
  exit 1
fi

if [ -d "${WORKDIR}/.git" ]; then
  log "Repository already present — pulling latest changes."
  git -C "${WORKDIR}" pull --ff-only || warn "Could not fast-forward; using existing checkout."
else
  log "Cloning GPS-SDR-SIM from ${GPS_SDR_SIM_REPO}"
  git clone "${GPS_SDR_SIM_REPO}" "${WORKDIR}"
fi

log "Compiling gpssim.c with GCC (-O3)..."
( cd "${WORKDIR}" && gcc gpssim.c -lm -O3 -o gps-sdr-sim )

if [ -x "${GPS_SDR_SIM_BIN}" ]; then
  ok "Build complete: ${GPS_SDR_SIM_BIN}"
else
  err "Build failed — expected binary not found at ${GPS_SDR_SIM_BIN}"
  exit 1
fi
