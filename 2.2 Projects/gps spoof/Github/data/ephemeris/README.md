# Sample Ephemeris Data

## `brdc3190.25n`

A **RINEX navigation (broadcast ephemeris)** file obtained from
[NASA CDDIS](https://cddis.nasa.gov/archive/gnss/data/daily/). It is included here so the file
format can be inspected and the demonstration reproduced.

### Filename decoded

```
brdc 319 0 . 25 n
│    │   │   │  └── file type:  n = GPS navigation message
│    │   │   └───── year:       25 = 2025
│    │   └───────── (session)
│    └───────────── day-of-year: 319
└────────────────── "brdc" = broadcast (merged daily navigation data)
```

So `brdc3190.25n` = the GPS broadcast navigation data for **day‑of‑year 319 of 2025**.

### What's inside

Plain‑text RINEX v2:

- **Header** — RINEX version/type, program/run info, ionospheric correction terms
  (`ION ALPHA` / `ION BETA`), UTC/leap‑second data, `END OF HEADER`.
- **Records** — one block per satellite per epoch: satellite PRN, reference time, clock bias/
  drift, and the Keplerian orbital parameters (semi‑major axis, eccentricity, inclination,
  correction terms, etc.) used to compute each satellite's position.

GPS‑SDR‑SIM reads this to place the simulated satellites so the generated L1 C/A waveform is
structurally valid.

### Getting a current file

Daily files are published at:

```
https://cddis.nasa.gov/archive/gnss/data/daily/<YEAR>/brdc/brdc<DOY>0.<YY>n.gz
```

A free [NASA Earthdata](https://urs.earthdata.nasa.gov/) login is required. The helper script
[`../../scripts/02_fetch_ephemeris.sh`](../../scripts/02_fetch_ephemeris.sh) automates the
download and decompression.

> **Attribution:** broadcast ephemeris data courtesy of NASA CDDIS. Please follow CDDIS's data
> use and citation guidance when redistributing.
