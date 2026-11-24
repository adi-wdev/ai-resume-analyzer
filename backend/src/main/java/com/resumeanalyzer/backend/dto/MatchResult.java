
package com.resumeanalyzer.backend.dto;

import java.util.List;

public class MatchResult {

    private String candidateName;
    private String jobTitle;
    private String company;

    private double matchScore;
    private String matchCategory;
    private String recommendation;

    private List<String> matchedSkills;
    private List<String> missingSkills;

    private double weightedMatchScore;

    private List<String> matchedPreferredSkills;
    private List<String> missingPreferredSkills;

    private boolean experienceEligible;

    public MatchResult() {
    }

    public MatchResult(
            String candidateName,
            String jobTitle,
            String company,
            double matchScore,
            List<String> matchedSkills,
            List<String> missingSkills,
            boolean experienceEligible
    ) {
        this.candidateName = candidateName;
        this.jobTitle = jobTitle;
        this.company = company;
        this.matchScore = matchScore;
        this.matchedSkills = matchedSkills;
        this.missingSkills = missingSkills;
        this.experienceEligible = experienceEligible;
    }

    public String getCandidateName() {
        return candidateName;
    }

    public void setCandidateName(String candidateName) {
        this.candidateName = candidateName;
    }

    public String getJobTitle() {
        return jobTitle;
    }

    public void setJobTitle(String jobTitle) {
        this.jobTitle = jobTitle;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public double getMatchScore() {
        return matchScore;
    }

    public void setMatchScore(double matchScore) {
        this.matchScore = matchScore;
    }

    public String getMatchCategory() {
        return matchCategory;
    }

    public void setMatchCategory(String matchCategory) {
        this.matchCategory = matchCategory;
    }

    public String getRecommendation() {
        return recommendation;
    }

    public void setRecommendation(String recommendation) {
        this.recommendation = recommendation;
    }

    public List<String> getMatchedSkills() {
        return matchedSkills;
    }

    public void setMatchedSkills(List<String> matchedSkills) {
        this.matchedSkills = matchedSkills;
    }

    public List<String> getMissingSkills() {
        return missingSkills;
    }

    public void setMissingSkills(List<String> missingSkills) {
        this.missingSkills = missingSkills;
    }

    public List<String> getMatchedPreferredSkills() {
        return matchedPreferredSkills;
    }

    public void setMatchedPreferredSkills(List<String> matchedPreferredSkills) {
        this.matchedPreferredSkills = matchedPreferredSkills;
    }

    public List<String> getMissingPreferredSkills() {
        return missingPreferredSkills;
    }

    public void setMissingPreferredSkills(List<String> missingPreferredSkills) {
        this.missingPreferredSkills = missingPreferredSkills;
    }

    public double getWeightedMatchScore() {
        return weightedMatchScore;
    }

    public void setWeightedMatchScore(double weightedMatchScore) {
        this.weightedMatchScore = weightedMatchScore;
    }

    public boolean isExperienceEligible() {
        return experienceEligible;
    }

    public void setExperienceEligible(boolean experienceEligible) {
        this.experienceEligible = experienceEligible;
    }
}
