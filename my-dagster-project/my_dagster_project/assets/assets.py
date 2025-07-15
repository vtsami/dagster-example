from dagster import asset
from github import Github

ACCESS_TOKEN = "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"

@asset
def github_stargazers():
    return list(Github(ACCESS_TOKEN).get_repo("dagster-io/dagster").get_stargazers_with_dates())
