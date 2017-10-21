# Author: Jon Seaman (.73)
# Version: v1.0
# Revised: 10/08/2017
# Copyright (c) 2017 Jon Seaman

import os
from os.path import join

if __name__ == "__main__":
    # Allow the user to enter a directory to work from.
    working_dir = input("Enter the path to the submissions directory: ")
    os.chdir(working_dir)
    print("Working in: " + os.getcwd())

    # For each dir in the current folder.
    for dir_or_file in os.listdir("."):
        if os.path.isdir(dir_or_file):
            # Grab name for renaming. This happens to be the students name.
            name = dir_or_file.split("_")[0]
            # go into sub_dir
            directory = os.path.join(".", dir_or_file)
            directory = join(directory, os.listdir(directory)[0])

            # Look for .project in dir, rename project
            project_filename = join(directory, ".project")
            project_file = open(project_filename, mode='r')

            # Look in project file to replace the project name
            lines = []
            found_name = False
            for line in project_file:
                if "<name>" in line and not found_name:
                    lines.append("<name>" + name + "</name>\n")
                    found_name = True
                else:
                    lines.append(line)

            # Write the lines back to the file.
            print("Writing file..." + project_filename, end='')
            project_file = open(project_filename, mode='w')
            project_file.writelines(lines)
            print("\nDone.")
