import http.client
import json
import requests
import pandas as pd


class HelperRaveleryAPIs:
    '''
    A helper class for interacting with the Revelry API.

    This class provides several helper functions for retrieving data from the Revelry API, including get_favorites, get_queue, get_patterns, and get_color_families. 
    Each function uses the `requests` library to send HTTP requests to the API and retrieve information.
    '''

    def __init__(self, authUsername:str, authPassword:str):
        '''
        Initialize a new object of type <ClassName> with the given authentication credentials.

        Args:
            authUsername (str): The username to be used for authentication.
            authPassword (str): The password to be used for authentication.

        Returns:
            None
        '''
        self.authUsername = authUsername
        self.authPassword = authPassword
     
   
    def get_color_families(self) -> pd.core.frame.DataFrame:
        '''
        Retrieve a list of available color families from the Ravelry API and return as a pandas dataframe.

        Returns:
            pd.DataFrame: A dataframe containing information about each color family.
        '''
        #define URL
        url = 'https://api.ravelry.com/color_families.json'      
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        #return a dataframe of the output
        return pd.DataFrame.from_records(json.loads(r1.text)['color_families'])
    
    
    def get_patterns(self, query = '', page = 1, page_size = 100, craft = 'knitting') -> pd.core.frame.DataFrame:
        '''
        Retrieve a list of patterns from the Ravelry API that match the given search query and return as a pandas dataframe.

        Args:
            query (str, optional): The search query to use when searching for patterns. Defaults to an empty string.
            page (int, optional): The page number of the results to return. Defaults to 1.
            page_size (int, optional): The number of results to return per page. Defaults to 100.
            craft (str, optional): The type of craft to search for patterns. Defaults to 'knitting'.

        Returns:
            pd.DataFrame: A dataframe containing a list of patterns.
        '''
        #define URL
        url = 'https://api.ravelry.com/patterns/search.json?query={}&page={}&page_size={}&craft={}'.format(query, page, page_size, craft)  
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        #return a dataframe of the output
        return pd.DataFrame.from_records(json.loads(r1.text)['patterns'])
    
    
    def get_queue(self, rav_username = 'rieslingm', query = '', page = 1, page_size = 100) -> pd.core.frame.DataFrame:
        ''''
        Retrieve a list of queued projects from the Ravelry API for the specified Ravelry username and return as a pandas dataframe.

        Args:
            rav_username (str, optional): The Ravelry username to retrieve the queued projects for. Defaults to 'rieslingm'.
            query (str, optional): The search query to use when searching for queued projects. Defaults to an empty string.
            page (int, optional): The page number of the results to return. Defaults to 1.
            page_size (int, optional): The number of results to return per page. Defaults to 100.

        Returns:
            pd.DataFrame: A dataframe containing information about each queued project.
        '''
        #define URL
        url = 'https://api.ravelry.com/people/{}/queue/list.json?query={}&page={}&page_size={}'.format(rav_username, query, page, page_size) 
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        #return a dataframe of the output
        return pd.DataFrame.from_records(json.loads(r1.text)['queued_projects'])
    
    
    # Note: This has to be authenticated credentials and we have only read only credentials so this will not work. However, it serves as a playground for debugging. 
    def get_favorites(self, rav_username = 'rieslingm', types = 'patterns', query = '', deep_search = '', page = 1, page_size = 100) -> list:
        '''
        Retrieve a list of favorites from the Ravelry API for the specified Ravelry username and return as a list.

        Args:
            rav_username (str, optional): The Ravelry username to retrieve the favorites for. Defaults to 'rieslingm'.
            types (str, optional): The types of favorites to retrieve. Can be one of 'patterns', 'projects', 'yarns', or 'stash'. Defaults to 'patterns'.
            query (str, optional): The search query to use when searching for favorites. Defaults to an empty string.
            deep_search (str, optional): Whether to perform a deep search or not. Can be one of 'true', 'false', or an empty string. Defaults to an empty string.
            page (int, optional): The page number of the results to return. Defaults to 1.
            page_size (int, optional): The number of results to return per page. Defaults to 100.

        Returns:
            list: A list containing information about each favorite for the specified Ravelry username and type, including its name, URL, and other details.
        '''
        #define URL
        url = 'https://api.ravelry.com/people/{}/favorites/list.json?types={}&query={}&deep_search={}&page={}&page_size={}'.format(rav_username, types, query, deep_search, page, page_size) 
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        
        print(r1.text)
       
        return json.loads(r1.text)[types]
 