from notebook.model.notebook import Notebook, Note


class Console:

    def __init__(self, notebook: Notebook):
        self.notebook: Notebook = notebook

    @staticmethod
    def show_welcome_msg():
        print("============================")
        print("WELCOME TO THE NOTEBOOK APP")
        print("============================")

    @staticmethod
    def show_menu():
        print("\nOPTIONS:")
        print("1. Add new note")
        print("2. List all notes")
        print("3. Add tags to note")
        print("4. List important notes")
        print("5. Delete note")
        print("6. Show notes count")
        print("7. Exit program")
        option = int(input("Enter an option: "))
        while option not in range(1, 8):
            print(">>> ERROR: Invalid option. Try again")
            option = int(input("Enter an option: "))
        return option

    def app_loop(self):
        Console.show_welcome_msg()
        end_app: bool = False
        while not end_app:
            option: int = Console.show_menu()
            end_app = self.process_user_option(option)

    def process_user_option(self, option: int) -> bool:
        if option == 1:
            self.add_new_note()
        elif option == 2:
            self.list_notes()
        elif option == 3:
            self.add_tags_to_note()
        elif option == 4:
            self.list_important_notes()
        elif option == 5:
            self.delete_note()
        elif option == 6:
            self.show_notes_count()
        elif option == 7:
            self.exit_app()
            return True

        return False

    @staticmethod
    def exit_app():
        print("======================")
        print("=== END OF PROGRAM ===")
        print("======================")

    def show_notes_count(self):
        print("\n=== SHOW NOTES COUNT ===\n")
        tags_count = self.notebook.tags_note_count()
        for tag, count in tags_count.items():
            print(f"- Tag '{tag}' has {count} notes")

    def delete_note(self):
        print("\n=== DELETE NOTE ===\n")
        self.list_notes()
        note_code: int = int(input("Enter note code: "))
        try: 
            del self.notebook.notes[note_code]
            print(f"Note with code {note_code} has been deleted")
        except:
            print("The Code does not exist")

    def list_important_notes(self):
        print("\n=== IMPORTANT NOTES ===")
        important_notes = self.notebook.important_notes()
        if len(important_notes) > 0:
            for note in important_notes:
                # print(f"code: {note}")
                print(self.notebook.notes[note])
                print(f"importance: {self.notebook.notes[note].importance}")
                print()
        else:
            print("No items to show")

    def add_tags_to_note(self):
        print("\n=== ADD TAGS TO NOTE ===\n")
        self.list_notes()
        # try: 
        note_code: int = int(input("Enter note code: "))
        tags: str = input("Enter tags separated by comma: ")
        for tag in tags.split(","):
            self.notebook.notes[note_code].add_tag(tag)
        print(f"Tags were added successfully to note with code {note_code}")
        # except:
        #     print("The Code does not exist")

    def list_notes(self):
        print("\n=== NOTES LIST ===")
        if len(self.notebook.notes) > 0:
            for note in self.notebook.notes.values():
                print(note)
                print()
        else:
            print("No items to show")

    def add_new_note(self):
        print("\n=== ADD NEW NOTE ===")
        title: str = input("Enter title: ")
        description: str = input("Enter note text: ")
        importance_options = [Note.LOW, Note.MEDIUM, Note.HIGH]
        importance: int = int(input("Enter importance - (0) LOW, (1) MEDIUM, (2) HIGH: "))
        code_id = self.notebook.add_note(title, description, importance_options[importance])
        print(f"A note was created successfully with code {code_id}")
