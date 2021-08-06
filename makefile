init:
	conda create -n fpl21 python=3.8 --yes &&\
	source activate fpl21 &&\
	pip install -r requirements.txt\
	pip install -e .

test:
	python -m pytest .