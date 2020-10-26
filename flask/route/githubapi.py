import requests
from route.ghexception import githubApiError
from route.models import GithubRepo


def create_query(languages, min_stars=5000):
    query = f"stars:>{min_stars} "
    for language in languages:
        query += f"language:{language} "
    return query


def repo_with_stars(languages, sort="stars", order="desc"):
    api_url = "http://api.github.com/search/repositories"
    parameters = {
        "q": f"{create_query(languages)}", "sort": sort, "order": order}
    response = requests.get(api_url, params=parameters)

    if response.status_code != 200:
        raise githubApiError(response.status_code)
    items = response.json()["items"]
    return [GithubRepo(items["name"], items["language"], items["stargazers_count"]) for item in items] 


