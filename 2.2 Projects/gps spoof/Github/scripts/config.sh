#!/usr/bin/env bash
# =============================================================================
# config.sh — Central configuration for the GPS spoofing demonstration.
# Source this file from the other scripts: `source ./config.sh`
#
# Edit the values below to change the target location, RF parameters, or paths.
# =============================================================================

# --- GPS-SDR-SIM ---------------------------------------------------------------
GPS_SDR_SIM_REPO="https://github.com/osqzss/gps-sdr-sim.git"
# Working directory where GPS-SDR-SIM is cloned/built and signals are generated.
WORKDIR="${WORKDIR:-$HOME/gps-sdr-sim}"
GPS_SDR_SIM_BIN="${WORKDIR}/gps-sdr-sim"

# --- Target (spoofed) location -------------------------------------------------
# Default: Indira Gandhi International (IGI) Airport, New Delhi.
TARGET_LAT="${TARGET_LAT:-28.556276}"     # latitude  (decimal degrees)
TARGET_LON="${TARGET_LON:-77.100662}"     # longitude (decimal degrees)
TARGET_ALT="${TARGET_ALT:-100}"           # altitude  (meters)

# --- Ephemeris (RINEX navigation / BRDC) --------------------------------------
# Day-of-year (001-366) and 2-digit year for the BRDC file to fetch.
# Example: brdc3190.25n  ->  DOY=319  YY=25
BRDC_DOY="${BRDC_DOY:-319}"
BRDC_YY="${BRDC_YY:-25}"
BRDC_YEAR="${BRDC_YEAR:-2025}"
EPHEMERIS_FILE="${EPHEMERIS_FILE:-${WORKDIR}/brdc${BRDC_DOY}0.${BRDC_YY}n}"

# --- Signal generation ---------------------------------------------------------
SAMPLE_BITS="8"                           # 8-bit signed I/Q (required by HackRF)
OUTPUT_IQ="${OUTPUT_IQ:-${WORKDIR}/gpssim.bin}"
# Optional: simulation duration in seconds (GPS-SDR-SIM default is ~300).
DURATION="${DURATION:-300}"

# --- HackRF transmission -------------------------------------------------------
TX_FREQ="1575420000"                      # GPS L1 carrier (Hz) = 1575.42 MHz
SAMPLE_RATE="2600000"                     # 2.6 Msps
TX_AMP="1"                                # enable amplifier (1=on)
TX_GAIN="0"                               # TX VGA gain (keep minimal on the bench)

# --- Pretty logging helpers ----------------------------------------------------
_c_reset="\033[0m"; _c_green="\033[1;32m"; _c_yellow="\033[1;33m"; _c_red="\033[1;31m"; _c_blue="\033[1;34m"
log()  { printf "${_c_blue}[*]${_c_reset} %s\n" "$*"; }
ok()   { printf "${_c_green}[+]${_c_reset} %s\n" "$*"; }
warn() { printf "${_c_yellow}[!]${_c_reset} %s\n" "$*"; }
err()  { printf "${_c_red}[x]${_c_reset} %s\n" "$*" >&2; }
