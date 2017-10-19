# CSE_GradingScript

## What this script does
This script modifies the project file for each submission so that each student's project can
be imported into eclipse at the same time.

## Requirements
* Archive manager, I use 7Zip.
* Python 3.x

## How to use

##### Get the submissions ready.

1. Download the zip of project files from carmen.
2. Unzip the archive to a folder called 'submissions'.
3. Open the 'submissions' folder.
4. Select all of the zip files.
5. RClick -> Zip .> Extract to "\*\"
6. Delete all of the zip files from 'submissions'

##### You are now ready to run the python script.

Run the python script, then when prompted, enter the path to 'submissions' directory.

```python3 GradingScript.py```

##### Importing

You can now import all of the projects from the 'submissions' directory into eclipse.