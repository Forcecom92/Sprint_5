from main import BooksCollector
import pytest

class TestBooksCollector:


    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Предупреждение и зомби')
        assert 'Предупреждение и зомби' in collector.books_genre

    @pytest.mark.parametrize('name', ['', 'Предупреждение' *10])
    def test_add_new_invalid_book(self, name):
        collector2 = BooksCollector()
        collector2.add_new_book(name)
        assert len(collector2.books_genre) == 0

    def test_add_same_book(self):
        collector3 = BooksCollector()
        collector3.add_new_book('Предупреждение и зомби')
        collector3.add_new_book('Предупреждение и зомби')
        assert len(collector3.books_genre) == 1


    def test_set_book_genre(self):
        collector4 = BooksCollector()
        collector4.add_new_book('Предупреждение и зомби')
        collector4.set_book_genre('Предупреждение и зомби', 'Ужасы')
        assert collector4.books_genre ['Предупреждение и зомби'] == 'Ужасы'

    @pytest.mark.parametrize('name, genre', [['Предупреждение и зомби', 'Роман'], ['', 'Мульфильмы']])
    def test_set_book_invalid_genre(self, name, genre):
        collector5 = BooksCollector()
        collector5.add_new_book('Предупреждение и зомби')
        collector5.set_book_genre('Предупреждение и зомби', 'Ужасы')
        collector5.set_book_genre(name, genre)
        assert collector5.books_genre ['Предупреждение и зомби'] == 'Ужасы'


    def test_get_books_with_specific_genre(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Автостопом по галактике')
        collector7.set_book_genre('Автостопом по галактике', 'Фантастика')
        books = collector7.get_books_with_specific_genre('Фантастика')
        assert "Автостопом по галактике" in books

    def test_get_books_for_children(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Автостопом по галактике')
        collector8.add_new_book('Философия в будуаре')
        collector8.set_book_genre('Автостопом по галактике', 'Фантастика')
        collector8.set_book_genre('Философия в будуаре', 'Ужасы')
        children_books = collector8.get_books_for_children()
        assert "Автостопом по галактике" in children_books

    @pytest.mark.parametrize('invalid_genre', ['Ужасы', 'Детективы'])
    def test_get_invalid_books_for_children(self, invalid_genre):
        collector8 = BooksCollector()
        collector8.add_new_book('Автостопом по галактике')
        collector8.add_new_book('Философия в будуаре')
        collector8.set_book_genre('Автостопом по галактике', 'Фантастика')
        collector8.set_book_genre('Философия в будуаре', invalid_genre)
        children_books = collector8.get_books_for_children()
        assert "Философия в будуаре" not in children_books

    def test_add_book_in_favorites(self):
        collector9 = BooksCollector()
        collector9.add_new_book('Холодное сердце')
        collector9.add_book_in_favorites('Холодное сердце')
        assert 'Холодное сердце' in collector9.get_list_of_favorites_books()


    def test_delete_book_in_favorites(self):
        collector10 = BooksCollector()
        collector10.add_new_book('Холодное сердце')
        collector10.add_book_in_favorites('Холодное сердце')
        collector10.delete_book_from_favorites('Холодное сердце')
        assert 'Холодное сердце' not in collector10.get_list_of_favorites_books()









