import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("user provided input values:")

else:
    script_name = sys.argv[0]
    name = "raj"
    rollno = "123"
    print(" no input given  default values:")
    print("Student Name:", script_name)
    print("Student Roll No:", rollno)
    
    
