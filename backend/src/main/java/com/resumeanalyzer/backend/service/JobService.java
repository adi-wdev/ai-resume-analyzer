package com.resumeanalyzer.backend.service;

import com.resumeanalyzer.backend.model.Job;
import org.springframework.stereotype.Service;

@Service
public class JobService {

    public Job createJob(Job job) {

        if (job.getJobTitle() == null || job.getJobTitle().isBlank()) {
            throw new IllegalArgumentException("Job title cannot be empty");
        }

        if (job.getCompany() == null || job.getCompany().isBlank()) {
            throw new IllegalArgumentException("Company cannot be empty");
        }

        return job;
    }
}