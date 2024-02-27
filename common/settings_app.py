from pydantic_settings import BaseSettings
from .__settings import env

from multiprocessing import cpu_count 

def max_workers():  # Определение функции max_workers
    return cpu_count()  # Возвращение количества доступных процессоров


class SettingsAPP(BaseSettings):
    # Журнал доступа и ошибок  
    accesslog: str = env.str('ACCESSLOG', default='gunicorn/access_log_gunicorn.log')
    errorlog: str = env.str('ERRORLOG', default='gunicorn/error_log_gunicorn.log') 
    
    # Таймауты
    timeout: int = env.int('TIMEOUT', default=30)
    
    # Перезагрузка и перезапуск
    reload: bool = env.bool('RELOAD', default=True)
    max_requests: int = env.int('MAX_REQUESTS', default=10000)
    max_requests_jitter: int = env.int('MAX_REQUESTS_JITTER', default=100)
    
    # Подключения и рабочие процессы
    worker_connections: int = env.int('WORKER_CONNECTIONS', default=1000)
    workers: int = env.int('WORKERS', default=max_workers())
    
    # Загрузка приложения и отладка
    preload_app: bool = env.bool('PRELOAD_APP', default=True)
    debug: bool = env.bool('DEBUG', default=False)
    loglevel: str = env.str('LOGLEVEL', default='warning')
    
    # Статистика и связывание    
    host_bind: str = env.str('HOST_BIND', default='0.0.0.0')
    port_bind: int = env.int('PORT_BIND')
    
    host_statsd_host: str = env.str('HOST_STATSD_HOST', default='0.0.0.0')
    port_statsd_host: int = env.int('PORT_STATSD_HOST')
    
    worker_class: str = env.str('WORKER_CLASS', default='gevent')
    
    @property
    def bind(self) -> str:
        return f'{self.host_bind}:{self.port_bind}'
    
    @property
    def statsd_host(self) -> str:
        return f'{self.host_statsd_host}:{self.port_statsd_host}'
    
env_app = SettingsAPP()