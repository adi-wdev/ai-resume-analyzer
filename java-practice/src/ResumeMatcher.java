
import java.util.ArrayList;

public class ResumeMatcher {

    public void matchResume(Candidate candidate, JobDescription job) {

        ArrayList<String> matched = new ArrayList<>();
        ArrayList<String> missing = new ArrayList<>();

        for (String skill : job.getRequiredSkills()) {

            if (candidate.getSkills().contains(skill)) {
                matched.add(skill);
            } else {
                missing.add(skill);
            }
        }

        double percentage =
                (double) matched.size() / job.getRequiredSkills().size() * 100;

        System.out.println("\nJob: " + job.getJobTitle());

        System.out.println("\nMatched Skills:");
        for (String skill : matched) {
            System.out.println(skill);
        }

        System.out.println("\nMissing Skills:");
        for (String skill : missing) {
            System.out.println(skill);
        }

        System.out.println("\nMatch Percentage: " + percentage + "%");
    }
}
