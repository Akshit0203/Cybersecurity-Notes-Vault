#!/usr/bin/env bash
# =============================================================================
# 02_fetch_ephemeris.sh — Download & decompress a daily BRDC (RINEX nav) file
# from NASA CDDIS.
#
# Requires a free NASA Earthdata account: https://urs.earthdata.nasa.gov/
# CDDIS uses Earthdata authentication, so configure ~/.netrc first:
#
#   machine urs.earthdata.nasa.gov login <USER> password <PASS>
#   (chmod 600 ~/.netrc)
#
# You can also simply download the file manually from the archive and place it
# in ${WORKDIR}; this script only automates the common case.
# =============================================================================
set -euo pipefail
cd "$(dirname "$0")"
source ./config.sh

mkdir -p "${WORKDIR}"

GZ_NAME="brdc${BRDC_DOY}0.${BRDC_YY}n.gz"
ARCHIVE_URL="https://cddis.nasa.gov/archive/gnss/data/daily/${BRDC_YEAR}/brdc/${GZ_NAME}"
GZ_PATH="${WORKDIR}/${GZ_NAME}"
OUT_PATH="${EPHEMERIS_FILE}"

log "BRDC file : ${GZ_NAME}"
log "Source    : ${ARCHIVE_URL}"
log "Target    : ${OUT_PATH}"

if [ -f "${OUT_PATH}" ]; then
  ok "Ephemeris already present: ${OUT_PATH}"
  exit 0
fi

if ! command -v curl >/dev/null 2>&1; then
  err "curl not found. Install curl, or download ${GZ_NAME} manually into ${WORKDIR}."
  exit 1
fi

if [ ! -f "${HOME}/.netrc" ]; then
  warn "No ~/.netrc found. CDDIS requires Earthdata login."
  warn "Create ~/.netrc with your Earthdata credentials, or download the file manually from:"
  warn "  https://cddis.nasa.gov/archive/gnss/data/daily/${BRDC_YEAR}/brdc/"
fi

log "Downloading (following Earthdata auth redirects)..."
curl -L -n -c /tmp/cddis_cookies.txt -b /tmp/cddis_cookies.txt \
     -o "${GZ_PATH}" "${ARCHIVE_URL}"

log "Decompressing..."
gzip -df "${GZ_PATH}"

if [ -f "${OUT_PATH}" ]; then
  ok "Ephemeris ready: ${OUT_PATH}"
else
  err "Expected ${OUT_PATH} after decompression but it was not found."
  err "Check the DOY/year in config.sh or download the file manually."
  exit 1
fi
