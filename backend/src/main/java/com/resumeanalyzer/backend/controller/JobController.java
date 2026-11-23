
package com.resumeanalyzer.backend.controller;

import com.resumeanalyzer.backend.model.Job;
import com.resumeanalyzer.backend.service.JobService;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/jobs")
public class JobController {

    private final JobService jobService;

    // Constructor injection
    public JobController(JobService jobService) {
        this.jobService = jobService;
    }

    // Temporary in-memory storage for GET endpoints
    private final Map<Integer, Job> jobs = new HashMap<>();

    {
        jobs.put(10, new Job(
                "Java Developer",
                "Google",
                "Bangalore",
                List.of("Java", "Spring Boot", "SQL"),
                2
        ));
    }

    // GET /jobs/10
    @GetMapping("/{id}")
    public ResponseEntity<Job> getJob(@PathVariable int id) {

        Job job = jobs.get(id);

        if (job == null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(job);
    }

    // GET /jobs/search?location=Bangalore
    @GetMapping("/search")
    public List<Job> searchJobs(@RequestParam String location) {

        List<Job> result = new ArrayList<>();

        for (Job job : jobs.values()) {
            if (job.getLocation().equalsIgnoreCase(location)) {
                result.add(job);
            }
        }

        return result;
    }

    // POST /jobs
    @PostMapping
    public ResponseEntity<Job> createJob(@RequestBody Job job) {

        Job savedJob = jobService.createJob(job);

        return new ResponseEntity<>(savedJob, HttpStatus.CREATED);
    }
}
