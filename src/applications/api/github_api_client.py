import requests
from src.config.config import CONFIG

class GitHubApiClient:
    __search_repositories = "/search/repositories"
    
    def __init__(self) -> None:
        self.token = None

    def __form_url(self, url):
        return CONFIG.get("BASE_URL_API") + url
    
    def __search_repo_url(self):
        return self.__form_url(self.__search_repositories)
    
    def login(self, username, password):
        self.__username=username
        print(f"Do login with {username}:{password}")
        self.token = "sdkfjbkjsdf"

    def logout(self):
        print(f"Do logout for {self.__username}")

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
    