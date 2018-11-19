# Task 
Identify the category of news based on headlines and short descriptions.

## Project Structure 

```
News Analysis/
│
├── input/                                      # Input Files 
├── notebook/                                   # Ipython Notebooks
│   └── 01 Exploratory Data Analysis.ipynb
|   └── 02 Model Building.ipynb
├── docs/                                                 
├── script/                                     # Python Scripts
|   └── json_to_csv.py
├── cleaned/                                    # Cleaned Data
|   └── newsdata.csv
└── README.md
└── requirements.txt
```

## Installation

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included

Open the terminal & Install the dependencies .

```sh
$ cd news analysis
$ pip install -r requirements.txt
$ cd script
$ python3 json_to_csv.py
$ cd notebook
$ jupyter 02 Model Building.ipynb
```sh
