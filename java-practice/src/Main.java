
public class Main {

    public static void main(String[] args) {

        Candidate candidate =
                new Candidate("Aditya", "aditya@gmail.com");

        candidate.addSkill("Java");
        candidate.addSkill("Python");
        candidate.addSkill("SQL");

        JobDescription job =
                new JobDescription("Java Developer");

        job.addRequiredSkill("Java");
        job.addRequiredSkill("Spring Boot");
        job.addRequiredSkill("SQL");
        job.addRequiredSkill("React");

        ResumeMatcher matcher = new ResumeMatcher();

        matcher.matchResume(candidate, job);
    }
}
