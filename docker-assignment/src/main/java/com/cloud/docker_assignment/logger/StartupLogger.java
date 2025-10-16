package com.cloud.docker_assignment.logger;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

@Component
public class StartupLogger {
    @Value("${server.port:8080}")
    private int port;

    @EventListener(ApplicationReadyEvent.class)
    public void logStartup() {
        System.out.printf("Application started successfully! Internal port: %d.%n", port);
        System.out.println("For a proper welcome, send a GET request to /api/hello.");
    }
}
