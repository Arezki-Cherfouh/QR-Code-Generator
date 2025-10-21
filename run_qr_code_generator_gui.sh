#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_qr_code_generator_gui..."
wine "run_qr_code_generator_gui" || ./"run_qr_code_generator_gui" "$@"
