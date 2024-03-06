


# ------------------------------------------------------------------

start-app:
	sudo docker compose -f dockerAppConf.yaml up -d --build

start: start-app

# ------------------------------------------------------------------

restart-app:
	sudo docker compose -f dockerAppConf.yaml restart

restart: restart-app

# ------------------------------------------------------------------

down-app:
	sudo docker compose -f dockerAppConf.yaml down

down: down-app

kill-app:
	sudo docker compose -f dockerAppConf.yaml kill

kill: kill-app


# ------------------------------------------------------------------

start-gunicorn:
	gunicorn -c ./gunicorn/gunicorn.conf.py main:app