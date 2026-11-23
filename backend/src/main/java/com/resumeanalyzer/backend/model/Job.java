
package com.resumeanalyzer.backend.model;

import java.util.List;

public class Job {

    private String jobTitle;
    private String company;
    private String location;
    private List<String> requiredSkills;
    private int minimumExperience;

    public Job() {
    }

    public Job(String jobTitle, String company, String location,
               List<String> requiredSkills, int minimumExperience) {
        this.jobTitle = jobTitle;
        this.company = company;
        this.location = location;
        this.requiredSkills = requiredSkills;
        this.minimumExperience = minimumExperience;
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

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<String> getRequiredSkills() {
        return requiredSkills;
    }

    public void setRequiredSkills(List<String> requiredSkills) {
        this.requiredSkills = requiredSkills;
    }

    public int getMinimumExperience() {
        return minimumExperience;
    }

    public void setMinimumExperience(int minimumExperience) {
        this.minimumExperience = minimumExperience;
    }
}
