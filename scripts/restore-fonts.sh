#!/usr/bin/env bash
set -euo pipefail

font_directory="templates/helium/public/fonts"
font_path="${font_directory}/inter-latin-wght-normal.woff2"
font_url="https://raw.githubusercontent.com/fontsource/font-files/9c76865650f64dd9242db524070753930bc7685c/fonts/variable/inter/files/manrope-latin-wght-normal.woff2"
expected_blob_sha="d15208de03cd1ad7c5199f0a0ce915fe841e4722"

mkdir -p "${font_directory}"
curl --fail --location --silent --show-error "${font_url}" --output "${font_path}"

actual_blob_sha="$(git hash-object "${font_path}")"
if [[ "${actual_blob_sha}" != "${expected_blob_sha}" ]]; then
  echo "Unexpected Inter font checksum: ${actual_blob_sha}" >&2
  rm -f "${font_path}"
  exit 1
fi
