#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_qr_code_generator..."
wine "run_qr_code_generator" || ./"run_qr_code_generator" "$@"
