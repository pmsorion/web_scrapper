import bs4
import requests

from common import config

class HomePage:

    def __init__(self, job_site_uid, url):
        self.__config = config()['job_site'][job_site_uid]
        self._queries = self.__config['queries']
        self._html = None

        self._visit(url)

    @property
    def job_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_job_company']):
            if link and link.has_attr('href'):
                link_list.append(link)
        
        return set(link['href'] for link in link_list)

    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')