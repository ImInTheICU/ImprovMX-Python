import requests
from typing import Union
from requests.auth import HTTPBasicAuth 

class ImprovMX:
    def __init__(self, api_user: str = "api", api_key: str = "api_key") -> None:
        """
        Initializes an instance of the class with the provided API user and API key.

        Args:
            api_user (str, optional): The username or identifier for accessing the API.
                Defaults to "api" <- api is the default user name for ImprovMX's api might change so i added a argument for it.
            api_key (str, optional): The authentication key or token for accessing the API.
        Raises:
            ValueError: If either `api_user` or `api_key` is not a string.
        """

        # Chekcs
        if not isinstance(api_user, str) or not api_user.strip():
            raise ValueError("API user must be a non-empty string.")
        
        if not isinstance(api_key, str) or not api_key.strip():
            raise ValueError("API key must be a non-empty string.")
        
        # User Defines
        self.api_user = api_user
        self.api_key = api_key

        # Built-In Defines 
        self.base_url = "https://api.improvmx.com/v3"
        self.session = requests.Session()

        self.__author__ = "PinguLovesYou (https://github.com/ImInTheICU)"
        self.__license__ = "MIT"
        self.__version__ = "0.0.1"


    def list_aliases(self, domain: str = "example.com") -> dict:
        """
        Retrieves a list of aliases for the specified domain.

        Args:
            domain (str, optional): The domain for which to retrieve aliases.

        Raises:
            ValueError: If `domain` is not a string or if it does not match any of the domains linked over at ImprovMX.

        Returns:
            dict: A dictionary containing the list of aliases.
        """

        # Checks
        if not isinstance(domain, str):
            raise ValueError("Domain must be a string.")

        # Request
        response = self.session.request(
            method="GET", 
            url=f"{self.base_url}/domains/{domain}/aliases", 
            auth=HTTPBasicAuth(self.api_user, self.api_key),
            cookies=self.session.cookies,
            headers=self.session.headers
        )
        response.raise_for_status()

        return response.json()


    def create_alias(self, domain: str = "example.com", alias: Union[str, list] = "test", forward: str = "example@test.com", bulk: bool = False, bulkBehavior: str = None) -> dict:
        """
        Creates an alias for the specified domain.

        Args:
            domain (str, optional): The domain for which to create the alias.
            alias (Union[str, list], optional): The alias or list of aliases to be created. 
                If `bulk` is False, it should be a string. If `bulk` is True, it should be a list of strings. 
                Defaults to "test".
            forward (str): The email address the alias forwards to.
            bulk (bool, optional): Indicates whether to create aliases in bulk. Defaults to False.
            bulkBehavior (str, optional): The behavior when creating aliases in bulk. 
                Can be "add" or "update". Defaults to None.

        Raises:
            ValueError: If input validation fails for any of the parameters.

        Returns:
            dict: A dictionary containing the response from the API.
        """

        # Checks
        if not isinstance(domain, str):
            raise ValueError("Domain must be a string.")
        if not isinstance(forward, str):
            raise ValueError("Forward must be a string.")
        if bulkBehavior not in (None, "add", "update"):
            raise ValueError("bulkBehavior must be None, 'add', or 'update'.")
        if bulk and not isinstance(alias, list):
            raise ValueError("Alias must be a list if bulk is True.")
        if not bulk and not isinstance(alias, str):
            raise ValueError("Alias must be a string if bulk is False.")

        # Request
        payload_key = "aliases" if bulk else "alias"
        payload_value = alias if bulk else [alias]

        url = f"{self.base_url}/domains/{domain}/aliases" if not bulk else f"{self.base_url}/domains/{domain}/aliases/bulk"

        json_payload = {
            payload_key: payload_value,
            "forward": forward
        }
        if bulkBehavior:
            json_payload["behavior"] = bulkBehavior

        response = self.session.request(
            method="POST", 
            url=url,
            cookies=self.session.cookies,
            headers=self.session.headers,
            auth=HTTPBasicAuth(self.api_user, self.api_key),
            json=json_payload
        )
        response.raise_for_status()

        return response.json()


    def edit_alias(self, domain: str = "example.com", alias: str = "test", forward: str = "example@test.com") -> dict:
        """
        Edits an existing alias for the specified domain.

        Args:
            domain (str, optional): The domain for which the alias belongs.
            alias (str, optional): The existing alias to be edited.
            forward (str): The new email address the edited alias forwards to.

        Raises:
            ValueError: If input validation fails for any of the parameters.

        Returns:
            dict: A dictionary containing the response from the API.
        """

        # Checks
        if not isinstance(domain, str):
            raise ValueError("Domain must be a string.")
        if not isinstance(alias, str):
            raise ValueError("Alias must be a string.")
        if not isinstance(forward, str):
            raise ValueError("Forward must be a string.")

        # Request
        response = self.session.request(
            method="PUT", 
            url=f"{self.base_url}/domains/{domain}/aliases/{alias}", 
            cookies=self.session.cookies,
            headers=self.session.headers,
            auth=HTTPBasicAuth(self.api_user, self.api_key),
            json={"forward": forward}
        )
        response.raise_for_status()

        return response.json()


    def delete_alias(self, domain: str = "example.com", alias: str = "test") -> dict:
        """
        Deletes an existing alias for the specified domain.

        Args:
            domain (str, optional): The domain from which to delete the alias.
            alias (str, optional): The existing alias to be deleted.

        Raises:
            ValueError: If either `domain` or `alias` is not a string.

        Returns:
            dict: A dictionary containing the response from the API.
        """

        # Checks
        if not isinstance(domain, str):
            raise ValueError("Domain must be a string.")
        if not isinstance(alias, str):
            raise ValueError("Alias must be a string.")

        # Request
        response = self.session.request(
            method="DELETE", 
            url=f"{self.base_url}/domains/{domain}/aliases/{alias}", 
            cookies=self.session.cookies,
            headers=self.session.headers,
            auth=HTTPBasicAuth(self.api_user, self.api_key),
        )
        response.raise_for_status()

        return response.json()
