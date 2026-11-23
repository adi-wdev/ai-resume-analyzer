package com.resumeanalyzer.backend.controller;

import com.resumeanalyzer.backend.model.Candidate;
import com.resumeanalyzer.backend.service.CandidateService;

import org.springframework.web.bind.annotation.*;

@RestController
public class CandidateController {

    private final CandidateService candidateService;

    public CandidateController(CandidateService candidateService) {
        this.candidateService = candidateService;
    }

    @GetMapping("/candidate")
    public Candidate getCandidate() {

        return candidateService.getCandidate();
    }

    @GetMapping("/experience")
    public String checkExperience(@RequestParam int years) {
        return candidateService.checkCandidateExperience(years);
    }
}