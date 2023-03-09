from uuid import uuid4
from datetime import date


class Note:

    def __init__(self, title: str, text: str, id=uuid4(), date=date.today()) -> None:
        self.id = id
        self.title = title
        self.text = text
        self.date = date

    def __str__(self) -> str:
        return "Id: "+str(self.id) + "\nTitle: " + self.title + "\nDate: " + str(self.date) + "\nText: " + self.text
