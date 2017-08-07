#!/usr/bin/python

"""
Sysomos API wrapper

This is a simple wrapper for the Sysomos MAP REST API v1.0

Author - Timothy Ip
"""


import requests

__author__ = "Timothy Ip"
__version__ = "0.1"


class twitter:

    def __init__(self,api_key):
    
        self.base_url = "http://api.sysomos.com/v1/map/analytics/twitter"
        self.search_url = "http://api.sysomos.com/v1/map/search/twitter"
        self.headers = {'Accept': 'application/json' ,'Content-Type': 'application/json'}
        self.api_key = api_key
        
    def profiles(self,handles):
    
        """
        Profiles search
        
        :param handles: A list of Twitter handles for which you want to obtain profile information
        :type handles: list  
        """
    
        handles = ','.join(handles) #convert list of handles into string
        search_url = self.search_url + '/profiles/' + '?apiKey=' + self.api_key
        response_data = requests.put(search_url,data=handles,headers=self.headers)
        
        results = response_data.json()
        
        return results
        
    def search(self, query, startDate=None, endDate=None, size=None, page=None, f1=None):
    
        """
        Twitter search
        
        :param query: The text string on which to search
        :type query: string
        
        :param startDate: Restrict results to a date range, required if endDate is specfied. Valid format is YYYY-MM-DD
        :type startDate: string
        
        :param endDate: Restrict results to a date range, required if startDate is specfied. Valid format is YYYY-MM-DD
        :type endDate: string
        
        :param size: The number of items per page. Maximum value is 50,000. Default=10
        :type size: int
        
        :param page: The page of results to return. Default = 1. Intended to be used with size param for pagination. 
        :type size: int
        
        :param f1: Comma-seperated list of fields to retrieve or skip in the return body. Fields that you want to include 
            are preceded by a space . Fields to exclude by a hyphen. The following fields can be skipped/excluded:
                - Sentiment
                - Id
                - Date
                - Link
                - Author
                - Content-Type
                
                Example: '-link,-content,sentiment'
        :type f1: string
        """

        params = _params(startDate=startDate,endDate=endDate,size=size)
        if f1:
            params['f1'] = f1
        
        try:
            search_url = self.search_url + '?apiKey=' + self.api_key + '&q=' + query + "&" + "&".join(["%s=%s" %(k,v) for (k,v) in params.items()])
        except AttributeError:
            search_url = self.search_url + '?apiKey=' + self.api_key + '&q=' + query
            
        response_data = requests.get(search_url,headers=self.headers)
        results = response_data.json()
        
        return results
        
    def top_hashtags(self,query,startDate=None,endDate=None,size=None):
    
        """
        Performs search for top hashtags based on query
        
        :param query: The text string on which to search
        :type query: string
        
        :param startDate: Restrict results to a date range, required if endDate is specfied. Valid format is YYYY-MM-DD
        :type startDate: string
        
        :param endDate: Restrict results to a date range, required if startDate is specfied. Valid format is YYYY-MM-DD
        :type endDate: string
        
        :param size: The number of items per page. Maximum value is 50,000. Default=10
        :type size: int
        
        """
   
        params = _params(startDate=startDate,endDate=endDate,size=size)
           
        try:
            search_url = self.base_url + '?apiKey=' + self.api_key + '&q=' + query + "&" + "&".join(["%s=%s" %(k,v) for (k,v) in params.items()])
        except AttributeError:
            search_url = self.base_url + '?apiKey=' + self.api_key + '&q=' + query
        
        response_data = requests.get(search_url,headers=self.headers)
        results = response_data.json()
        
        return results

    def top_authority(self,query,startDate=None,endDate=None,size=None):
    
        """
        Performs search for top authority sources based on query
        
        :param query: The text string on which to search
        :type query: string
        
        :param startDate: Restrict results to a date range, required if endDate is specfied. Valid format is YYYY-MM-DD
        :type startDate: string
        
        :param endDate: Restrict results to a date range, required if startDate is specfied. Valid format is YYYY-MM-DD
        :type endDate: string
        
        :param size: The number of items per page. Maximum value is 50,000. Default=10
        :type size: int
        
        """
   
        params = _params(startDate=startDate,endDate=endDate,size=size)
           
        try:
            search_url = self.base_url + '/top_authority' + '?apiKey=' + self.api_key + '&q=' + query + "&" + "&".join(["%s=%s" %(k,v) for (k,v) in params.items()])
        except AttributeError:
            search_url = self.base_url + '/top_authority' + '?apiKey=' + self.api_key + '&q=' + query
        
        response_data = requests.get(search_url,headers=self.headers)
        results = response_data.json()
        
        return results
        
    def most_retweeted(self,query,startDate=None,endDate=None,size=None):
        
        """
        Performs search for most retweeted based on query
        
        :param query: The text string on which to search
        :type query: string
        
        :param startDate: Restrict results to a date range, required if endDate is specfied. Valid format is YYYY-MM-DD
        :type startDate: string
        
        :param endDate: Restrict results to a date range, required if startDate is specfied. Valid format is YYYY-MM-DD
        :type endDate: string
        
        :param size: The number of items per page. Maximum value is 50,000. Default=10
        :type size: int
        
        """
   
        params = _params(startDate=startDate,endDate=endDate,size=size)
   
        try:
            search_url = self.base_url + '/most_retweeted' + '?apiKey=' + self.api_key + '&q=' + query + "&" + "&".join(["%s=%s" %(k,v) for (k,v) in params.items()])
        except AttributeError:
            search_url = self.base_url + '/most_retweeted' + '?apiKey=' + self.api_key + '&q=' + query
        
        response_data = requests.get(search_url,headers=self.headers)
        results = response_data.json()
        
        return results
        
        
    def top_sources(self,query,startDate=None,endDate=None,size=None,sampleSize=None,authorityLevel=None):
        
        """
        Performs search for top sources based on query
        
        :param query: The text string on which to search
        :type query: string
        
        :param startDate: Restrict results to a date range, required if endDate is specfied. Valid format is YYYY-MM-DD
        :type startDate: string
        
        :param endDate: Restrict results to a date range, required if startDate is specfied. Valid format is YYYY-MM-DD
        :type endDate: string
        
        :param size: The number of items per page. Maximum value is 50,000. Default=10
        :type size: int
        
        :param sampleSize: The number of documents to analyze the top sources list. If not specified, default value is 10,000.
        :type sampleSize: int
        
        :param authorityLevel: The cut-off point for authority level. Default value is 5.
        :type authorityLevel: int
        
        """
   
        params = _params(startDate=startDate,endDate=endDate,size=size)
        
        if sampleSize:
            params['sampleSize'] = sampleSize
        if authorityLevel:
            params['authorityLevel'] = authorityLevel
   
        try:
            search_url = self.base_url + '/top_sources' + '?apiKey=' + self.api_key + '&q=' + query + "&" + "&".join(["%s=%s" %(k,v) for (k,v) in params.items()])
        except AttributeError:
            search_url = self.base_url + '/top_sources' + '?apiKey=' + self.api_key + '&q=' + query
        
        response_data = requests.get(search_url,headers=self.headers)
        results = response_data.json()
        
        return results
        
    def reach(self,query,startDate=None,endDate=None,size=None):
        
        """
        Performs search for most retweeted based on query
        
        :param query: The text string on which to search
        :type query: string
        
        :param startDate: Restrict results to a date range, required if endDate is specfied. Valid format is YYYY-MM-DD
        :type startDate: string
        
        :param endDate: Restrict results to a date range, required if startDate is specfied. Valid format is YYYY-MM-DD
        :type endDate: string
        
        :param size: The number of items per page. Maximum value is 50,000. Default=10
        :type size: int
        
        """
   
        params = _params(startDate=startDate,endDate=endDate,size=size)
   
        try:
            search_url = self.base_url + '/reach' + '?apiKey=' + self.api_key + '&q=' + query + "&" + "&".join(["%s=%s" %(k,v) for (k,v) in params.items()])
        except AttributeError:
            search_url = self.base_url + '/reach' + '?apiKey=' + self.api_key + '&q=' + query
        
        response_data = requests.get(search_url,headers=self.headers)
        results = response_data.json()
        
        return results

    
def _params(startDate=None,endDate=None,size=None):

    params = {}

    if startDate:
        params['startDate'] = startDate
    if endDate:
        params['endDate'] = endDate
    if size:
        params['size'] = size
        
    return params