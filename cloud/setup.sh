#!/usr/bin/env bash
# Sets up the Pryisce Engine Discord bot on a small Linux server (Debian or Ubuntu) so that it stays
# online by itself, restarts if it stops, and starts again after a reboot.
#   curl -fsSL https://raw.githubusercontent.com/pryisce/pryisce-engine/main/cloud/setup.sh | bash
set -euo pipefail

echo "Installing what the bot needs..."
sudo apt-get update -y -qq
sudo apt-get install -y -qq python3 python3-websockets curl
sudo curl -fsSL https://raw.githubusercontent.com/pryisce/pryisce-engine/main/cloud/pryisce-bot.py -o /opt/pryisce-bot.py

# The token is typed here, hidden, and kept in a file only the system can read.
read -rsp "Paste the bot token (it stays hidden) and press Enter: " TOKEN < /dev/tty
echo
if [ "${#TOKEN}" -lt 50 ]; then echo "That does not look like a bot token."; exit 1; fi
printf 'DISCORD_TOKEN=%s\n' "$TOKEN" | sudo tee /etc/pryisce-bot.env > /dev/null
sudo chmod 600 /etc/pryisce-bot.env
unset TOKEN

sudo tee /etc/systemd/system/pryisce-bot.service > /dev/null <<'UNIT'
[Unit]
Description=Pryisce Engine Discord bot (keeps it online)
After=network-online.target
Wants=network-online.target

[Service]
EnvironmentFile=/etc/pryisce-bot.env
ExecStart=/usr/bin/python3 /opt/pryisce-bot.py
Restart=always
RestartSec=10
DynamicUser=yes
NoNewPrivileges=yes
ProtectSystem=strict
ProtectHome=yes

[Install]
WantedBy=multi-user.target
UNIT

sudo systemctl daemon-reload
sudo systemctl enable --now pryisce-bot.service
sleep 8
echo "--- what the bot says ---"
sudo journalctl -u pryisce-bot.service -n 5 --no-pager || true
echo "Done. If the last line above says 'online', the bot is up and will stay up."