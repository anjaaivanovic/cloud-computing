package com.cloud.docker_compose_assignment.dto;

public record BookDTO(
        String title,
        String author,
        int yearPublished
) {
}
