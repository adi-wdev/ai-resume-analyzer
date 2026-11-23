
package com.resumeanalyzer.backend.controller;

import com.resumeanalyzer.backend.model.Candidate;
import com.resumeanalyzer.backend.service.CandidateService;
import com.resumeanalyzer.backend.repository.CandidateRepository;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import jakarta.validation.Valid;
import java.util.List;

@RestController
public class CandidateController {

    private final CandidateService candidateService;
    private final CandidateRepository candidateRepository;

    public CandidateController(
            CandidateService candidateService,
            CandidateRepository candidateRepository) {

        this.candidateService = candidateService;
        this.candidateRepository = candidateRepository;
    }

    @PostMapping("/candidates")
    public ResponseEntity<Candidate> createCandidate(
            @Valid @RequestBody Candidate candidate) {

        return ResponseEntity.ok(candidateService.saveCandidate(candidate));
    }

    @GetMapping("/candidates")
    public List<Candidate> getAllCandidates() {
        return candidateService.getAllCandidates();
    }

    @GetMapping("/candidates/{id}")
    public Candidate getCandidateById(@PathVariable Long id) {
        return candidateService.getCandidateById(id);
    }

    @GetMapping("/candidate/experience")
    public String checkExperience(@RequestParam int years) {
        return candidateService.checkCandidateExperience(years);
    }

    // GET /candidates/count
    @GetMapping("/candidates/count")
    public long countCandidates() {
        return candidateRepository.count();
    }
}
