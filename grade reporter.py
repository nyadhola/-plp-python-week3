# Program: Grade Reporter
# Description: Processes student scores to assign grades, counts passes/fails, and calculates the average.

scores = [72, 45, 90, 61, 38]

# Trackers for passes, fails, and total sum
passed_count = 0
failed_count = 0
total_score = 0

# Process each score in the list
for score in scores:
    total_score += score  # Add to running total
    
    # Determine grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    # Track pass/fail status
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1
        
    print(f"Score: {score} - Grade: {grade}")

# Calculate average score
average = total_score / len(scores)

print("-" * 30)
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average score: {round(average, 1)}")