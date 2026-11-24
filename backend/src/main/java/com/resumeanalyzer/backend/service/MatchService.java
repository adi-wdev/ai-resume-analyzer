
package com.resumeanalyzer.backend.service;

import com.resumeanalyzer.backend.dto.MatchResult;
import com.resumeanalyzer.backend.exception.ResourceNotFoundException;
import com.resumeanalyzer.backend.model.Candidate;
import com.resumeanalyzer.backend.model.Job;
import com.resumeanalyzer.backend.repository.CandidateRepository;
import com.resumeanalyzer.backend.repository.JobRepository;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Service
public class MatchService {

    private final CandidateRepository candidateRepository;
    private final JobRepository jobRepository;

    public MatchService(
            CandidateRepository candidateRepository,
            JobRepository jobRepository
    ) {
        this.candidateRepository = candidateRepository;
        this.jobRepository = jobRepository;
    }

    public MatchResult calculateMatch(Long candidateId, Long jobId) {

        // Step 1: Fetch candidate
        Candidate candidate = candidateRepository.findById(candidateId)
                .orElseThrow(() ->
                        new ResourceNotFoundException(
                                "Candidate not found with ID: " + candidateId
                        )
                );

        // Step 2: Fetch job
        Job job = jobRepository.findById(jobId)
                .orElseThrow(() ->
                        new ResourceNotFoundException(
                                "Job not found with ID: " + jobId
                        )
                );

        // Step 3: Get candidate and job skills
        List<String> candidateSkills = candidate.getSkills();
        List<String> requiredSkills = job.getRequiredSkills();

        // Step 4: Prepare collections
        Set<String> normalizedCandidateSkills = new HashSet<>();

        if (candidateSkills != null) {
            for (String skill : candidateSkills) {
                if (skill != null) {
                    normalizedCandidateSkills.add(
                            skill.trim().toLowerCase()
                    );
                }
            }
        }

        List<String> matchedSkills = new ArrayList<>();
        List<String> missingSkills = new ArrayList<>();

        // Step 5: Compare skills
        if (requiredSkills != null) {
            for (String skill : requiredSkills) {

                if (skill == null || skill.isBlank()) {
                    continue;
                }

                if (normalizedCandidateSkills.contains(
                        skill.trim().toLowerCase()
                )) {
                    matchedSkills.add(skill);
                } else {
                    missingSkills.add(skill);
                }
            }
        }

        // Step 6: Calculate matching percentage
        double matchScore = 0.0;

        if (requiredSkills != null && !requiredSkills.isEmpty()) {

            int totalRequiredSkills = matchedSkills.size()
                    + missingSkills.size();

            if (totalRequiredSkills > 0) {
                matchScore = (double) matchedSkills.size()
                        / totalRequiredSkills * 100;
            }
        }

        // Step 7: Check experience eligibility
        boolean experienceEligible =
                candidate.getExperience() >= job.getMinimumExperience();

        // Step 8: Determine match category
        String matchCategory;

        if (matchScore >= 80) {
            matchCategory = "Excellent Match";
        } else if (matchScore >= 60) {
            matchCategory = "Good Match";
        } else if (matchScore >= 40) {
            matchCategory = "Average Match";
        } else {
            matchCategory = "Low Match";
        }

        // Step 9: Generate recommendation
        String recommendation;

        if (missingSkills.isEmpty()) {
            recommendation = "You have all the required skills.";
        } else {
            recommendation = "Consider learning: "
                    + String.join(", ", missingSkills);
        }

        // Step 10: Create and return result
        MatchResult result = new MatchResult(
                candidate.getName(),
                job.getJobTitle(),
                job.getCompany(),
                matchScore,
                matchedSkills,
                missingSkills,
                experienceEligible
        );

        result.setMatchCategory(matchCategory);
        result.setRecommendation(recommendation);

        return result;
    }
}
 