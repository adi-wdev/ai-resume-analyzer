
package com.resumeanalyzer.backend.service;

import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
public class SkillNormalizer {

    private final Map<String, String> skillAliases = new HashMap<>();

    public SkillNormalizer() {

        // JavaScript
        addAliases("JavaScript", "JS", "Javascript");

        // Machine Learning
        addAliases("Machine Learning", "ML");

        // Artificial Intelligence
        addAliases("Artificial Intelligence", "AI");

        // React
        addAliases("React", "ReactJS", "React.js");

        // PostgreSQL
        addAliases("PostgreSQL", "Postgres");

        // Spring Boot
        addAliases("Spring Boot", "SpringBoot");

        // Node.js
        addAliases("Node.js", "NodeJS");

        // Additional aliases
        addAliases("TypeScript", "TS");
        addAliases("Python", "Py");
        addAliases("C#", "C Sharp");
        addAliases("Kubernetes", "K8s");
        addAliases("MongoDB", "Mongo");
    }

    private void addAliases(String standardName, String... aliases) {

        skillAliases.put(standardName.toLowerCase(), standardName);

        for (String alias : aliases) {
            skillAliases.put(alias.toLowerCase(), standardName);
        }
    }

    public String normalize(String skill) {

        if (skill == null || skill.isBlank()) {
            return "";
        }

        String cleanedSkill = skill.trim().toLowerCase();

        return skillAliases.getOrDefault(
                cleanedSkill,
                cleanedSkill
        );
    }
}
