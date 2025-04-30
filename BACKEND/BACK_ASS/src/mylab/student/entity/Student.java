package mylab.student.entity;
import java.io.IOException;
import mylab.student.exception.InvalidGradeException;

public class Student {
	private String studentId;
	private String name;
	private String major;
	private int grade;
	public Student() {
		
	}
	
	public Student(String name, String major, int grade) throws InvalidGradeException {
		setName(name);
		setMajor(major);
		setGrade(grade);
	}

	public void setStudentId(String studentId) {
		this.studentId = studentId;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setMajor(String major) {
		this.major = major;
	}

	public int getGrade() {
		return grade;
	}
	public void setGrade(int grade) throws InvalidGradeException {
		if (grade < 1 || grade > 4) {
			throw new InvalidGradeException("Àß¸øµÈ grade:" + grade);
		}
		this.grade = grade;
	}
	public String getStudentId() {
		return studentId;
	}
	public String getName() {
		return name;
	}
	public String getMajor() {
		return major;
	}
	
}
