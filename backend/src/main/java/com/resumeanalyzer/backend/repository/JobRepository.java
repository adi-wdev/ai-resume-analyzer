package com.resumeanalyzer.backend.repository;

import com.resumeanalyzer.backend.model.Job;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface JobRepository extends JpaRepository<Job, Long> {

    List<Job> findByLocationIgnoreCase(String location);

    List<Job> findByCompanyIgnoreCase(String company);
}