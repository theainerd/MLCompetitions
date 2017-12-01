### Problem Description

In total, there are 40 type of attacks to which their network is vulnerable to. But, 3 of them cause the maximum damage. In this challenge, we are given an anonymised sample dataset of server connections. We have to predict the type of attack(s).

For detailed description visit:
[Problem Description](https://www.hackerearth.com/challenge/competitive/machine-learning-challenge-4/machine-learning/sample/#c124772)

### Folder Description

input - contain all the input files.
output - contain all the submission files produced from results.
proxy - contain all the data saved to disk for future use

### How to produce the results

1. Run datasetprep.ipynb to produce the datasets.
2. Run model_selection.ipynb to produce the prediction csv file.
3. Finally ensemble it using kaggle_vote.py (sub1.csv+ sub2.csv+ sub3.csv) to produce the final submission.

### Results

Scored Rank 80 on the public leaderboard.

### Lessons Learned

1. Predicting the probability and then setting the threshold improves the reults. Plot AUC-ROC curve to decide the threshold.

2. Always save your submission file in a systematic manner else very soon you will lose control over your submissions and later nothing will sense.
