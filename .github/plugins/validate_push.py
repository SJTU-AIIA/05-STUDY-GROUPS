import os
import sys
import json
from git import Repo
from github import Github
from baselib import ROOT_DIR

def validate_PR(pr_author):
    repo = Repo(".")
    modified_files = [diff.a_path for diff in repo.head.commit.diff()]
    for file_path in modified_files:
        parts = file_path.split("/")
        project_path = "/".join(parts[:-1])  # Get project folder path
        study_group = parts[0]  # Get study group name
        manifest_path = ROOT_DIR / f"{project_path}/manifest.json"
        groupinfo_path = ROOT_DIR / f"{study_group}/groupinfo.json"

        if not os.path.exists(manifest_path):
            print(f"Manifest not found in {project_path}")
            sys.exit(1)

        with open(manifest_path, "r") as f:
            manifest = json.load(f)
            allowed = manifest["authors"]
            with open(groupinfo_path, "r") as f:
                groupinfo = json.load(f)

            if pr_author not in allowed:
                if pr_author in (groupinfo["teachers"] + groupinfo["students"]):
                    # Study group member but not project author - create PR
                    create_review_pr(repo, pr_author, project_path, modified_files)
                    sys.exit(0)
                else:
                    print(f"{pr_author} not authorized to modify {project_path}")
                    sys.exit(1)

    print("All changes are authorized!")
    sys.exit(0)

def create_review_pr(repo, author, project_path, modified_files):
    """Create a PR for project owner review"""
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable not set")

    # Create new branch for the PR
    branch_name = f"review-request/{author}/{project_path.replace('/', '-')}"
    repo.git.checkout(b=f"review-request/{author}/{project_path.replace('/', '-')}")

    # Push changes
    repo.git.push("origin", branch_name)

    # Initialize GitHub API
    g = Github(github_token)
    github_repo = g.get_repo(f"{os.getenv('GITHUB_REPOSITORY')}")

    # Create PR
    pr = github_repo.create_pull(
        title=f"Review Request from {author} for {project_path}",
        body=f"""This change requires approval from project owners.
        
**Changed Files**:
{'\n'.join(f"- {f}" for f in modified_files)}

**Requested By**: @{author}
**Project Path**: {project_path}""",
        head=branch_name,
        base="main"
    )

    # Add labels and assignees
    pr.add_to_labels("needs-review")
    manifest = json.load(open(ROOT_DIR / f"{project_path}/manifest.json"))
    for owner in manifest["authors"]:
        try:
            pr.add_to_assignees(owner)
        except:
            print(f"Couldn't assign {owner}")

    print(f"Created PR #{pr.number} for review")
    print(f"::set-output name=pr_number::{pr.number}")

if __name__ == "__main__":
    validate_PR(sys.argv[1])