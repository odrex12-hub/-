#!/bin/bash
# Shared helpers for SITL campaigns. Source after setting CAMPAIGN (c2, c3, ...).
#   inst <variant>        install model variant from $OUT/<variant> and rebuild; aborts the campaign on build failure
#   run <stem> <motor> [VAR=value ...]
#                         one case -> $OUT/<stem>_m<motor>.json, log -> $OUT/logs/, status -> <campaign>_progress.txt
# On any exit (normal, error, Ctrl-C) the default model "gen" is reinstalled if another variant was left installed.
set -u

PX4_DIR=${PX4_DIR:-/src/PX4-Autopilot}
OUT=${OUT:-/out}
LOGDIR=$OUT/logs
DONE=$OUT/${CAMPAIGN}_done.txt
PROGRESS=$OUT/${CAMPAIGN}_progress.txt

mkdir -p "$LOGDIR"
rm -f "$DONE" "$PROGRESS"

CURRENT_MODEL=""   # empty = whatever was installed before the campaign (assumed "gen")

inst() {
  local variant=$1
  CURRENT_MODEL=$variant   # set before building: model files are replaced even if the build fails
  if ! (
    cd "$PX4_DIR" &&
    rm -rf Tools/simulation/gz/models/agro_hexa &&
    cp -r "$OUT/$variant/models/agro_hexa" Tools/simulation/gz/models/ &&
    cp "$OUT/$variant/airframes/4099_gz_agro_hexa" ROMFS/px4fmu_common/init.d-posix/airframes/ &&
    make px4_sitl_default
  ) > "$OUT/build_$variant.log" 2>&1; then
    echo "BUILD_FAIL $variant (see build_$variant.log)" >> "$DONE"
    exit 1   # never run cases on a stale build
  fi
}

run() {
  local stem=$1 m=$2
  shift 2
  local tag=${stem}_m$m
  if env "$@" python3 "$OUT/run_case.py" "$m" "$OUT/$tag.json" > "$LOGDIR/$tag.log" 2>&1; then
    echo "$tag OK" >> "$PROGRESS"
  else
    echo "$tag FAIL rc=$? (see logs/$tag.log)" >> "$PROGRESS"
  fi
}

finish() {
  echo "ALLDONE fails=$(grep -c ' FAIL ' "$PROGRESS" 2>/dev/null || true)" >> "$DONE"
}

restore_default_model() {
  if [ -n "$CURRENT_MODEL" ] && [ "$CURRENT_MODEL" != gen ]; then
    echo "restoring model gen (was $CURRENT_MODEL)" >> "$DONE"
    inst gen
  fi
}
trap restore_default_model EXIT
trap 'exit 130' INT TERM
