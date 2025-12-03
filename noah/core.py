import requests
from . import config 

class NoahSDK:
    def __init__(self, api_code: str):
        if not api_code:
            raise ValueError(config.ERROR_MESSAGES['MISSING_KEY'])
            
        self.api_code = api_code
        print(f"Noah's SDK inicializada e pronta para {config.API_BASE_URL}")

    def _prepare_request(self, method: str, endpoint: str, payload: dict = None):
        url = f"{config.API_BASE_URL}/{endpoint}"
        
        headers = config.DEFAULT_HEADERS.copy()
        headers["Authorization"] = f"Bearer {self.api_code}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=config.DEFAULT_TIMEOUT_SECONDS)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=payload, timeout=config.DEFAULT_TIMEOUT_SECONDS)
            else:
                raise ValueError(f"Método HTTP '{method}' não suportado pela SDK.")
            
            response.raise_for_status() 
            
            return response.json() if response.content else {"status": "success", "message": "Operação concluída com sucesso."}
            
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            error_message = config.ERROR_MESSAGES.get(status_code, f"Erro HTTP: {status_code}")
            return {"error": error_message, "status": status_code}
            
        except requests.exceptions.RequestException as e:
            return {"error": "Falha na conexão de rede.", "details": str(e)}

    def get_data(self, endpoint: str):
        return self._prepare_request('GET', endpoint)

    def post_data(self, endpoint: str, payload: dict):
        return self._prepare_request('POST', endpoint, payload=payload)