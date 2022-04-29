import os
import os.path as path

from git import InvalidGitRepositoryError, Repo


def _get_testdata_repo():

    repo_path = "/tmp/legend-testdata"

    if not path.isdir(repo_path):
        os.mkdir(repo_path)

    repo = None
    try:
        repo = Repo(repo_path)
    except InvalidGitRepositoryError:
        repo = Repo.clone_from(
            "https://github.com/legend-exp/legend-testdata", repo_path
        )

    return repo_path, repo


def get_path(filename: str):

    rootdir = _get_testdata_repo()[0]
    full_path = path.abspath(path.join(rootdir, "data", filename))

    if not path.isfile(full_path):
        raise FileNotFoundError(
            f"Test file '{filename}' not found in legend-testdata repository"
        )

    return full_path
