import requests
from urllib.parse import quote_plus

class DolibarrAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url.rstrip('/') + '/'
        self.api_key = api_key
        self.headers = {
            'DOLAPIKEY': self.api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def request(self, method, endpoint, data=None):
        url = self.base_url + endpoint.lstrip('/')
        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=self.headers,
                json=data
            )
            return {
                'http_code': response.status_code,
                'error': None if response.ok else response.text,
                'data': response.json() if response.content else None
            }
        except requests.RequestException as e:
            return {
                'http_code': None,
                'error': str(e),
                'data': None
            }

    def get(self, endpoint):
        return self.request('GET', endpoint)

    def post(self, endpoint, data):
        return self.request('POST', endpoint, data)

    def put(self, endpoint, data):
        return self.request('PUT', endpoint, data)

    def delete(self, endpoint, data):
        return self.request('DELETE', endpoint, data)

class TicketAPI:
    def __init__(self, api: DolibarrAPI):
        self.api = api

    def get(self):
        return self.api.get('tickets')['data']

    def getById(self, id: int):
        return self.api.get('tickets/'+str(id))['data']

    def post(self, ticket):
        return self.api.post('tickets', ticket)

    def put(self, ticket):
        if 'id' not in ticket:
            raise ValueError("Ticket must contain 'id' to update.")
        return self.api.put(f"tickets/{ticket['id']}", ticket)

    def delete(self, ticket):
        if 'id' not in ticket:
            raise ValueError("Ticket must contain 'id' to delete.")
        return self.api.delete(f"tickets/{ticket['id']}", ticket)

    def filter(self, sqlfilters: list):
        raw_filter = ' and '.join([f"({f})" for f in sqlfilters])
        query = f"sqlfilters={quote_plus(raw_filter)}"
        endpoint = f"tickets?{query}"
        return self.api.get(endpoint)['data']

class UserAPI:
    def __init__(self, api: DolibarrAPI):
        self.api = api

    def get(self):
        return self.api.get('users')['data']
    
    def getById(self, id: int):
        return self.api.get('users/'+str(id))['data']

    def post(self, user):
        return self.api.post('users', user)

    def put(self, user):
        if 'id' not in user:
            raise ValueError("User must contain 'id' to update.")
        return self.api.put(f"users/{user['id']}", user)

    def delete(self, user):
        if 'id' not in user:
            raise ValueError("User must contain 'id' to delete.")
        return self.api.delete(f"users/{user['id']}", user)
    
    def filter(self, sqlfilters: list):
        raw_filter = ' and '.join([f"({f})" for f in sqlfilters])
        query = f"sqlfilters={quote_plus(raw_filter)}"
        endpoint = f"users?{query}"
        return self.api.get(endpoint)['data']


