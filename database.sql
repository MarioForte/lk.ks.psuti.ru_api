--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Чт окт. 27 14:04:24 2022
--
-- Использованная кодировка текста: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: settings
CREATE TABLE settings (peer_id INTEGER UNIQUE NOT NULL, obj VARCHAR (2) NOT NULL);

-- Индекс: sqlite_autoindex_settings_1
CREATE INDEX sqlite_autoindex_settings_1 ON settings (peer_id COLLATE BINARY);

-- Индекс: sqlite_autoindex_settings_2
CREATE INDEX sqlite_autoindex_settings_2 ON settings (obj COLLATE BINARY);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
