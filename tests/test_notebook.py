from datetime import datetime

import pytest
import inspect


from notebook.model import notebook as notebook_module

module_members = [item[0] for item in inspect.getmembers(notebook_module)]
class_note_defined = "Note" in module_members
class_notebook_defined = "Notebook" in module_members

if class_note_defined:
    from notebook.model.notebook import Note

if class_notebook_defined:
    from notebook.model.notebook import Notebook


@pytest.fixture
def note():
    return Note(1, "note 1", "note 1 text", Note.HIGH)


@pytest.fixture
def empty_notebook():
    return Notebook()


@pytest.fixture
def notebook_with_notes():
    notebook = Notebook()
    notebook.add_note("note 1", "note 1 text", Note.HIGH)
    notebook.add_note("note 2", "note 2 text", Note.MEDIUM)
    notebook.add_note("note 3", "note 3 text", Note.LOW)
    notebook.notes[1].add_tag("tag1")
    notebook.notes[1].add_tag("tag2")
    notebook.notes[2].add_tag("tag1")
    notebook.notes[3].add_tag("tag2")
    return notebook


@pytest.mark.xfail(not class_note_defined, reason="Note class not defined")
def test_note_class_decorated_with_dataclass(note):
    assert hasattr(note, "__dataclass_params__")


@pytest.mark.xfail(not class_note_defined, reason="Note class not defined")
@pytest.mark.parametrize(
    "constant_name, constant_value", [("HIGH", "HIGH"), ("MEDIUM", "MEDIUM"), ("LOW", "LOW")]
)
def test_note_class_has_constants(note, constant_name, constant_value):
    assert hasattr(note, constant_name)
    assert getattr(note, constant_name) == constant_value


@pytest.mark.xfail(not class_note_defined, reason="Note class not defined")
@pytest.mark.parametrize(
    "attribute_name, attribute_type",
    [("code", int), ("title", str), ("text", str), ("importance", str), ("creation_date", datetime), ("tags", list)]
)
def test_note_class_has_attributes(note, attribute_name, attribute_type):
    assert hasattr(note, attribute_name)
    assert isinstance(getattr(note, attribute_name), attribute_type)


@pytest.mark.xfail(not class_note_defined, reason="Note class not defined")
def test_note_class_has_add_tag_method(note):
    assert hasattr(note, "add_tag")
    assert callable(getattr(note, "add_tag"))


@pytest.mark.xfail(not class_note_defined, reason="Note class not defined")
def test_note_class_initializes_attributes(note):
    assert note.code == 1
    assert note.title == "note 1"
    assert note.text == "note 1 text"
    assert note.importance == Note.HIGH
    assert note.creation_date
    assert note.tags == []


@pytest.mark.xfail(not class_note_defined, reason="Note class not defined")
def test_note_class_add_tag_method_adds_tag(note):
    note.add_tag("tag1")
    assert "tag1" in note.tags
    note.add_tag("tag2")
    assert "tag2" in note.tags
    note.add_tag("tag1")
    assert len(note.tags) == 2


@pytest.mark.xfail(not class_note_defined, reason="Note class not defined")
def test_note_class_str_method(note):
    note_str = str(note)
    assert "Code: 1" in note_str
    assert "Creation date: " in note_str
    assert "note 1: note 1 text" in note_str


@pytest.mark.xfail(not class_notebook_defined, reason="Notebook class not defined")
def test_notebook_class_has_notes_attribute(empty_notebook):
    assert hasattr(empty_notebook, "notes")
    assert isinstance(empty_notebook.notes, dict)


@pytest.mark.xfail(not class_notebook_defined, reason="Notebook class not defined")
@pytest.mark.parametrize(
    "method_name, expected_return_type, args",
    [("add_note", int, ("note 1", "note 1 text", "HIGH")),
     ("important_notes", list, ()),
     ("tags_note_count", dict, ())]
)
def test_notebook_class_has_method(empty_notebook, method_name, expected_return_type, args):
    assert hasattr(empty_notebook, method_name)
    assert callable(getattr(empty_notebook, method_name))
    method = getattr(empty_notebook, method_name)
    assert isinstance(method(*args), expected_return_type)


@pytest.mark.xfail(not class_notebook_defined, reason="Notebook class not defined")
def test_notebook_class_add_note(empty_notebook):
    assert empty_notebook.notes == {}
    note_code = empty_notebook.add_note("note 1", "note 1 text", "HIGH")
    assert note_code == 1
    assert len(empty_notebook.notes) == 1
    note = empty_notebook.notes[note_code]
    assert note.title == "note 1"
    assert note.text == "note 1 text"
    assert note.importance == Note.HIGH


@pytest.mark.xfail(not class_notebook_defined, reason="Notebook class not defined")
def test_notebook_class_important_notes(notebook_with_notes):
    important_notes = notebook_with_notes.important_notes()
    assert len(important_notes) == 2
    assert all(note.importance in ["HIGH", "MEDIUM"] for note in important_notes)


@pytest.mark.xfail(not class_notebook_defined, reason="Notebook class not defined")
def test_notebook_class_tags_note_count(notebook_with_notes):
    tag_count = notebook_with_notes.tags_note_count()
    assert tag_count == {"tag1": 2, "tag2": 2}
