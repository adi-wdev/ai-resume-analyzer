
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
    private final SkillNormalizer skillNormalizer;

    public MatchService(
            CandidateRepository candidateRepository,
            JobRepository jobRepository,
            SkillNormalizer skillNormalizer
    ) {
        this.candidateRepository = candidateRepository;
        this.jobRepository = jobRepository;
        this.skillNormalizer = skillNormalizer;
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

        // Step 3: Get skills safely
        List<String> candidateSkills = candidate.getSkills();
        List<String> requiredSkills = job.getRequiredSkills();
        List<String> preferredSkills = job.getPreferredSkills();

        // Step 4: Normalize candidate skills
        Set<String> normalizedCandidateSkills = new HashSet<>();

        if (candidateSkills != null) {
            for (String skill : candidateSkills) {
                String normalized = skillNormalizer.normalize(skill);

                if (!normalized.isEmpty()) {
                    normalizedCandidateSkills.add(normalized);
                }
            }
        }

        List<String> matchedSkills = new ArrayList<>();
        List<String> missingSkills = new ArrayList<>();

        List<String> matchedPreferredSkills = new ArrayList<>();
        List<String> missingPreferredSkills = new ArrayList<>();

        // Step 5: Compare required skills
        if (requiredSkills != null) {
            for (String skill : requiredSkills) {

                String normalized = skillNormalizer.normalize(skill);

                if (normalized.isEmpty()) {
                    continue;
                }

                if (normalizedCandidateSkills.contains(normalized)) {
                    matchedSkills.add(skill);
                } else {
                    missingSkills.add(skill);
                }
            }
        }

        // Step 6: Compare preferred skills
        if (preferredSkills != null) {
            for (String skill : preferredSkills) {

                String normalized = skillNormalizer.normalize(skill);

                if (normalized.isEmpty()) {
                    continue;
                }

                if (normalizedCandidateSkills.contains(normalized)) {
                    matchedPreferredSkills.add(skill);
                } else {
                    missingPreferredSkills.add(skill);
                }
            }
        }

        // Step 7: Calculate weighted score
        int matchedWeight = matchedSkills.size() * 2
                + matchedPreferredSkills.size();

        int totalWeight = (matchedSkills.size() + missingSkills.size()) * 2
                + matchedPreferredSkills.size()
                + missingPreferredSkills.size();

        double weightedMatchScore = 0.0;

        if (totalWeight > 0) {
            weightedMatchScore =
                    (double) matchedWeight / totalWeight * 100;
        }

        // Step 8: Calculate normal required-skill score
        int totalRequired = matchedSkills.size() + missingSkills.size();

        double matchScore = 0.0;

        if (totalRequired > 0) {
            matchScore =
                    (double) matchedSkills.size() / totalRequired * 100;
        }

        // Step 9: Determine category using weighted score
        String matchCategory;

        if (weightedMatchScore >= 80) {
            matchCategory = "Excellent Match";
        } else if (weightedMatchScore >= 60) {
            matchCategory = "Good Match";
        } else if (weightedMatchScore >= 40) {
            matchCategory = "Average Match";
        } else {
            matchCategory = "Low Match";
        }

        // Step 10: Generate recommendation
        List<String> allMissingSkills = new ArrayList<>();
        allMissingSkills.addAll(missingSkills);
        allMissingSkills.addAll(missingPreferredSkills);

        String recommendation;

        if (allMissingSkills.isEmpty()) {
            recommendation = "You have all the required skills.";
        } else {
            recommendation = "Consider learning: "
                    + String.join(", ", allMissingSkills);
        }

        // Step 11: Check experience
        boolean experienceEligible =
                job.getMinimumExperience() == null
                        || candidate.getExperience() >= job.getMinimumExperience();

        // Step 12: Create result
        MatchResult result = new MatchResult(
                candidate.getName(),
                job.getJobTitle(),
                job.getCompany(),
                matchScore,
                matchedSkills,
                missingSkills,
                experienceEligible
        );

        result.setMatchedPreferredSkills(matchedPreferredSkills);
        result.setMissingPreferredSkills(missingPreferredSkills);
        result.setWeightedMatchScore(weightedMatchScore);
        result.setMatchCategory(matchCategory);
        result.setRecommendation(recommendation);

        return result;
    }
}
