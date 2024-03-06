from common import env_gunicorn as gunicorn_settings


# Журнал доступа и ошибок
accesslog = gunicorn_settings.accesslog  # Путь к файлу журнала доступа
errorlog = gunicorn_settings.errorlog    # Путь к файлу журнала ошибок  

# Таймауты
timeout = gunicorn_settings.timeout  # Таймаут соединения в секундах

# Перезагрузка и перезапуск
reload = gunicorn_settings.reload  # Автоматическая перезагрузка приложения при изменениях в коде
max_requests = gunicorn_settings.max_requests  # Максимальное количество запросов, обрабатываемых каждым рабочим процессом перед его перезагрузкой
max_requests_jitter = gunicorn_settings.max_requests_jitter  # Допустимый разброс в количестве запросов до перезапуска рабочего процесса

# Подключения и рабочие процессы
worker_connections = gunicorn_settings.worker_connections  # Максимальное количество соединений для каждого рабочего процесса
workers = gunicorn_settings.workers  # Количество рабочих процессов, вычисляемое с помощью функции max_workers()

# Загрузка приложения и отладка
preload_app = gunicorn_settings.preload_app  # Загрузка приложения в память перед запуском рабочих процессов
debug = gunicorn_settings.debug  # Отключение режима отладки
loglevel = gunicorn_settings.loglevel  # Уровень журналирования `warning` | `debug` 

# Статистика и связывание
statsd_host = gunicorn_settings.statsd_host  # Адрес хоста для отправки статистики в StatsD
bind = gunicorn_settings.bind  # Адрес, к которому привязывается сервер Gunicorn

worker_class = gunicorn_settings.worker_class  # Класс рабочего процесса
