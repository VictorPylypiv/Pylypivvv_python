# Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
# edit_document выводит на экран информацию о том, что редактирование документов недоступно для
# бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
# # иначе Editor. Вызовите методы просмотра и редактирования документов.


class Editor:
    @staticmethod
    def view_doc():
        print('doc 1')

    def edit_doc(self):
        print("you can`t edit this document")


class ProEditor(Editor):
    def edit_doc(self):
        self.view_doc()
        if input("Enter password: ") == '123':
            print("edit document")
        else:
            super().edit_doc()


user = ProEditor()
user.edit_doc()
