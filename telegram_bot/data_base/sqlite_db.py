import sqlite3 as sq
from create_bot import bot

def sql_start():
	global base, cur
	base = sq.connect('Interesting_Places.db')
	cur = base.cursor()
	if base:
		print('База данных подключена')
	base.execute('CREATE TABLE IF NOT EXISTS places(img TEXT, name TEXT PRIMARY KEY, open_hours TEXT ,description TEXT)')
	base.commit()


async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO places VALUES (?, ?, ?, ?)', tuple(data.values()))
		base.commit()


async def sql_read(message):
	for ret in cur.execute('SELECT * FROM places').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n*Открыто:* {ret[2]}\n*Описание:* {ret[3]}', parse_mode="Markdown")


async def sql_read2():
	return cur.execute('SELECT * FROM places').fetchall()


async def sql_delete_command(data):
	cur.execute('DELETE FROM places WHERE name == ?', (data,))
	base.commit()