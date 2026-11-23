package com.resumeanalyzer.backend.controller;

import com.resumeanalyzer.backend.model.Job;
import com.resumeanalyzer.backend.service.JobService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/jobs")
public class JobController {

    private final JobService jobService;

    public JobController(JobService jobService) {
        this.jobService = jobService;
    }

    // Create job
    @PostMapping
    public ResponseEntity<Job> createJob(
            @Valid @RequestBody Job job) {

        Job savedJob = jobService.saveJob(job);

        return new ResponseEntity<>(
                savedJob,
                HttpStatus.CREATED
        );
    }

    // Get all jobs
    @GetMapping
    public ResponseEntity<List<Job>> getAllJobs() {

        return ResponseEntity.ok(
                jobService.getAllJobs()
        );
    }

    // Get job by ID
    @GetMapping("/{id}")
    public ResponseEntity<Job> getJobById(
            @PathVariable Long id) {

        Job job = jobService.getJobById(id);

        if (job == null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(job);
    }

    // Search by location
    @GetMapping("/search")
    public ResponseEntity<List<Job>> searchJobs(
            @RequestParam String location) {

        return ResponseEntity.ok(
                jobService.getJobsByLocation(location)
        );
    }

    // Update job
    @PutMapping("/{id}")
    public ResponseEntity<Job> updateJob(
            @PathVariable Long id,
            @Valid @RequestBody Job job) {

        Job updatedJob = jobService.updateJob(id, job);

        if (updatedJob == null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(updatedJob);
    }

    @GetMapping("/count")
    public ResponseEntity<Long> getJobCount() {

        return ResponseEntity.ok(
                jobService.getJobCount()
        );
    }

    @GetMapping("/company")
    public ResponseEntity<List<Job>> getJobsByCompany(
            @RequestParam String name) {

        return ResponseEntity.ok(
                jobService.getJobsByCompany(name)
        );
    }

    // Delete job
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteJob(
            @PathVariable Long id) {

        boolean deleted = jobService.deleteJob(id);

        if (!deleted) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.noContent().build();
    }
}