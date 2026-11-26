import re

from skill_extractor import SKILL_ALIASES


def extract_skill_evidence(resume_text):

    evidence = {}

    lines = resume_text.splitlines()

    for skill, aliases in SKILL_ALIASES.items():

        matched_lines = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            for alias in aliases:

                if alias == "c":
                    pattern = r"(?<!\w)c(?![\w+#])"
                else:
                    pattern = (
                        r"(?<!\w)" +
                        re.escape(alias) +
                        r"(?!\w)"
                    )

                if re.search(pattern, line, re.IGNORECASE):

                    if line not in matched_lines:
                        matched_lines.append(line)

                    break

        if matched_lines:
            evidence[skill] = matched_lines[:3]

    return evidence