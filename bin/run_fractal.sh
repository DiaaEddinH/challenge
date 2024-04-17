mkdir -p results

python bin/calc_fractal.py 3 data/data.dat
python bin/fig1.py

python bin/calc_fractal.py 5 data/data.dat
python bin/fig2.py

python bin/calc_fractal.py 6 data/data.dat
python bin/fig3.py

python bin/fig4.py
