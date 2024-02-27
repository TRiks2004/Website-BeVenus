


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

# ------------------------------------------------------------------