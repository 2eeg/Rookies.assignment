package mylab.student.control;

import mylab.student.entity.Student;
import mylab.student.exception.InvalidGradeException;

public class StudentTest {
	public static void main(String[] args) {
		try {
			Student student = new Student("김민수","컴퓨터공학",3);
			student.setGrade(5);
		}
		catch(InvalidGradeException e) {
			System.out.println("학년은 1~4 사이여야 합니다.");
		}
		
	}
	
}
