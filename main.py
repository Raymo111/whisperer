import time
import zenon
import random
import sys
import os

token = os.getenv('DISCORD_TOKEN')


def broadcast(users: dict, message: str, dry_run: bool = True):
	for user in users:
		msg = message.format(name=users[user])
		print(f'Sending "{msg}" to {user}')
		if not dry_run:
			client.send_message(user, msg)
			time.sleep(0.5 + float(random.randrange(0, 300)) / 100)


if __name__ == '__main__':
	client = zenon.Client(token)
	d = {}
	with open(
		# '/home/raymo/Downloads/Discord test.tsv'
		'/home/raymo/raymocloud/Documents/Discord Christmas Card.tsv'
		, 'r') as f:
		for line in f.readlines():
			l = line.strip().split('\t')
			if l[0] == 'd':
				d[l[1]] = l[3 if len(l) > 3 else 2]
			else:
				print(f"{l[2]}" + (f"({l[3]})" if len(l) > 3 else "") + " skipped", file=sys.stderr)
	# print(d)
	broadcast(d, "Hey {name}! :slight_smile:"  # , dry_run=False
	          )
