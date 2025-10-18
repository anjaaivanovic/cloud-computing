package com.cloud.docker_compose_assignment.service;

import com.cloud.docker_compose_assignment.dto.BookDTO;
import com.cloud.docker_compose_assignment.model.Book;
import com.cloud.docker_compose_assignment.repository.BookRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class BookService {
    private final BookRepository bookRepository;

    public BookService(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }

    public List<Book> findAll() { return bookRepository.findAll(); }

    public Optional<Book> findById(Long id) { return bookRepository.findById(id); }

    public Book create(BookDTO book) {
        Book bookToSave = new Book(
                book.title(),
                book.author(),
                book.yearPublished()
        );

        return bookRepository.save(bookToSave);
    }

    public Book update(Long id, BookDTO bookDTO) {
        Book book = bookRepository.findById(id).orElseThrow(() -> new RuntimeException("Book not found with id " + id));

        Optional.ofNullable(bookDTO.title()).ifPresent(book::setTitle);
        Optional.ofNullable(bookDTO.author()).ifPresent(book::setAuthor);
        if (bookDTO.yearPublished() != 0) {
            book.setYearPublished(bookDTO.yearPublished());
        }

        return bookRepository.save(book);
    }


    public void delete(Long id) { bookRepository.deleteById(id); }
}
