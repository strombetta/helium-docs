#!/usr/bin/env bash
set -euo pipefail

font_directory="templates/helium/public/fonts"
font_path="${font_directory}/manrope-latin-wght-normal.woff2"
font_url="https://cdn.jsdelivr.net/fontsource/fonts/manrope:vf@5.3.0/latin-wght-normal.woff2"
expected_blob_sha="71eb731d558046199aa7f985adbf812890a093a1"

mkdir -p "${font_directory}"
curl --fail --location --silent --show-error "${font_url}" --output "${font_path}"

actual_blob_sha="$(git hash-object "${font_path}")"
if [[ "${actual_blob_sha}" != "${expected_blob_sha}" ]]; then
  echo "Unexpected Manrope font checksum: ${actual_blob_sha}" >&2
  rm -f "${font_path}"
  exit 1
fi
