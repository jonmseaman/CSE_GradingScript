# Author: Jon Seaman (.73)
# Version: v1.1
# Revised: 10/21/2017
# Copyright (c) 2017 Jon Seaman

import os
from os.path import join


# TODO: Create a function that renames all of the projects by editing .project files.

# TODO: Stop at the end of the program so that the user can see the output.

def rename_projects(working_dir):
    # Allow the user to enter a directory to work from.
    original_dir = os.getcwd()
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
            print("Writing file..." + project_filename)
            project_file = open(project_filename, mode='w')
            project_file.writelines(lines)

    # Revert change to working dir.
    os.chdir(original_dir)
    print("\nDone.")


def get_submissions_path():
    path = input("Enter the path to the submission.zip: ")
    while not os.path.isfile(path):
        print("That is not a valid file path.")
        path = input("Enter the path to the submission.zip: ")

    return path


def unzip_submission_file(path):
    import zipfile

    # Unzip the submissions file.
    working_dir = os.path.splitext(path)[0]

    with zipfile.ZipFile(path, mode="r") as submissions:
        submissions.extractall(working_dir)

    # Unzip each submission
    for filename in os.listdir(working_dir):

        filepath = os.path.join(working_dir, filename)
        if filepath.endswith(".zip"):
            with zipfile.ZipFile(filepath, mode="r") as project:
                output_folder = os.path.splitext(filepath)[0]
                print(filename + " ----> " + output_folder)
                project.extractall(output_folder)

    # Delete each submission zip
    print("Cleaning up")
    for filename in os.listdir(working_dir):

        filepath = os.path.join(working_dir, filename)
        if filepath.endswith(".zip"):
            print("X " + filepath)
            os.remove(filepath)



if __name__ == "__main__":
    # Get the path to the submissions.zip
    submissionsPath = get_submissions_path()
    # Extract that file to a working directory.
    unzip_submission_file(submissionsPath)

    # Rename the projects that were extracted.
    rename_projects(os.path.splitext(submissionsPath)[0])

    input("Press enter to exit...")
