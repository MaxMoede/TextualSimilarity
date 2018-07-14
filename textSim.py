#MAX MOEDE
from jira import JIRA
from git import Repo
import tempfile
import json
import time
import csv
import subprocess
from subprocess import PIPE
import os, errno
import re
import git
import sys
import itertools
import shutil
from datetime import date, timedelta, datetime

#For each commit in the project
#Take the ticket linked to it
#Take the date the ticket was marked "in progress"

def createRepo(githubURL):
	repoPath = ""
	try:
		os.makedirs("repoHolder")
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
		else:
			shutil.rmtree("./repoHolder")
			os.makedirs("repoHolder")
	git.Git("./repoHolder").clone(githubURL)
	for x in os.listdir("./repoHolder"):
		if os.path.isdir(os.path.join("./repoHolder", x)):
			repoPath = str(x)
		else:
			print("{} is not recognized as a directory.".format(str(x)))
	return repoPath

def get_repo(repoPath):
	initialFolder = os.path.abspath(os.curdir)
	fullRepoPath = initialFolder + "/" + repoPath
	repo = Repo(fullRepoPath)
	return repo

def get_list_of_commits(repo):
	listOfCommits = []
	p = subprocess.Popen(["git", "log", "--all", "--oneline"], stdout=PIPE, stderr=PIPE)
	output, error = p.communicate()
	if p.returncode == 0:
		commits = output.split("\n")
		for eachCommit in commits:
			partsOfCommit = eachCommit.split()
			if len(partsOfCommit) > 1:
				commitHash = partsOfCommit[0]
				listOfCommits.append(eachCommit)
				print("commit: {}".format(commitHash))
	else:
		print("something went wrong... {}".format(error))
	return listOfCommits

def get_textual_similarity(listOfCommits, repo):
	print("hello")

def get_complexity(listOfCommits):
	print("hello as well")

def get_temporal_locality(listOfCommits, repo):
	print("getting temporal locality...")
	#for eachCommit in listOfCommits:
	#	commitInstance = eachCommit.split()[0]
	#	p = subprocess.Popen(["git", "show", "--name-only", ])

def main():
	githubURL = sys.argv[1]
	repoPath = createRepo(githubURL)
	repoPath = "./repoHolder/{}".format(repoPath)
	repo = get_repo(repoPath)
	os.chdir(repoPath)
	listOfCommits = get_list_of_commits(repo)
	get_temporal_locality(listOfCommits, repo)

if __name__ == '__main__':
	main()