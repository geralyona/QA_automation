import pytest
import requests
from src.config.config import CONFIG
from src.libraries.helpers import *

search_repositories = "/search/repositories"
validation_failed = "Validation Failed"
message_tag = "message"
total_count_tag = "total_count"

def test_existing_repo_can_be_found(github_api_client):
    #login
    # token = requests.post(url="https://api.github.com/login", data={
    #     "username": 'kjsdkjf',
    #     'password': 'sdlkfnkjsdnf'
    #     }
    # )

    body = github_api_client.search_repo("Q")
    assert body[total_count_tag] > 0

#@pytest.mark.usefixtures("github_api_client")
def test_non_existing_repo_cannot_be_found(github_api_client):    
    repo_name = get_random_string(20)
    print("Repository unexisted name is "+repo_name)
    body = github_api_client.search_repo(repo_name)

    assert body[total_count_tag] <= 0


def test_search_not_working_without_q(github_api_client):
    body = github_api_client.search_repo_without_params()
    assert body[message_tag] == validation_failed

def test_search_not_working_with_not_q(github_api_client):
    character = get_random_letter("q")
    body = requests.get(
        url=f"{github_api_client.get_search_repo_without_params()}?{character}={character}"
        )
    assert body.json()[message_tag] == validation_failed

def test_existing_repo_can_be_found_by_name(github_api_client):   
    repo_name = get_random_string(3)
    print("Repository name contains "+repo_name)    
    body = github_api_client.search_repo(f"{repo_name}+in%3Aname&type=Repositories")

    assert body[total_count_tag] > 0

