# Author: Jon Seaman (.73)
# Version: v1.2
# Revised: 10/21/2017
# Copyright (c) 2017 Jon Seaman

import os
from os.path import join

def rename_projects(working_dir):
    # Allow the user to enter a directory to work from.
    original_dir = os.getcwd()
    os.chdir(working_dir)
    print("Working in: " + os.getcwd())

    # For each dir in the current folder.
    for dir_or_file in os.listdir("."):
        rename_project(dir_or_file)
    # Revert change to working dir.
    os.chdir(original_dir)
    print("\nDone.")


def rename_project(project_dir):
    if os.path.isdir(project_dir):
        # Grab name for renaming. This happens to be the students name.
        name = project_dir.split("_")[0]
        # go into sub_dir
        directory = os.path.join(".", project_dir)
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


def get_submissions_path() -> str:
    print("Enter the path to the submission.zip: ")
    path = input("Leave blank for default value ('./submissions.zip'): ")
    while not os.path.isfile(path) and not path == "":
        print("That is not a valid file path.")
        path = input("Enter the path to the submission.zip: ")

    if path == "":
        path = "./submissions.zip"

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


def download_components_jar():
    """
    Checks if components.jar exists in the current directory
    The jar will be downloaded if not.
    """
    components_path = "./components.jar"
    components_url = "http://cse.osu.edu/software/common/components.jar"
    if not os.path.isfile(components_path):
        # Download the jar
        import urllib.request
        urllib.request.urlretrieve(components_url, components_path)


def download_workspace_template():
    """
    Verifies that the workspace template is available in the current directory.
    :return: None
    """
    ws_path = "./OsuCseWsTemplate.zip"
    ws_url = "http://cse.osu.edu/software/common/OsuCseWsTemplate.zip"
    if not os.path.isfile(ws_path):
        # Download the jar
        import urllib.request
        urllib.request.urlretrieve(ws_url, ws_path)


if __name__ == "__main__":
    # Gather dependencies
    download_components_jar()
    download_workspace_template()

    # Get the path to the submissions.zip
    submissionsPath = get_submissions_path()
    # Extract that file to a working directory.
    unzip_submission_file(submissionsPath)

    # Rename the projects that were extracted.
    rename_projects(os.path.splitext(submissionsPath)[0])

    input("Press enter to exit...")
