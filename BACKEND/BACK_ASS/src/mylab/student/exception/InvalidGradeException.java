package mylab.student.exception;

import java.lang.Exception;
public class InvalidGradeException extends Exception {
	public InvalidGradeException(String errMessage) {
		super(errMessage);
	}
}
