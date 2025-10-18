class User:
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id

    def __repr__(self):
        return f"<id = {self.id}, user_id = {self.user_id}>"

    def add_session(self):
        pass


class URL:
    def __init__(self, id, user_id, url, short_code, updated_at):
        self.id = id
        self.user_id = user_id
        self.url = url
        self.short_code = short_code
        self.updated_at = updated_at

    def __repr__(self):
        return f"<id = {self.id}, url = {self.url}, short code = {self.short_code}, user_id = {self.user_id}>"

    def short_url(self):
        pass
