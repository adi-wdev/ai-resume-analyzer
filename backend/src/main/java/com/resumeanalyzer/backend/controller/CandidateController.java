package com.resumeanalyzer.backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class CandidateController {

    @GetMapping("/candidate")
    public Map<String, Object> getCandidate() {

        return Map.of(
                "name", "Aditya",
                "email", "aditya@example.com",
                "skills", new String[]{"Java", "Python", "SQL"},
                "experience", 0
        );
    }
}