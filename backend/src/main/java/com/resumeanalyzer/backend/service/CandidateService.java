package com.resumeanalyzer.backend.service;

import com.resumeanalyzer.backend.model.Candidate;
import org.springframework.stereotype.Service;

@Service
public class CandidateService {

    public Candidate getCandidate() {

        Candidate candidate = new Candidate();

        candidate.setName("Aditya");
        candidate.setEmail("aditya@gmail.com");

        return candidate;
    }

    public String checkCandidateExperience(int experience) {
        if (experience >= 2) {
            return "Experienced Candidate";
        }
        else {
            return "Fresher Candidate";
        }
    }
}