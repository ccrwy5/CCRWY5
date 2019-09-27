import pytest
import login

def test_login():

	userName = login.getUserName()
	password = login.getPassword()
	assert userName != "" and  password != ""

def test_login_FAIL():
	userName = login.getUserNameFAIL()
	password = login.getPasswordFAIL()
	
	assert userName != '' and password != ''






# Test 2

def test_math():
	expectedResult = login.getExpectedResult()

	assert expectedResult == (9 * 2)

def test_math_FAIL():
	expectedResult = login.getExpectedResult()

	assert expectedResult == (9 * 3)





# Test 3

def test_find_student():
	fname = login.getStudentFirstName()
	lname = login.getStudentLastName()

	assert fname == 'Michael' and lname == 'Jones'

def test_find_student_FAIL():
	fname = login.getStudentFirstNameFAIL()
	lname = login.getStudentLastNameFAIL()
	
	assert fname != '' and lname != ''


# Test 4

def test_check_courseID():
	courseID = login.getCourseID()
	assert courseID == 'CS4230'

def test_check_courseIDFAIL():
	courseID = login.getCourseIDFAIL()
	assert courseID == 'CS4230'


# Test 5

def test_check_instructor_info():
	id = login.getInstructorID()

	assert id == "9999"

def test_check_instructor_info_FAIL():
	id = login.getInstructorIDFAIL()
	assert id != ""
