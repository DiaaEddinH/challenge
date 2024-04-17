mkdir -p data
curl -L -o data/survey.csv https://energydata.info/dataset/a27a9b60-706b-4c81-8608-c913d2ed998f/resource/fdef4f22-fe57-49b1-9c42-e5dac79cc90c/download/pakistanbiomassfieldsurvey.csv

mkdir -p results

python bin/calc_fractal.py 3 results/data.dat
python bin/fig1.py

python bin/calc_fractal.py 5 results/data.dat
python bin/fig2.py

python bin/calc_fractal.py 6 results/data.dat
python bin/fig3.py

python bin/fig4.py
