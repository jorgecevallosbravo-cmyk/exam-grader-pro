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
    layout="wide"  # Use full screen width
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
    # Compact header
    col_title1, col_title2 = st.columns([3, 1])
    with col_title1:
        st.title("✓ Exam Grader Pro")
        st.caption("Generate accurate grades from multiple-choice exams with intelligent answer parsing")
    
    with col_title2:
        # Instructions expander in top right
        with st.expander("📖 How to use"):
            st.markdown("""
            1. Select grading scale
            2. Enter answer key
            3. Paste student's answer
            4. Click Calculate Grade
            
            **Accepts any format!**
            """)
    
    st.markdown("---")
    
    # Create two-column layout with equal width
    left_col, right_col = st.columns([1, 1])
    
    with left_col:
        # Configuration (compact)
        scale_option = st.selectbox(
            "⚙️ Grading Scale",
            ["10-point scale", "100-point scale", "20-point scale", "5-point scale", "Custom"]
        )
        
        if scale_option == "Custom":
            grading_scale = st.number_input("Custom Scale", min_value=1, max_value=1000, value=10, step=1)
        else:
            grading_scale = int(scale_option.split('-')[0])
        
        # Answer Key (compact)
        answer_key = st.text_area(
            "🔑 Answer Key",
            height=60,
            placeholder="ADCABCBADCBA...",
            key="answer_key"
        )
        
        # Student Answer (compact)
        student_answer = st.text_area(
            "📝 Student's Answer",
            height=120,
            placeholder="Paste answer in any format",
            key="student_answer"
        )
        
        # Buttons (compact)
        col1, col2 = st.columns(2)
        with col1:
            calculate_button = st.button("🚀 Calculate", type="primary", use_container_width=True)
        with col2:
            if st.button("Clear", use_container_width=True):
                st.rerun()
    
    # Right column - Results (always starts at top)
    with right_col:
        # Add same vertical spacing as left column's grading scale to align
        st.markdown("<div style='height: 68px;'></div>", unsafe_allow_html=True)
        
        # Process grading
        if calculate_button:
            if not answer_key or not student_answer:
                st.error("❌ Please enter both answer key and student answer.")
            else:
                # Extract letters for validation
                key_letters = extract_letters(answer_key)
                student_letters = extract_letters(student_answer)
                
                if not key_letters:
                    st.error("❌ Could not extract valid letters from answer key.")
                elif not student_letters:
                    st.error("❌ Could not extract valid letters from student answer.")
                else:
                    # Check for length mismatch
                    if len(key_letters) != len(student_letters):
                        st.warning(f"⚠️ Length mismatch: Key={len(key_letters)}, Student={len(student_letters)}")
                    
                    # Calculate grade
                    grade, correct, incorrect, total, percentage, comparison = grade_exam(
                        answer_key, student_answer, grading_scale
                    )
                    
                    if grade is not None:
                        # GRADE - BIG AND PROMINENT AT TOP
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #4299e1 0%, #667eea 100%); 
                                    padding: 32px; 
                                    border-radius: 12px; 
                                    text-align: center; 
                                    color: white;
                                    margin-bottom: 20px;
                                    box-shadow: 0 4px 12px rgba(66, 153, 225, 0.3);">
                            <div style="font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.85; margin-bottom: 12px;">
                                FINAL GRADE
                            </div>
                            <div style="font-size: 64px; font-weight: 700; letter-spacing: -2px; line-height: 1;">
                                {grade:.2f} / {grading_scale}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Compact stats - small and uniform
                        st.markdown(f"""
                        <div style="display: flex; justify-content: space-around; margin-bottom: 16px; padding: 12px; background: #f9fafb; border-radius: 8px;">
                            <div style="text-align: center;">
                                <div style="font-size: 11px; color: #6b7280; font-weight: 600; margin-bottom: 4px;">✓ CORRECT</div>
                                <div style="font-size: 18px; font-weight: 700; color: #10b981;">{correct}</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 11px; color: #6b7280; font-weight: 600; margin-bottom: 4px;">✗ INCORRECT</div>
                                <div style="font-size: 18px; font-weight: 700; color: #ef4444;">{incorrect}</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 11px; color: #6b7280; font-weight: 600; margin-bottom: 4px;">TOTAL</div>
                                <div style="font-size: 18px; font-weight: 700; color: #374151;">{total}</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 11px; color: #6b7280; font-weight: 600; margin-bottom: 4px;">PERCENTAGE</div>
                                <div style="font-size: 18px; font-weight: 700; color: #374151;">{percentage:.1f}%</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Copy grade - centered - ONLY THE NUMERIC VALUE
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 24px;">
                            <div style="display: inline-block; background: #f3f4f6; padding: 10px 20px; border-radius: 6px; font-family: monospace; font-size: 16px; color: #1f2937; border: 1px solid #e5e7eb;">
                                {grade:.2f}
                            </div>
                            <div style="font-size: 11px; color: #6b7280; margin-top: 6px;">👆 Copy to LMS</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown("---")
                        
                        # Detailed comparison - centered title
                        st.markdown("<h3 style='text-align: center; margin-bottom: 16px;'>Detailed Comparison</h3>", unsafe_allow_html=True)
                        
                        # Create DataFrame
                        import pandas as pd
                        comparison_df = pd.DataFrame(comparison)
                        comparison_df['Q'] = comparison_df['question']
                        comparison_df['Key'] = comparison_df['key']
                        comparison_df['Student'] = comparison_df['student']
                        comparison_df['✓/✗'] = comparison_df['correct'].apply(lambda x: '✓' if x else '✗')
                        
                        # Display table centered
                        st.dataframe(
                            comparison_df[['Q', 'Key', 'Student', '✓/✗']],
                            use_container_width=True,
                            hide_index=True,
                            height=300
                        )
        else:
            # Placeholder
            st.info("👈 Enter data and click Calculate to see grade here")
    
    # Compact footer - centered
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6b7280; font-size: 13px; padding: 16px 0;">
        <div style="margin-bottom: 8px;"><strong>Smart Format Detection</strong></div>
        <div>Created by <strong style="color: #374151;">Jorge B. Cevallos</strong></div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
