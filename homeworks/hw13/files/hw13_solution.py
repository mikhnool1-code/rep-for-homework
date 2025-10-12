class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students_data = []

    def create_students_file(self, text):
        with open(self.filename, "w") as file:
            file.write(text)

    def read_students_file(self):
        self.students_data = []
        groups = {}

        with open(self.filename, "r") as file:
            for line in file:
                try:
                    name, group, grade = line.strip().split(",")
                    name = name.strip()
                    group = group.strip()
                    grade = int(grade.strip())
                    self.students_data.append((name, group, grade))

                    if group not in groups:
                        groups[group] = {"count": 0, "total_grade": 0}
                    groups[group]["count"] += 1
                    groups[group]["total_grade"] += grade
                except ValueError:
                    continue

        return self.students_data, groups

    def get_summary(self):
        groups = {}

        for name, group, grade in self.students_data:
            if group not in groups:
                groups[group] = {"count": 0, "total_grade": 0}
            groups[group]["count"] += 1
            groups[group]["total_grade"] += grade

        summary = {}
        for group, data in groups.items():
            count = data["count"]
            total_grade = data["total_grade"]
            avg_grade = round(total_grade / count, 2) if count > 0 else 0
            summary[group] = {"count": count, "avg_grade": avg_grade}

        return summary

    def write_summary_to_file(self):
        summary = self.get_summary() if self.students_data else {}

        if not summary:
            summary_lines = "\nTotal students: 0\n"
        else:
            total_students = sum(data["count"] for data in summary.values())
            summary_lines = "\nSummary\n"
            for group, data in summary.items():
                count = data["count"]
                avg_grade = data["avg_grade"]
                summary_lines += (
                    f"Group: {group}, Number of students: {count}, Average grade: {avg_grade}\n"
                )
            summary_lines += f"Total students: {total_students}\n"

        with open(self.filename, "a") as file:
            file.write(summary_lines)
