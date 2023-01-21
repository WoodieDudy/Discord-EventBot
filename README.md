# Discord EventBot

# About
> EventBot is a simple Discord bot that logs some user activity in channel

## Clone the repo
```sh
$ git clone https://github.com/WoodieDudy/Discord-EventBot.git
$ cd Discord-EventBot
```

## Fill the env file
```sh
$ cp env.yml.example env.yml
# change token and time zone in env.yml
```

### Running with docker
If you are using podman
```sh
echo "unqualified-search-registries = [\"docker.io\"]" | sudo tee -a /etc/containers/registries.conf
```
```sh
$ docker build -t eventbot .
$ docker run -d --restart unless-stopped --name event_bot event_bot
```
