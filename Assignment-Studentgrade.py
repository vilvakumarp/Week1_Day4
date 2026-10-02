import streamlit as st


# Same grading logic from Day 2
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Page title
st.title("Student Grade Manager")

# Session state keeps students across Streamlit reruns
if "students" not in st.session_state:
    st.session_state.students = []


# Form to add a student
with st.form("add_student"):
    name = st.text_input("Name")
    mark = st.number_input(
        "Mark",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

    submitted = st.form_submit_button("Add")

    if submitted:
        if not name.strip():
            st.error("Please enter a student name.")
        else:
            st.session_state.students.append({
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            })
            st.success(f"{name.strip()} added successfully.")


# Display students and class statistics
if st.session_state.students:
    st.subheader("Students")

    st.table(st.session_state.students)

    marks = [student["Mark"] for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average", f"{average:.1f}")

    with col2:
        st.metric("Highest", f"{highest:g}")

    with col3:
        st.metric("Lowest", f"{lowest:g}")

else:
    st.info("No students added yet.")
