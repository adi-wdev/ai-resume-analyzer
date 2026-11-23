package com.resumeanalyzer.backend.service;

import com.resumeanalyzer.backend.model.Job;
import com.resumeanalyzer.backend.repository.JobRepository;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class JobService {

    private final JobRepository jobRepository;

    public JobService(JobRepository jobRepository) {
        this.jobRepository = jobRepository;
    }

    // Create job
    public Job saveJob(Job job) {

        if (job.getJobTitle() == null ||
                job.getJobTitle().isBlank()) {

            throw new IllegalArgumentException(
                    "Job title cannot be empty"
            );
        }

        if (job.getCompany() == null ||
                job.getCompany().isBlank()) {

            throw new IllegalArgumentException(
                    "Company cannot be empty"
            );
        }

        return jobRepository.save(job);
    }

    // Get all jobs
    public List<Job> getAllJobs() {
        return jobRepository.findAll();
    }

    // Get job by ID
    public Job getJobById(Long id) {
        return jobRepository.findById(id).orElse(null);
    }

    // Search jobs by location
    public List<Job> getJobsByLocation(String location) {
        return jobRepository.findByLocationIgnoreCase(location);
    }

    // Update job
    public Job updateJob(Long id, Job updatedJob) {

        Job existingJob = getJobById(id);

        if (existingJob == null) {
            return null;
        }

        existingJob.setJobTitle(updatedJob.getJobTitle());
        existingJob.setCompany(updatedJob.getCompany());
        existingJob.setLocation(updatedJob.getLocation());
        existingJob.setRequiredSkills(
                updatedJob.getRequiredSkills()
        );
        existingJob.setMinimumExperience(
                updatedJob.getMinimumExperience()
        );

        return jobRepository.save(existingJob);
    }

    // Delete job
    public boolean deleteJob(Long id) {

        if (!jobRepository.existsById(id)) {
            return false;
        }

        jobRepository.deleteById(id);
        return true;
    }

    public long getJobCount() {
        return jobRepository.count();
    }

    public List<Job> getJobsByCompany(String company) {
        return jobRepository.findByCompanyIgnoreCase(company);
    }
}