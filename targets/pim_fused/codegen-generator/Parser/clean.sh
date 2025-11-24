for i in {1..1000}
do

    echo "Iteration: $i"
    python3 ../glob_check.py
    sleep 60m
done
