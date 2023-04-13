import requests
from src.config.config import config

class GitHubApiClient:
    __search_repositories = "/search/repositories"
    __validation_failed = "Validation Failed"
    __message_tag = "message"
    __total_count_tag = "total_count"

    def __init__(self) -> None:
        self.token = None

    def __form_url(self, url):
        return config.get("BASE_URL_API") + url
    
    def __search_repo_url(self):
        return self.__form_url(self.__search_repositories)
    
    def login(self, username, password):
        print(f"Do login with {username}:{password}")
        self.token = "sdkfjbkjsdf"

    def logout(self, username):
        print(f"Do logout for {username}")

     #{config.get_url_api()}{search_repositories}?q=Q
    def get_search_repo_without_params(self):    
        return self.__search_repo_url()
    
    def search_repo_without_params(self):
        r = requests.get(
            url=self.__search_repo_url(),
            # headers=f"Authorization: Bearer {self.token}"
            )

        return r.json() 

    #{config.get_url_api()}{search_repositories}?q=Q
    def search_repo(self, repo_name):        
        r = requests.get(
            url=self.__search_repo_url(),
            params={'q': repo_name},
            # headers=f"Authorization: Bearer {self.token}"
            )

        return r.json()    
    