# Discord EventBot

# About
> EventBot is a simple Discord bot that logs some user activity in channel

## How to use
We have ensured that your passwords are kept safe, so you must create an application password in order to log in. See the Google [guide](https://support.google.com/accounts/answer/185833?hl=en) for details on how to do this.

You can also use another email service. We're sure that all the popular services also provide this option and have their own guide, we suggest you look it up.

## Clone the repo
```sh
$ git clone https://github.com/WoodieDudy/Discord-EventBot.git
$ cd Discord-EventBot
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
