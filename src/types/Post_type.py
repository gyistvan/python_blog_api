class Post:
    def __init__(
        self,
        id,
        title,
        created_at,
        image_url,
        short_text,
        long_text,
        author_id,
        author_name,
    ):
        self.id = id
        self.title = title
        self.created_at = created_at
        self.image_url = image_url
        self.short_text = short_text
        self.long_text = long_text
        self.author_id = author_id
        self.author_name = author_name
