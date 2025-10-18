package com.cloud.docker_compose_assignment.logger;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

@Component
public class StartupLogger {
    @Value("${server.port:8080}")
    private int port;

    @Value("${springdoc.swagger-ui.path:/swagger-ui.html}")
    private String swaggerPath;

    @Value("${server.servlet.context-path:/library}")
    private String contextPath;

    @EventListener(ApplicationReadyEvent.class)
    public void logStartup() {
        System.out.printf("Application started successfully! Internal port: %d.%n", port);
        System.out.printf("Navigate to localhost:8080%s%s to access the application endpoints.%n", contextPath, swaggerPath);
    }
}
