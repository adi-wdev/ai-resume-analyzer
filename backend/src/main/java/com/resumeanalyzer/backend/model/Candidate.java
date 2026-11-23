package com.resumeanalyzer.backend.model;

import java.util.List;

public class Candidate {

    private String name;
    private String email;
    private List<String> skills;
    private int experience;

    public Candidate() {
    }

    public Candidate(String name, String email,
                     List<String> skills, int experience) {

        this.name = name;
        this.email = email;
        this.skills = skills;
        this.experience = experience;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<String> getSkills() {
        return skills;
    }

    public void setSkills(List<String> skills) {
        this.skills = skills;
    }

    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }
}