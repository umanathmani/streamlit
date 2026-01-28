import streamlit as st

st.title("🎓 Student Management System")

# Initialize student list
if "students" not in st.session_state:
    st.session_state.students = []

# ---- Add Student ----
st.subheader("Add Student")

roll_no = st.text_input("Roll Number")
name = st.text_input("Student Name")
department = st.text_input("Department")
marks = st.number_input("Marks", min_value=0, max_value=100)

if st.button("Add Student"):
    if roll_no and name and department:
        st.session_state.students.append({
            "roll": roll_no,
            "name": name,
            "dept": department,
            "marks": marks
        })
        st.success("Student added successfully")
    else:
        st.error("Please fill all details")

# ---- View Students ----
st.subheader("Student Records")

if st.session_state.students:
    for i, s in enumerate(st.session_state.students):
        st.write(
            f"{i+1}. Roll: {s['roll']} | "
            f"Name: {s['name']} | "
            f"Dept: {s['dept']} | "
            f"Marks: {s['marks']}"
        )
else:
    st.info("No student records found")

# ---- Delete Student ----
st.subheader("Delete Student")

delete_roll = st.text_input("Enter Roll Number to Delete")

if st.button("Delete"):
    for s in st.session_state.students:
        if s["roll"] == delete_roll:
            st.session_state.students.remove(s)
            st.success("Student record deleted")
            break
    else:
        st.error("Student not found")