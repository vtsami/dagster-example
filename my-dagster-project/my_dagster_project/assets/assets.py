from dagster import asset
from github import Github

ACCESS_TOKEN = "ghp_YOUR_TOKEN_HERE"

@asset
def github_stargazers():
    return list(Github(ACCESS_TOKEN).get_repo("dagster-io/dagster").get_stargazers_with_dates())
