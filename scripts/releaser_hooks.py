import subprocess


def prereleaser_middle(data):
    print('Running unit tests one last time before we make a release.')
    subprocess.check_output(["python", "demo_project/manage.py", "test", "demo_project"])

    print('Running flake8 check (PEP8 conventions).')
    # See setup.cfg for configuration options.
    subprocess.check_output(["flake8"])
