class Post:
    def __init__(self, post_id:int, title='', subtitle='', body='') -> None:
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body=body