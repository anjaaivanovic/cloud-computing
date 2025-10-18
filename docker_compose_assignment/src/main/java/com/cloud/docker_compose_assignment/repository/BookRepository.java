package com.cloud.docker_compose_assignment.repository;

import com.cloud.docker_compose_assignment.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BookRepository extends JpaRepository<Book, Long> {
}
