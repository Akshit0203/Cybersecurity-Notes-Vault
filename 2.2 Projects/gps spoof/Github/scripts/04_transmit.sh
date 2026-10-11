#!/usr/bin/env bash
# =============================================================================
# 04_transmit.sh — Transmit the generated I/Q (gpssim.bin) with HackRF One.
#
# !!  DANGER / LEGAL  !!
# Transmitting on GPS L1 (1575.42 MHz) over the air is ILLEGAL in virtually
# every country and is dangerous to aircraft, ships, vehicles, phones, and
# timing infrastructure. This script is intended ONLY for a wired / shielded,
# RF-ISOLATED bench into a dedicated receiver under test.
#
# As a safeguard, this script refuses to run unless you explicitly confirm the
# RF-isolation requirement, either interactively or by setting:
#     I_UNDERSTAND_RF_ISOLATION=yes ./04_transmit.sh
# =============================================================================
set -euo pipefail
cd "$(dirname "$0")"
source ./config.sh

cat <<'BANNER'
-------------------------------------------------------------------------------
  GPS L1 TRANSMISSION — RF-ISOLATED BENCH ONLY
  Transmitting spoofed GPS over the air is illegal and dangerous.
  Proceed ONLY if this HackRF is connected by cable/shielding into a receiver
  under test, with NO radiating antenna and NO exposure to public space.
-------------------------------------------------------------------------------
BANNER

confirm="${I_UNDERSTAND_RF_ISOLATION:-}"
if [ "${confirm}" != "yes" ]; then
  read -r -p "Type 'yes' to confirm this is an RF-isolated test environment: " confirm
fi
if [ "${confirm}" != "yes" ]; then
  err "Confirmation not given. Aborting — nothing transmitted."
  exit 1
fi

if ! command -v hackrf_transfer >/dev/null 2>&1; then
  err "hackrf_transfer not found. Install the HackRF host tools."
  exit 1
fi

if [ ! -f "${OUTPUT_IQ}" ]; then
  err "I/Q file not found: ${OUTPUT_IQ}. Run ./03_generate_signal.sh first."
  exit 1
fi

log "Verifying HackRF..."
hackrf_info || { err "HackRF not detected."; exit 1; }

log "Transmitting ${OUTPUT_IQ}"
log "  Frequency   : ${TX_FREQ} Hz (GPS L1, 1575.42 MHz)"
log "  Sample rate : ${SAMPLE_RATE} sps"
log "  Amp / Gain  : -a ${TX_AMP}  -x ${TX_GAIN}"
warn "Press Ctrl-C to stop."

hackrf_transfer \
  -t "${OUTPUT_IQ}" \
  -f "${TX_FREQ}" \
  -s "${SAMPLE_RATE}" \
  -a "${TX_AMP}" \
  -x "${TX_GAIN}"

ok "Transmission finished."
