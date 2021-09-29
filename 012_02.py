class Editor:
    def view_document(self):
        print('Document 1')


    def edit_document(self):
        print('For edit get ProEditor')


class ProEditor(Editor):
    def edit_document(self):
        print("You can edit")


doc = Editor()
print(doc.view_document())
key = input("Enter key: ")
true_key = '123'

if key == true_key:
    edit = ProEditor()
else:
    edit = Editor()

print(edit.edit_document())
