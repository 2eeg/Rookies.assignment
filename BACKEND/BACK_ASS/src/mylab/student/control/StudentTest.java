package mylab.student.control;

import mylab.student.entity.Student;
import mylab.student.exception.InvalidGradeException;

public class StudentTest {
	public static void main(String[] args) {
		try {
			Student student = new Student("��μ�","��ǻ�Ͱ���",3);
			student.setGrade(5);
		}
		catch(InvalidGradeException e) {
			System.out.println("�г��� 1~4 ���̿��� �մϴ�.");
		}
		
	}
	
}
