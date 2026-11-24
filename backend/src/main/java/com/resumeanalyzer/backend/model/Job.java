
package com.resumeanalyzer.backend.model;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;

@Entity
@Table(name = "jobs")
public class Job {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "Job title is required")
    @Column(nullable = false)
    private String jobTitle;

    @NotBlank(message = "Company name is required")
    @Column(nullable = false)
    private String company;

    @NotBlank(message = "Location is required")
    private String location;

    @ElementCollection
    @CollectionTable(
            name = "job_required_skills",
            joinColumns = @JoinColumn(name = "job_id")
    )
    @Column(name = "skill")
    private List<String> requiredSkills = new ArrayList<>();

    // NEW: Preferred skills
    @ElementCollection
    @CollectionTable(
            name = "job_preferred_skills",
            joinColumns = @JoinColumn(name = "job_id")
    )
    @Column(name = "skill")
    private List<String> preferredSkills = new ArrayList<>();

    @Min(value = 0, message = "Minimum experience cannot be negative")
    private Integer minimumExperience;

    public Job() {
    }

    public Job(String jobTitle, String company,
               String location, List<String> requiredSkills,
               Integer minimumExperience) {

        this.jobTitle = jobTitle;
        this.company = company;
        this.location = location;
        this.requiredSkills = requiredSkills;
        this.minimumExperience = minimumExperience;
    }

    public Long getId() {
        return id;
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

    // NEW: Preferred skills getter and setter
    public List<String> getPreferredSkills() {
        return preferredSkills;
    }

    public void setPreferredSkills(List<String> preferredSkills) {
        this.preferredSkills = preferredSkills;
    }



    public Integer getMinimumExperience() {
        return minimumExperience;
    }

    public void setMinimumExperience(Integer minimumExperience) {
        this.minimumExperience = minimumExperience;
    }
}
