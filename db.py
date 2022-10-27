import sqlite3


class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_obj(self, peer_id):
        query = self.cursor.execute(
            "SELECT obj FROM settings WHERE peer_id = ?", (peer_id,))
        result = query.fetchone()
        if not bool(len(result)):
            return False
        else:
            return int(result[0])

    def obj_write(self, peer_id, obj):
        self.cursor.execute(
            "INSERT INTO settings (peer_id, obj) VALUES (?, ?)", (peer_id, obj)
        )
        return self.conn.commit()
