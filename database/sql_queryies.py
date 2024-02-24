CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS lists (
                    user_id INTEGER,
                    content_type TEXT,
                    content_data TEXT
                )
'''

INSERT_TABLE = ''' INSERT INTO list (user_id, content_type, content_data) VALUES (?, ?, ?) '''

SELECT_TABLE = '''SELECT content_type, GROUP_CONCAT(content_data, ', ') FROM saved_data 
                    WHERE user_id = ? GROUP BY content_type'''
