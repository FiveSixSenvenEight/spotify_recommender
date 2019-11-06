# Spotify Recommender System

## Team 47
Members: Catharine Wu, Liyang Zhao, Yiwen Wang, Zihao Xu

## Directory Explanation
- `1-build/`: stores notebooks that clean/wrangle the data
- `2-eda/`: stores notebooks that does exploratory data analyses
- `3-analysis/`: stores notebooks that build recommender systems
- `utils.py`: used to  
	- load in common packages
	- store paths to datasets and export paths for visualizations
	- To import all the content of utils.py, you could put the following code at the top of each notebook.
	'''
	import sys
	sys.path.append("../")
	from utils import *
	'''

## File Naming Convention
- Refer to files inside `1-build/` for the naming convention.

## Workflow
- The workflow of this repo is similar to that of the CS207 final project, i.e.
	- It is **important** to `git pull` before working on anything 
	- Create a new branch for new work
	- Push changes to new branch
	- Create Pull Request
	- Someone else needs to **approve and merge** the changes
	- Everyone else needs to pull the new changes

