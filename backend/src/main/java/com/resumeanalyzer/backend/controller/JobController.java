package com.resumeanalyzer.backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class JobController{
    @GetMapping("/job")
    public Map<String, Object> getJob() {

        return Map.of(
                "jobTitle", "Java Developer",
                "company", "Google",
                "location", "Bangalore",
                "requiredSkills", new String[]{"Java", "Spring Boot", "SQL"}
        );
    }
}