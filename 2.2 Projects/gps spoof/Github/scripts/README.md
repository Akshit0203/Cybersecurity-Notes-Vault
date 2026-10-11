# Automation Scripts

These scripts wrap the full GPS spoofing workflow documented in the
[main README](../README.md) and [methodology](../docs/methodology.md). They target a
Linux/SDR environment (e.g. **DragonOS**) with `gcc`, `git`, `curl`, `gzip`, and the
**HackRF host tools** installed.

> ⚠️ **Read [../DISCLAIMER.md](../DISCLAIMER.md) first.** `04_transmit.sh` will not run without
> an explicit RF‑isolation confirmation, by design. Never transmit on GPS frequencies over the air.

## Order of execution

| # | Script | What it does |
|---|---|---|
| 1 | `01_setup.sh` | Clones and compiles [GPS‑SDR‑SIM](https://github.com/osqzss/gps-sdr-sim). |
| 2 | `02_fetch_ephemeris.sh` | Downloads + decompresses the configured BRDC (RINEX nav) file from NASA CDDIS. |
| 3 | `03_generate_signal.sh` | Runs GPS‑SDR‑SIM to produce `gpssim.bin` for the configured coordinates. |
| 4 | `04_transmit.sh` | Guarded `hackrf_transfer` wrapper — transmits the I/Q (RF‑isolated bench only). |

All configuration lives in **[`config.sh`](config.sh)** — target coordinates (default: IGI
Airport), frequency, sample rate, duration, BRDC day/year, and paths.

## Quick start

```bash
cd scripts
chmod +x *.sh

# Optionally override defaults via environment or by editing config.sh:
#   TARGET_LAT, TARGET_LON, TARGET_ALT, BRDC_DOY, BRDC_YY, BRDC_YEAR, DURATION ...

./01_setup.sh
./02_fetch_ephemeris.sh       # needs a NASA Earthdata login (see the script header)
./03_generate_signal.sh
./04_transmit.sh              # asks for explicit RF-isolation confirmation
```

## Notes

- **Earthdata / CDDIS auth:** CDDIS requires a free [Earthdata](https://urs.earthdata.nasa.gov/)
  account. Configure `~/.netrc` (see `02_fetch_ephemeris.sh` header) or download the BRDC file
  manually and drop it into the working directory.
- **Working directory:** defaults to `~/gps-sdr-sim` (override with `WORKDIR=...`).
- **Sample data:** a ready‑to‑inspect BRDC file is in [`../data/ephemeris/`](../data/ephemeris/).
- **Syntax check:** `bash -n 0X_*.sh` (or run `shellcheck`) before editing/running.
