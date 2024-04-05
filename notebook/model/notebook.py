from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class Note:
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    code: int
    title: str
    text: str
    importance: str
    creation_date: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def __str__(self):
        return f"Code: {self.code}\nCreation date: {self.creation_date}\n{self.title}: {self.text}"

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

@dataclass
class Notebook:
    notes: Dict[str, Note] = field(default_factory=dict)
    id_control = 0

    def add_note(self, title: str, text: str, importance: str) -> str:
        self.id_control += 1
        code = self.id_control  
        new_note = Note(code=code, title=title, text=text, importance=importance)
        self.notes[code] = new_note
        return self.id_control

    def list_all_notes(self):
        for code, note in self.notes.items():
            print(f"Code: {code}")
            print(note)

    def add_tags_to_note(self, code: int, tags: List[str]):
        if code in self.notes:
            for tag in tags:
                self.notes[code].add_tag(tag)

    def important_notes(self) -> Dict[str, Note]:
        return {code: note for code, note in self.notes.items() if note.importance in ['HIGH', 'MEDIUM']}

    def delete_note(self, code: int):
        if code in self.notes:
            del self.notes[code]

    def tags_note_count(self) -> Dict[str, int]:
        tag_count = {}
        for note in self.notes.values():
            for tag in note.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count