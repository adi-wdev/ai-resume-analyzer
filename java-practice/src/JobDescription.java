import java.util.ArrayList;

public class JobDescription {

    private String jobTitle;

    private ArrayList<String> requiredSkills = new ArrayList<>();

    public JobDescription(String jobTitle) {
        this.jobTitle = jobTitle;
    }

    public void addRequiredSkill(String skill) {
        requiredSkills.add(skill);
    }

    public ArrayList<String> getRequiredSkills() {
        return requiredSkills;
    }

    public String getJobTitle() {
        return jobTitle;
    }
}