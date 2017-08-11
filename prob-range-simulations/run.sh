LA='1.6765100539857060'
LB='167.65100539857060'
N='1000'
IT=100
for p in $(seq -w 0 100); do
    echo -n "$p: "
    for i in $(seq 1 $IT); do
        python3 ../tools/DualBirthSimulator.py -la $LA -lb $LB -n $N -p $(echo $p/100 | bc -l) | python3 ../tools/estimate-r-by-bl.py
    done | numlist -csv
done
