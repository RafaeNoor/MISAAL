#!/bin/bash
BENCHMARK_NAME=$1

echo "Processing Compute only ${BENCHMARK_NAME}"
time ./${BENCHMARK_NAME}/bin/${BENCHMARK_NAME}_compute_run.out &> ${BENCHMARK_NAME}_compute_log

echo "Processing Datamovement only ${BENCHMARK_NAME}"
time ./${BENCHMARK_NAME}/bin/${BENCHMARK_NAME}_data_movement_run.out &> ${BENCHMARK_NAME}_data_movement_log

