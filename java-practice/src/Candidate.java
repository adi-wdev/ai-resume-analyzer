
import java.util.ArrayList;

public class Candidate {
    private String name;
    private String email;

    private ArrayList<String> skills = new ArrayList<>();

    public Candidate(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public void addSkill(String skill) {
        skills.add(skill);
    }

    public ArrayList<String> getSkills() {
        return skills;
    }

    public String getName() {
        return name;
    }

    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Skills: " + skills);
    }
}
