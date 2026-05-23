"""
Exam Grader Pro - Streamlit Web App
A professional tool for grading multiple-choice exams with intelligent answer parsing.

Author: Jorge B. Cevallos
"""

import streamlit as st
import re
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Exam Grader Pro",
    page_icon="✓",
    layout="centered"
)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def extract_letters(input_text):
    """Extract only letters from input text, removing numbers, punctuation, and whitespace."""
    if not input_text:
        return ""
    # Remove all non-letter characters and convert to uppercase
    return re.sub(r'[^A-Z]', '', input_text.upper())


def grade_exam(answer_key, student_answer, grading_scale):
    """
    Compare student answer against answer key and calculate grade.
    
    Returns:
        tuple: (grade, correct_count, incorrect_count, total_questions, percentage, comparison_data)
    """
    # Extract letters only
    key_letters = extract_letters(answer_key)
    student_letters = extract_letters(student_answer)
    
    if not key_letters or not student_letters:
        return None, None, None, None, None, None
    
    # Get the shorter length for comparison
    total_questions = min(len(key_letters), len(student_letters))
    
    # Compare answers
    correct_count = 0
    comparison_data = []
    
    for i in range(total_questions):
        is_correct = key_letters[i] == student_letters[i]
        if is_correct:
            correct_count += 1
        
        comparison_data.append({
            'question': i + 1,
            'key': key_letters[i],
            'student': student_letters[i],
            'correct': is_correct
        })
    
    # Calculate metrics
    incorrect_count = total_questions - correct_count
    percentage = (correct_count / total_questions * 100) if total_questions > 0 else 0
    grade = (correct_count / total_questions * grading_scale) if total_questions > 0 else 0
    
    return grade, correct_count, incorrect_count, total_questions, percentage, comparison_data


# ============================================================================
# STREAMLIT APP
# ============================================================================

def main():
    # Header
    st.title("✓ Exam Grader Pro")
    st.markdown("Generate accurate grades from multiple-choice exams with intelligent answer parsing")
    st.markdown("---")
    
    # Instructions
    with st.expander("📖 How to use this tool"):
        st.markdown("""
        1. **Select your grading scale** (10-point, 100-point, or custom)
        2. **Enter the answer key** as a string of letters (e.g., ADCABCBA...)
        3. **Paste the student's answer** in any format:
           - Plain letters: `ABCDABCD...`
           - Numbered: `1) A, 2) B, 3) C...`
           - Punctuated: `A, B, C, D...`
        4. **Click 'Calculate Grade'** to see results
        5. **Copy the grade** to paste into your LMS (Moodle, Canvas, etc.)
        
        **The app automatically extracts only the letters, so students can format their answers however they want!**
        """)
    
    # Configuration Section
    st.subheader("Configuration")
    
    # Grading scale selector
    col1, col2 = st.columns([3, 2])
    
    with col1:
        scale_option = st.selectbox(
            "⚙️ Grading Scale",
            ["10-point scale", "100-point scale", "20-point scale", "5-point scale", "Custom"],
            help="Select the grading scale for your institution"
        )
    
    with col2:
        if scale_option == "Custom":
            custom_scale = st.number_input(
                "Custom Scale",
                min_value=1,
                max_value=1000,
                value=10,
                step=1,
                help="Enter your custom grading scale"
            )
            grading_scale = custom_scale
        else:
            # Extract number from option (e.g., "10-point scale" -> 10)
            grading_scale = int(scale_option.split('-')[0])
    
    st.markdown("---")
    
    # Step 1: Answer Key
    st.subheader("Step 1: Enter Answer Key")
    
    answer_key = st.text_area(
        "🔑 Answer Key",
        height=100,
        placeholder="e.g., ADCABCBADCBA...",
        help="Enter the correct answers as a string of letters"
    )
    
    st.markdown("---")
    
    # Step 2: Student Answer
    st.subheader("Step 2: Enter Student's Answer")
    
    student_answer = st.text_area(
        "📝 Student's Answer",
        height=200,
        placeholder="""Paste student's answer in any format...

Examples:
• ABCDABCD...
• 1) A, 2) B, 3) C...
• A, B, C, D...""",
        help="Paste the student's answer string in any format"
    )
    
    # Buttons
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        calculate_button = st.button("🚀 Calculate Grade", type="primary", use_container_width=True)
    
    with col2:
        if st.button("Clear All", use_container_width=True):
            st.rerun()
    
    # Process grading
    if calculate_button:
        if not answer_key or not student_answer:
            st.error("❌ Please enter both answer key and student answer.")
        else:
            # Extract letters for validation
            key_letters = extract_letters(answer_key)
            student_letters = extract_letters(student_answer)
            
            if not key_letters:
                st.error("❌ Could not extract valid letters from answer key. Please check your input.")
            elif not student_letters:
                st.error("❌ Could not extract valid letters from student answer. Please check your input.")
            else:
                # Check for length mismatch
                if len(key_letters) != len(student_letters):
                    st.warning(f"⚠️ Length Mismatch\n\nAnswer Key: {len(key_letters)} questions\n\nStudent Answer: {len(student_letters)} questions\n\nGrading will proceed based on the shorter length.")
                
                # Calculate grade
                grade, correct, incorrect, total, percentage, comparison = grade_exam(
                    answer_key, student_answer, grading_scale
                )
                
                if grade is not None:
                    st.success("✅ Grading complete!")
                    
                    # Display final grade in a prominent card
                    st.markdown("---")
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #4299e1 0%, #667eea 100%); 
                                padding: 40px; 
                                border-radius: 8px; 
                                text-align: center; 
                                color: white;
                                margin-bottom: 24px;">
                        <div style="font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9; margin-bottom: 12px;">
                            FINAL GRADE
                        </div>
                        <div style="font-size: 56px; font-weight: 700; letter-spacing: -1px;">
                            {grade:.2f} / {grading_scale}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Statistics
                    col1, col2, col3, col4 = st.columns(4)
                    
                    col1.metric("Correct", correct)
                    col2.metric("Incorrect", incorrect)
                    col3.metric("Total", total)
                    col4.metric("Percentage", f"{percentage:.2f}%")
                    
                    # Detailed comparison
                    st.markdown("---")
                    st.subheader("Detailed Comparison")
                    
                    # Create comparison table
                    comparison_html = """
                    <style>
                        .comparison-table {
                            width: 100%;
                            border-collapse: collapse;
                            margin-top: 16px;
                            background: white;
                            border-radius: 6px;
                            overflow: hidden;
                        }
                        .comparison-table thead {
                            background: #f0f2f5;
                        }
                        .comparison-table th {
                            padding: 12px 16px;
                            text-align: center;
                            font-size: 13px;
                            font-weight: 600;
                            color: #6b6b76;
                            text-transform: uppercase;
                            letter-spacing: 0.5px;
                            border-bottom: 2px solid #e6e6ea;
                        }
                        .comparison-table td {
                            padding: 12px 16px;
                            text-align: center;
                            border-bottom: 1px solid #f0f2f5;
                            font-family: 'Courier New', monospace;
                            font-size: 14px;
                        }
                        .comparison-table tbody tr:hover {
                            background: #f9fafb;
                        }
                        .result-correct {
                            background: #c6f6d5;
                            color: #22543d;
                            font-weight: 700;
                            padding: 4px 12px;
                            border-radius: 4px;
                        }
                        .result-incorrect {
                            background: #fed7d7;
                            color: #742a2a;
                            font-weight: 700;
                            padding: 4px 12px;
                            border-radius: 4px;
                        }
                    </style>
                    <table class="comparison-table">
                        <thead>
                            <tr>
                                <th>Question</th>
                                <th>Answer Key</th>
                                <th>Student</th>
                                <th>Result</th>
                            </tr>
                        </thead>
                        <tbody>
                    """
                    
                    for item in comparison:
                        result_class = "result-correct" if item['correct'] else "result-incorrect"
                        result_symbol = "✓" if item['correct'] else "✗"
                        
                        comparison_html += f"""
                            <tr>
                                <td>{item['question']}</td>
                                <td><strong>{item['key']}</strong></td>
                                <td><strong>{item['student']}</strong></td>
                                <td><span class="{result_class}">{result_symbol}</span></td>
                            </tr>
                        """
                    
                    comparison_html += """
                        </tbody>
                    </table>
                    """
                    
                    st.markdown(comparison_html, unsafe_allow_html=True)
                    
                    # Copy grade button
                    st.markdown("---")
                    grade_text = f"{grade:.2f} / {grading_scale}"
                    
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.code(grade_text, language=None)
                        st.caption("👆 Copy this grade to paste into your LMS")
    
    # Info banner
    st.markdown("---")
    st.info("""
    **Smart Format Detection:** The app automatically extracts answers from any format—plain letters, 
    numbered lists, or punctuated sequences. Students can submit however they're comfortable.
    """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #6b6b76; font-size: 0.9em;'>"
        "Exam Grader Pro | Created by <strong>Jorge B. Cevallos</strong>"
        "</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
