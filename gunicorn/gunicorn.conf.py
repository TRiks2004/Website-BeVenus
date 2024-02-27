from common import env_app


# Журнал доступа и ошибок
accesslog = env_app.accesslog  # Путь к файлу журнала доступа
errorlog = env_app.errorlog    # Путь к файлу журнала ошибок  

# Таймауты
timeout = env_app.timeout  # Таймаут соединения в секундах

# Перезагрузка и перезапуск
reload = env_app.reload  # Автоматическая перезагрузка приложения при изменениях в коде
max_requests = env_app.max_requests  # Максимальное количество запросов, обрабатываемых каждым рабочим процессом перед его перезагрузкой
max_requests_jitter = env_app.max_requests_jitter  # Допустимый разброс в количестве запросов до перезапуска рабочего процесса

# Подключения и рабочие процессы
worker_connections = env_app.worker_connections  # Максимальное количество соединений для каждого рабочего процесса
workers = env_app.workers  # Количество рабочих процессов, вычисляемое с помощью функции max_workers()

# Загрузка приложения и отладка
preload_app = env_app.preload_app  # Загрузка приложения в память перед запуском рабочих процессов
debug = env_app.debug  # Отключение режима отладки
loglevel = env_app.loglevel  # Уровень журналирования `warning` | `debug` 

# Статистика и связывание
statsd_host = env_app.statsd_host  # Адрес хоста для отправки статистики в StatsD
bind = env_app.bind  # Адрес, к которому привязывается сервер Gunicorn

worker_class = env_app.worker_class  # Класс рабочего процесса
