#!/bin/bash

if [[ "$1" == "--fail" ]]; then
    echo "Simulando fallo"
    exit 1
fi

echo "Simulación exitosa"
exit 0

