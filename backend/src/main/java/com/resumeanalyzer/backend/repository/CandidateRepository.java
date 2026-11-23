package com.resumeanalyzer.backend.repository;

import com.resumeanalyzer.backend.model.Candidate;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CandidateRepository
        extends JpaRepository<Candidate, Long> {

}