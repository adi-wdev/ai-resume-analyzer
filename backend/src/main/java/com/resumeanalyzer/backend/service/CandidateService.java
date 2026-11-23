package com.resumeanalyzer.backend.service;

import com.resumeanalyzer.backend.exception.ResourceNotFoundException;
import com.resumeanalyzer.backend.model.Candidate;
import com.resumeanalyzer.backend.repository.CandidateRepository;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CandidateService {

    private final CandidateRepository candidateRepository;

    public CandidateService(CandidateRepository candidateRepository) {
        this.candidateRepository = candidateRepository;
    }

    public Candidate saveCandidate(Candidate candidate) {
        return candidateRepository.save(candidate);
    }

    public List<Candidate> getAllCandidates() {
        return candidateRepository.findAll();
    }

    public Candidate getCandidateById(Long id) {
        return candidateRepository.findById(id).orElseThrow(() ->
                new ResourceNotFoundException(
                        "Candidate not found with ID: " + id
                )
        );
    }

    public String checkCandidateExperience(int experience) {

        if (experience >= 2) {
            return "Experienced Candidate";
        }

        return "Fresher Candidate";
    }
}